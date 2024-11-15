# TODO: Scrape data from best family guy quotes

"""This is a summary
In this portion we will be using the requests library to scrape data from the website
requests is a library that allows us to make HTTP requests in Python
while,BeautifulSoup is a library that allows us to parse HTML and XML documents

"""
import requests
from bs4 import BeautifulSoup
from save_csv import save_to_csv



### ========================================================================================###
"""
Requests is a library that allows us to make HTTP requests in Python
Args:
{URL} : The URL to make the request to
Params:
The status code of the response

"""

URL = "https://www.scarymommy.com/family-guy-quotes/"


def get_data(URL):
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


##===========================================================================================##

"""
BeautifulSoup is a library that allows us to parse HTML and XML documents
Args:
html_content (str): The raw HTML content to be parsed.

    Returns:
        list: A list of parsed data (e.g., quotes) extracted from the HTML.

    Raises:
        ValueError: If the HTML content is empty or None.

"""


def parse_data(html_content):
    if not html_content:
        raise ValueError("HTML content is empty or None.")

    soup = BeautifulSoup(html_content, "html.parser")

    target_element = soup.select_one(".AOL > ol:nth-child(5)")
    if target_element:
        # Extract the text content and split into individual quotes
        raw_text = target_element.get_text(strip=True)
        # Split by sentence endings or custom delimiters
        quotes = [quote.strip() for quote in raw_text.split("“") if quote]
        return quotes
    else:
        print("The specified element was not found.")
        return []
    


   
if __name__ == "__main__":
    # Define the URL
    URL = "https://www.scarymommy.com/family-guy-quotes/"
    
    html_content = get_data(URL)
    if html_content:
        quotes = parse_data(html_content)
        if quotes:
            save_to_csv(quotes, "family_guy_quotes.csv")  # Save quotes to CSV
            print("Quotes saved to 'family_guy_quotes.csv'.")
