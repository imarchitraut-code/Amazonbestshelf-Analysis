#Amazonbestshelf-Analysis
# BookInsights

**[View Live Dashboard](https://amazonbestshelf-analysis-xkfyqmqljnaifkf8szb2xk.streamlit.app/)**

An interactive Streamlit web application for exploring and analyzing Amazon's Top 50 Best-Selling Books (2009-2019). The app allows users to search, filter, and visualize trends across authors, genres, user ratings, and prices using the Python library Pandas.
An interactive Streamlit web application for exploring and analyzing Amazon's Top 50 Best-Selling Books (2009-2019). The app allows users to search, filter, and visualize trends across authors, genres, user ratings, and prices using the Python library Pandas.

## Overview

This project takes a static dataset of 550 bestselling books and turns it into an interactive analysis tool. Users can browse the full dataset, search for specific authors or titles, filter books by custom price and rating ranges, and view visualizations of genre distribution and author frequency.

## Features

- Full dataset browser with a scrollable, sortable table
- Search by author name (case-insensitive, partial match supported)
- Search by book title (case-insensitive, partial match supported)
- Adjustable view of the most and least frequently best-selling authors
- Genre distribution visualized as a bar chart
- Average user rating and price grouped by genre, with price formatted as currency
- Custom filtering by price range and user rating range simultaneously
- Correlation analysis between book price and user rating
- Identification of the most frequently appearing book in the dataset

## Dataset

This project uses the Amazon Top 50 Bestselling Books 2009-2019 dataset, available on Kaggle:
https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019

The dataset contains 550 entries across 7 columns: Name, Author, User Rating, Reviews, Price, Year, and Genre.

## Tech Stack

- Python 3
- Streamlit
- Pandas
- Matplotlib

## Installation

1. Clone the repository

```
git clone https://github.com/imarchitraut-code/Amazonbestshelf-Analysis.git
cd Amazonbestshelf-Analysis

```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Download the dataset from Kaggle (link above) and place the CSV file, named `bestsellers with categories-bestsellers with categories.csv`, in the project root directory.

## Usage

Run the application with:

```
streamlit run amzonbestsellingbooks.py
```

If the above command is not recognized, use:

```
python -m streamlit run amzonbestsellingbooks.py
```

The application will open automatically in a browser window at `http://localhost:8501`.

## Project Structure

```
Amazonbestshelf-Analysis/
├── amzonbestsellingbooks.py
├── requirements.txt
├── README.md
└── bestsellers with categories-bestsellers with categories.csv
```

## License

This project is licensed under the MIT License.
