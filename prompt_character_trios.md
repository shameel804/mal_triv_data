**Task:**

You are an expert in Malayalam cinema. I am building a trivia game where players guess the Malayalam movie based on the names of 3 iconic characters from that movie.

I need you to generate a new level for my game containing 15 popular Malayalam movies and automatically write the files to my project.

**Rules for the Character Trios:**
- List exactly 3 iconic character names from the movie, separated by commas (e.g., "Ramanan, Udayabhanu, Kousalya" for Punjabi House).
- Do NOT include any actor names or the movie name itself.
- Keep it entirely focused on the fictional character names.
- Make sure the movies and characters are very famous and recognizable to a Malayali audience.

**Execution Steps (Follow exactly in order):**

1. **Determine the next album name:** Look at `mal_triv_data/allLevelDetails_v3.json`. Find the last "Character Trios" album (e.g., "Character Trios 1") and increment the number to create the new album name (e.g., "Character Trios 2"). If it doesn't exist yet, start with "Character Trios 1".
2. **Update `allLevelDetails_v3.json`:** Append a new JSON object for this new album to the end of the array. Use this exact structure:
```json
{
    "name": "[New Album Name]",
    "lvls": [Number of levels],
    "cost": 150,
    "star": null,
    "is_text": true,
    "cover": 0,
    "type": "Character Trios"
}
```
3. **Create the Folder:** Create a new directory at `mal_triv_data/[New Album Name]/`.
4. **Write `units.json`:** Generate an array of 15 movie names (ALL CAPS) and write it to `mal_triv_data/[New Album Name]/units.json`.
5. **Write `questions.json`:** Generate an array of 15 character trios matching the exact order of `units.json`, and write it to `mal_triv_data/[New Album Name]/questions.json`.

Please proceed with generating and writing the files!
