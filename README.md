# Elder Scrolls V: Skyrim Chat Bots

Chat bots for Elder Scrolls V: Skyrim NPCs


## Setup
---

### Requirements:
- [PDM](https://pdm.fming.dev/latest/)
- Python 3.10

### From Source:
1. `git clone`
2. `eval $(pdm venv activate in-project)`
3. `pdm install`

### Post install:
Export environment variables:
```bash
export NLTK_DATA=./nltk_data
```

## Run the Natural Language Processing Demo:
```bash
cd bots/
python natural_language_processing.py
```