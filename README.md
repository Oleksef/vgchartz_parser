# VGChartz Game Sales Parser

A simple Python-based parser that extracts game sales data from [VGChartz](https://www.vgchartz.com/games/games.php) and saves it to a CSV file for further processing.

> ⚠️ Note: This parser collects raw data and does not clean or normalize it. It's intended for use in data pipelines where further processing will be applied.
> 
> This parser absolutely *could (and should)* be improved — with logging, better structure, and proper error handling.
> However, the main goal was to create a ***"workflow"*** where the maximum raw data is provided for analysis and processing, which was achieved.

---

## 📦 Features

- Collects data on:
  - Game title
  - Platform
  - Publisher & Developer
  - VGChartz score, critic/user scores
  - Regional and global sales figures
  - Release date
- Exports data to `games.csv`
- Supports automatic pagination (fetches all available pages)
  
---

## 🛠 Requirements

- Python 3.7+
- `requests`
- `pandas`
- `lxml`

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run
```bash
python vgchartz_parser.py
```
This will fetch all game data from VGChartz and export it to games.csv in the same directory.

---

## 📂 Output
The output file `games.csv` contains one row per game with the following columns:
- name
- platform
- publisher
- developer
- vgs_score
- critic_score
- user_score
- total_shipped
- total_sales
- na_sales
- pal_sales
- jp_sales
- other_sales
- release_date

[Sample output CSV](./games.csv).

---

## ⚙️ Code Structure
- `run(start_url)` – handles pagination and sends HTTP requests.
- `process_gamelist(tree)` – extracts data from a single page of results.
- Output is stored in a list of dictionaries and then exported via `pandas`.

---

## 🧑‍💻 Contributing
Feel free to use, fork, or suggest improvements via pull requests or issues.

Found a bug or want to suggest a feature? Open an issue [here](https://github.com/Oleksef/vgchartz_scraper/issues).
