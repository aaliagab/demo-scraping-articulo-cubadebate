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
git clone https://github.com/aaliagab/demo-scraping-articulo-cubadebate.git

# Or just download and unzip the project
```

**2. Navigate to the project directory**

```bash
cd /path/to/your/project
```

**3. Create and activate a virtual environment**

It is a best practice to isolate project dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate

# On macOS / Linux:
source venv/bin/activate
```
*After activation, your terminal prompt should be prefixed with `(venv)`.*

**4. Install dependencies**

This command will read the `requirements.txt` file and install everything needed.

```bash
pip install -r requirements.txt
```

**5. Configure environment variables**

Create a file named `.env` in the project's root directory (next to `main.py`).

```bash
# On Windows (PowerShell):
New-Item .env

# On macOS / Linux:
touch .env
```

Open the `.env` file with a text editor and add the following line:

```
TARGET_URL="http://www.cubadebate.cu/especiales/2025/06/21/como-los-hackers-de-elite-se-infiltran-y-permanecen-invisibles-en-nuestros-sistemas-informaticos/"
```

## Usage

Once the environment is set up and activated, simply run the main script:

```bash
python main.py
```

The script will display its progress in the console.

## What do we get? (Output)

Upon completion, a single file named `article_complete.json` will be generated in the same folder. This file will contain all the scraped data with the following structure:

```json
{
    "url_source": "http://www.cubadebate.cu/...",
    "article": {
        "title": "Cómo los hackers de élite se infiltran y permanecen invisibles en nuestros sistemas informáticos",
        "author": "Antonio Hernández Domínguez",
        "body": "En 2016, mis estimados lectores, un prestigioso hospital universitario en Alemania descubrió algo alarmante..."
    },
    "comments": [
        {
            "author": "Yo",
            "date": "21 junio 2025 a las 19:23",
            "comment_text": "Muy buena esta sesión de ciberseguridad, enseña al lector sobre temas que desconoce..."
        },
        {
            "author": "Adrián Castellano Martínez",
            "date": "22 junio 2025 a las 12:06",
            "comment_text": "Increíble artículo y muestra de una irresponsable e injustificada ingenuidad..."
        }
    ]
}
```
```