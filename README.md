# Overlayy

Overlayy is a Python-based web scraping tool designed to extract, store, and analyze links from a given webpage. It fetches all the links from a specified URL, stores them in a JSON file, and then scrapes the content of each linked page. This tool helps in collecting and analyzing webpage content efficiently.

## Features

- **Link Extraction**: Extracts all links from the specified webpage.
- **JSON Storage**: Saves the extracted links into a scapped links JSON file.
- **Content Scraping**: Fetches and scrapes the content of each linked page.
- **Structured Output**: Stores the webpage content along with its URL for easy access and analysis(links_content.json).

## Requirements

To run Overlayy, you need the following Python libraries:

- `requests`
- `beautifulsoup4`

You can install these dependencies using pip:

```
pip install requests beautifulsoup4
```

## Usage
Clone the Repository:
Copy code
```
git clone <repository-url>
cd overlayy
```

Run the Script:
```
python overlayy.py <url>
```
Replace <url> with the URL of the webpage you want to scrape. For example:
```
python overlayy.py https://example.com
```

