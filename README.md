# YouTube Trending Video Analysis

## Overview
This project analyzes trending YouTube videos to uncover insights about video popularity, categories, and engagement metrics. Using a dataset from [Kaggle: YouTube Trending Videos](https://www.kaggle.com/datasnaek/youtube-new), this project demonstrates data cleaning, exploratory data analysis, and interactive visualizations using Python, Pandas, Seaborn, Matplotlib, and Plotly Dash.

---

## Project Structure
YouTube-Trending-Analysis/
│
├─ data/ # Raw CSV datasets
├─ output/ # Cleaned CSVs and generated charts
├─ src/
│ ├─ 00_data_cleaning.py # Scripts to clean and preprocess the data
│ ├─ 01_data_analysis.py # Scripts to perform analysis (counts, trends)
│ └─ 02_visualizations.py # Scripts to generate charts and interactive dashboard
├─ README.md
└─ requirements.txt # Python dependencies

## Dataset
- The dataset contains trending videos for multiple countries.
- Key columns:
  - `video_id`: unique video identifier
  - `title`: video title
  - `channel_title`: channel name
  - `category_id`: video category
  - `publish_time`: upload timestamp
  - `trending_date`: date when video trended
  - `views`, `likes`, `dislikes`, `comment_count`
  - `tags`: video tags separated by `|`

---
