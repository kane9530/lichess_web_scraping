# lichess_web_scraping

My writeup of this project was uploaded in the Lichess webpage here:
https://lichess.org/@/bompipi95/blog/a-data-driven-deep-dive-into-lichess-coaches/KvYjULSR

The dataset is also shared via Kaggle datasets:
https://www.kaggle.com/datasets/kane9530/lichess-coaches-22april2024

- [lichess\_web\_scraping](#lichess_web_scraping)
  - [Download Lichess Coaches csv file](#download-lichess-coaches-csv-file)
  - [Installation](#installation)
  - [Background](#background)
    - [Dataset Dimensions](#dataset-dimensions)
    - [Motivation](#motivation)
  - [Running Scrapy](#running-scrapy)
  - [File/folder descriptions](#filefolder-descriptions)

## Download Lichess Coaches csv file

Dataset can be downloaded from kaggle using the kaggle API:
```
kaggle datasets download -d kane9530/lichess-coaches-22april2024
```
or directly from the kaggle datasets page [here](https://www.kaggle.com/datasets/kane9530/lichess-coaches-22april2024/data)

## Installation

Install the specified packages in a conda environment using the `requirements.txt` file:

```bash
conda install --file requirements.txt
```

## Background

Web scraping results from the [lichess coaches web page](lichess.org/coach) on `22/4/2024`. 

### Dataset Dimensions
Entries: 1632 rows
Attributes: 18 columns

### Motivation
As an active player on Lichess, an open-source chess server, I am seeking to enhance my chess skills through affordable and experienced coaching. The project is motivated by several needs and interests:

- Usability Improvements: The Lichess coaches page lacks convenient filters for searching coaches based on lesson rates, chess ratings, or titles.
Coaching Analytics: I am interested in analyzing how a coach's chess strength correlates with their lesson rates and exploring the distribution of coaches by title and geography.

- Skill Development: This project also serves as a practical application to learn web scraping using Scrapy and to practice programming with the ChatGPT API.

- Methodology
I utilized Scrapy, a robust Python framework for web crawling, to scrape data from the Lichess Coaches webpage. The site uses infinite scrolling to display coach profiles, which initially complicated data extraction. By analyzing the HTML structure, I devised a method to systematically navigate the site by incrementing page numbers in the URL (login?page=<number>). For each coach listed, I captured the Lichess username, then accessed their detailed coaching bio to extract comprehensive data.

Due to the varied formats coaches use to list their rates, the data required cleaning. I employed the ChatGPT-3.5-turbo API to standardize rate information into a uniform format, focusing on hourly rates and corresponding currencies (ISO 4217 standard). The `location` column was also cleaned to identify the countries of the coaches.


## Running Scrapy

Run the Scrapy `lichessSpider` crawler with:
```bash
scrapy crawl lichessSpider
```

## File/folder descriptions

- `chatgpt_3.5_turbo_clean.ipynb` : Contains the prompts and code used to clean the chess lesson rates and geographical location  columns from the web scraped csv file.
  
- `lichess/`: scrapy folder.




