# LinkedIn Scrape

This project is designed to scrape data from LinkedIn for research or analysis purposes for my Apply Beast Project. Please ensure you comply with LinkedIn's terms of service and any applicable laws when using this tool.

Includes Batching and dynamic writes to CSV file
Uses Data Kund Library

## Features

- Extract public profile information.
- Scrape job postings and company details.
- Export data in CSV or JSON format.

## Requirements

- Python 3.8 or higher
- Required libraries (see `requirements.txt`)

### 1. Clone the Repository

```bash
git clone https://github.com/jangamnoelpaulmoses/linkedin_scraper.git
cd linkedin-scraper
```

### 2. Set Up the Environment

```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

##  Usage

Run the script:

1. Paste the LinkedIn post URL of the post and enter the output file name in run.py
2. Run below command:
```bash
python run.py
```
3. A chrome window pops up, manually log in to your LinkedIn account.
4. Visit the terminal, hit Enter.
5. When the dropdown appears, **manually select "Most recent" or "Most Relevant"**.
6. Visit terminal, hit **Enter** to begin scraping.


##  Output
All comments are saved to:
```
comments.csv
```