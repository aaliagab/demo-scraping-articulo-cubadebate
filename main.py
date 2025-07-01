import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv

load_dotenv()

TARGET_URL = os.environ.get("TARGET_URL")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

def scrape_article_content(soup):
    """
    Scrapes the article's title, author, and body from the parsed BeautifulSoup object.
    """
    print("Extracting article content...")
    title_meta_element = soup.select_one('meta[property="og:title"]')
    author_element = soup.select_one('section#relates p.seriestitle a')
    entry_div = soup.select_one('div.entry')
    body_text = ""
    if entry_div:
        body_elements = entry_div.select('p')
        body_text = "\n\n".join([p.get_text(strip=True) for p in body_elements])
    else:
        print("Could not find the main article container ('div.entry').")
    
    article_data = {
        'title': title_meta_element.get('content').replace('- Cubadebate', '').strip() if title_meta_element else "Title not found",
        'author': author_element.get_text(strip=True) if author_element else "Author not found",
        'body': body_text if body_text else "Body not found"
    }
    print("Article content extracted successfully.")
    return article_data

def scrape_comments(soup):
    """
    Scrapes the comments from the article.
    """
    print("Extracting comments...")
    comments_list = []
    comment_elements = soup.select('li.comment')
    if not comment_elements:
        print("No comment elements found on the page.")
        return []
    
    for comment_element in comment_elements:
        author_element = comment_element.select_one('div.commenttext cite')
        text_element = comment_element.select_one('div.commenttext p')
        date_element = comment_element.select_one('div.commentmetadata')
        comments_list.append({
            'author': author_element.get_text(strip=True).replace('dijo:', '').strip() if author_element else 'Anonymous',
            'date': date_element.get_text(strip=True) if date_element else 'No date',
            'comment_text': text_element.get_text(strip=True) if text_element else 'Text not found'
        })
    print(f"Extracted {len(comments_list)} comments.")
    return comments_list


def main():
    """
    Main function that orchestrates the scraping and data export to a single JSON file.
    """
    if not TARGET_URL:
        print("Error: TARGET_URL not found in environment variables. Please create a .env file.")
        return
        
    print(f"Fetching content from: {TARGET_URL}")
    print(f"Using headers: {HEADERS}")
    try:
        response = requests.get(TARGET_URL, headers=HEADERS, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")
        return
        
    soup = BeautifulSoup(response.text, 'html.parser')
    
    article_info = scrape_article_content(soup)
    comments = scrape_comments(soup)
    
    print("\n" + "="*50)
    print("SCRAPING SUMMARY")
    print("="*50)
    print(f"Title: {article_info['title']}")
    print(f"Author: {article_info['author']}")
    print(f"Total comments: {len(comments)}")
    print("="*50 + "\n")

    final_data = {
        'url_source': TARGET_URL,
        'article': article_info,
        'comments': comments
    }

    output_filename = "article_complete.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)
    
    print(f"All data has been saved to a single file: '{output_filename}'")


if __name__ == '__main__':
    main()