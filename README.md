
---

### **README.md (English Version)**

```markdown
# Article and Comments Web Scraper

This project is a professional web scraping demonstration developed in Python. The script is designed to extract the full content of a news article (title, author, and body) along with all its comments, and consolidate all the information into a single, well-structured JSON file.

## Features

- **Content Extraction:** Scrapes the article's title, author, and body.
- **Comment Extraction:** Gathers all comments from the post, including the commenter's name, date, and text.
- **Structured Output:** Exports all data to a single `JSON` file for easy consumption by other applications.
- **Professional Setup:** Uses environment variables to manage the target URL, separating configuration from code.
- **Dependency Management:** Includes a `requirements.txt` file for a quick and easy environment setup.

## Prerequisites

- Python 3.8 or higher
- pip (usually comes with Python)

## Installation and Setup

Follow these steps to set up and run the project from scratch.

**1. Clone or download the repository**

Get the project files on your local machine.

```bash
# If using git
git clone <REPOSITORY_URL>

# Or just download and unzip the project

cd /path/to/your/project

# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate

# On macOS / Linux:
source venv/bin/activate

pip install -r requirements.txt

# On Windows (PowerShell):
New-Item .env

# On macOS / Linux:
touch .env

TARGET_URL="http://www.cubadebate.cu/especiales/2025/06/21/como-los-hackers-de-elite-se-infiltran-y-permanecen-invisibles-en-nuestros-sistemas-informaticos/"

python main.py