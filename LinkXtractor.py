#!/usr/bin/python3

import argparse
import requests
import re
import warnings
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore", category=UserWarning, module='html.parser')


# Function to read URLs from a text file
def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        url_pattern = r'(https?://[^\s]+)'
        
        infile = file.read()
        urls = re.findall(url_pattern, infile)
    # Remove any trailing whitespace characters (e.g., newlines)
    urls = [url.strip() for url in urls]
    return urls
    
# Function to extract only HTTP/HTTPS URLs from text
#def extract_urls_from_text(text_content):
    # Regular expression pattern for HTTP/HTTPS URLs
#    url_pattern = r'(https?://[^\s]+)'
    
    # Find all URLs matching the pattern
#    urls = re.findall(url_pattern, text_content)
    
    # Return unique URLs by converting to a set
#    return set(urls)

# Function to extract URLs from HTML content
def extract_urls_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    urls = set()

    # Find all anchor tags and extract href attributes that start with http/https
    for link in soup.find_all('a', href=True):
        href = link['href']
        if '//' in href:
            urls.add(href)  # Add the filtered URL to the set

    return urls

# Function to process URLs and extract URLs from the HTML content
def process_urls(file_path):
    url_list = read_urls_from_file(file_path)

    for url in url_list:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Extract the HTML content
                html_content = response.text
                
                # Extract all URLs from the HTML content
                extracted_urls = extract_urls_from_html(html_content)
                
                if len(extracted_urls) != 0:
                	# Print or save the extracted URLs
	                print(f"\nExtracted URLs from {url}:")
        	        for extracted_url in extracted_urls:
        	            print(extracted_url)

            else:
                print(f"\nFailed to retrieve {url}. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"\nError occurred while trying to access {url}: {e}")

def printArt():
    art = r"""
 (                        )                                      
 )\ )               )  ( /(     )                    )           
(()/( (          ( /(  )\()) ( /( (       )       ( /(      (    
 /(_)))\   (     )\())((_)\  )\()))(   ( /(   (   )\()) (   )(   
(_)) ((_)  )\ ) ((_)\ __((_)(_))/(()\  )(_))  )\ (_))/  )\ (()\  
| |   (_) _(_/( | |(_)\ \/ /| |_  ((_)((_)_  ((_)| |_  ((_) ((_) 
| |__ | || ' \))| / /  >  < |  _|| '_|/ _` |/ _| |  _|/ _ \| '_| 
|____||_||_||_| |_\_\ /_/\_\ \__||_|  \__,_|\__|  \__|\___/|_|   

Author: Murray R
                                              
    """
    print(art)


# Main function to handle input argument
def main():
    printArt()
    	
    # Setup argparse to handle the input argument
    parser = argparse.ArgumentParser(description='Process a list of URLs from a text file and extract URLs from HTML content.')
    parser.add_argument('file', type=str, help='Path to the text file containing URLs')

    # Parse the argument
    args = parser.parse_args()

    if args.file is None:
        print("Usage: ./LinkXtractor.py <file_path>")
        print("Provide a path to a text or HTML file to search for URLs containing '//'.")
        return	
        
    # Process the URLs using the provided file
    process_urls(args.file)

if __name__ == '__main__':
    main()
