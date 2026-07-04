**Task:**

You are an expert in Malayalam cinema and emoji puzzles. I am building a trivia game where players guess the Malayalam movie based entirely on a sequence of emojis representing its title or plot.

I need you to generate a new level for my game containing 15 popular Malayalam movies and automatically write the files to my project.

**Rules for the Emoji Puzzles:**
- Use a sequence of 3 to 5 emojis to represent either the literal movie name or its core plot (e.g., 🐑 🏆 🚐 for Aadu, or 🔑 🚪 💃 for Manichitrathazhu).
- The question must ONLY contain emojis. Do NOT include any text, letters, or numbers.
- Make sure the emojis cleverly but clearly point to a very famous and recognizable Malayalam movie.

**Execution Steps (Follow exactly in order):**

1. **Determine the next album name:** Look at `mal_triv_data/allLevelDetails_v3.json`. Find the last "Emoji Movies" album (e.g., "Emoji Movies 1") and increment the number to create the new album name (e.g., "Emoji Movies 2"). If it doesn't exist yet, start with "Emoji Movies 1".
2. **Update `allLevelDetails_v3.json`:** Append a new JSON object for this new album to the end of the array. Use this exact structure:
```json
{
    "name": "[New Album Name]",
    "lvls": [Number of levels],
    "cost": 150,
    "star": null,
    "is_text": true,
    "cover": 0,
    "type": "Emoji Movies"
}
```
3. **Create the Folder:** Create a new directory at `mal_triv_data/[New Album Name]/`.
4. **Write `units.json`:** Generate an array of 15 movie names (ALL CAPS) and write it to `mal_triv_data/[New Album Name]/units.json`.
5. **Write `questions.json`:** Generate an array of 15 emoji sequences matching the exact order of `units.json`, and write it to `mal_triv_data/[New Album Name]/questions.json`.

Please proceed with generating and writing the files!
