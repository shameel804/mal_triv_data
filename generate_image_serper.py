import os
import json
import time
import requests
from io import BytesIO
from PIL import Image

BASE_DIR = "/Users/shameelabid/MyWork/Guess Malayalam Movies/mal_triv_data"
FILE_NAME = "allLevelDetails_v3.json"
TARGET_TYPE = "New Movie"  # Only process albums with this type

# ==========================================
# ENTER YOUR SERPER.DEV API KEY HERE
# Get 2,500 free searches at https://serper.dev
API_KEY = "663a70b97d4891afcc36326702d68336af374ad3"
# ==========================================

def download_image_from_serper(app_name, save_path):
        
    # Using minus operators to exclude posters, titles, and logos from the search results
    query = f"{app_name} Malayalam movie stills -poster -title -text -logo -typography"
    print(f"Searching Web (Serper/Google Images) for: {query}")
    
    url = "https://google.serper.dev/images"
    payload = json.dumps({
        "q": query
    })
    headers = {
        'X-API-KEY': API_KEY,
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        images = data.get("images", [])
        if not images:
            print(f"  -> No results found on web for {app_name}")
            return False
            
        req_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        # Try the top 3 images
        for result in images[:3]:
            image_url = result.get("imageUrl")
            if not image_url:
                continue
                
            try:
                img_resp = requests.get(image_url, headers=req_headers, timeout=10)
                img_resp.raise_for_status()
                
                img = Image.open(BytesIO(img_resp.content))
                # Ensure it's in a mode that can be saved as WEBP
                if img.mode not in ('RGB', 'RGBA'):
                    img = img.convert('RGB')
                    
                img.save(save_path, "WEBP")
                print(f"  -> Saved web image: {save_path}")
                return True
            except Exception as e:
                print(f"  -> Failed to download/save {image_url}: {e}")
                continue
                
        return False
    except Exception as e:
        print(f"  -> Error fetching API for {app_name}: {e}")
        return False

def main():
    json_file = os.path.join(BASE_DIR, FILE_NAME)
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    failed_images = []
        
    for item in data:
        if TARGET_TYPE and item.get("type") != TARGET_TYPE:
            continue
            
        is_text = item.get("is_text", False)
        if is_text:
            continue
            
        album_name = item.get("name")
        album_dir = os.path.join(BASE_DIR, album_name)
        units_file = os.path.join(album_dir, "units.json")
        img_dir = os.path.join(album_dir, "img")
        
        if not os.path.exists(units_file):
            print(f"Skipping {album_name}: units.json not found.")
            continue
            
        print(f"\n--- Processing {album_name} ---")
        with open(units_file, 'r', encoding='utf-8') as f:
            units = json.load(f)
            
        for idx, app_name in enumerate(units):
            image_num = idx + 1
            save_path = os.path.join(img_dir, f"{image_num}.webp")
            
            if os.path.exists(save_path):
                print(f"[{image_num}/{len(units)}] {app_name} image already exists. Skipping.")
                continue
                
            print(f"[{image_num}/{len(units)}] Fetching {app_name}...")
            
            success = download_image_from_serper(app_name, save_path)
            if not success:
                print(f"  -> Skipping {app_name} due to download failure.")
                failed_images.append(f"{album_name} - {app_name} (Index: {image_num})")
            
            # Very small sleep just in case, though API limits handle the rest
            time.sleep(0.5)

    print("\n=========================================")
    if failed_images:
        print("SUMMARY: The following images FAILED to download and were skipped:")
        for fail in failed_images:
            print(f" - {fail}")
        print("Please add these manually.")
    else:
        print("SUMMARY: All images downloaded successfully!")
    print("=========================================\n")

if __name__ == "__main__":
    main()
