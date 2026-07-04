**Task:**

You are an expert in Malayalam cinema. I am building a trivia game where players guess the Malayalam movie based on a famous, iconic dialogue from that movie.

I need you to generate a new level for my game containing 15 popular Malayalam movies and their famous dialogues, and automatically write the files to my project.

**Rules for the Dialogues:**
- The dialogues should be iconic and easily recognizable to any Malayali movie fan.
- Write the dialogues in Malayalam.
- Do NOT include the character name or actor name who says it, just the quote itself.
- Make sure the movies are very famous and recognizable.

**Execution Steps (Follow exactly in order):**

1. **Determine the next album name:** Look at `mal_triv_data/allLevelDetails_v3.json`. Find the last "Dialogues" album (e.g., "Dialogues 1") and increment the number to create the new album name (e.g., "Dialogues 2").
2. **Update `allLevelDetails_v3.json`:** Append a new JSON object for this new album to the end of the array. Use this exact structure:
```json
{
    "name": "[New Album Name]",
    "lvls": [Number of levels],
    "cost": 150,
    "star": null,
    "is_text": true,
    "cover": 0,
    "type": "Dialogues"
}
```
3. **Create the Folder:** Create a new directory at `mal_triv_data/[New Album Name]/`. I want more than 7 albums. Currently the "Dialogue 1" is made for testing. So remove existing and start your generation from 1.
4. **Write `units.json`:** Generate an array of 15 movie names (ALL CAPS) and write it to `mal_triv_data/[New Album Name]/units.json`.
5. **Write `questions.json`:** Generate an array of 15 Movie dialogues matching the exact order of `units.json`, and write it to `mal_triv_data/[New Album Name]/questions.json`.

Please proceed with generating and writing the files!
