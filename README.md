# FantanoScraper

## Table of Contents
1. [Description](#description)
2. [Concepts used](#concepts-used)
3. [Files Overview](#files-overview)
4. [Setup](#setup)

## Description
**FantanoScraper** is a Python-based web scraper designed to extract data from the theneedledrop channel. The project aims to compare the sentiment analysis of:
- The transcript of the review (classified by sentiment models).
- The numerical rating given by the reviewer.
- The score it was given on Album of the Year (AOTY) and Rate Your Music (RYM). (present in the pdf for the poject)
- The sentiment of the YouTube comments under the reviews.
We analyze how controversial the review was and the amount of discourse it generated in the comments. The project helps visualize the relationship between audience perception and critic reviews using various sentiment analysis tools.

## Concepts used
- **Web Scraping**: Extracting review transcripts and comments from YouTube videos.
- **Natural Language Processing (NLP)**: Cleaning and analyzing text using `nltk`, `text2emotion`, and sentiment classifiers.
- **Data Visualization**: Graphing sentiment distributions using `matplotlib`.
- **Automation**: Organizing scraped data and generating insights for multiple albums.

## Files Overview

### Main Scripts
- `main.py`: Entry point of the project, iterating over the list of albums and calling the `organizer` function.
- `organizer.py`: Manages the overall data extraction and processing workflow.

### Scraping
- `scraping/pullCommentsDF.py`: Converts YouTube comments into a DataFrame.
- `scraping/pullCommentsTXT.py`: Saves comments as a text file.
- `scraping/getFantanoTranscript.py`: Retrieves the transcript of the video.

### Sentiment Analysis
- `sentiment/barGraphs.py`: Generates bar graphs for sentiment comparison.
- `sentiment/emotionBars.py`: Processes and visualizes emotions in the comments.


## Setup
### Prerequisites
Ensure you have Python installed (version 3.7+ recommended). Then, install the required dependencies using:

### Dependencies
The project requires the following libraries:
- google-api-python-client
- youtube-transcript-api
- nltk
- text2emotion
- matplotlib
- pandas
- torch
- transformers
- re

### Usage
To run the scraper, execute the following command:
```sh
python main.py
```
This will process all the albums listed in `main.py`, extract data, perform sentiment analysis, and generate visualizations.

---
Thank you for checking out **FantanoScraper**! 🎵