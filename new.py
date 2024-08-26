import requests
from bs4 import BeautifulSoup
import json

# Function to retrieve and save the content of each link
def scrape_and_save_content(links, output_file):
    content_dict = {}

    for link in links:
        try:
            # Send a GET request to the link
            response = requests.get(link)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')

                # Store the text content of the page (you can modify this to store specific parts)
                content_dict[link] = soup.get_text()

                print(f"Content retrieved from: {link}")
            else:
                print(f"Failed to retrieve content from: {link}")
        
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    # Save the content dictionary to a JSON file
    with open(output_file, 'w') as file:
        json.dump(content_dict, file, indent=4)

    print(f"All content has been saved to '{output_file}'")

# Load links from a JSON file
input_file = 'scrapped_links.json'
with open(input_file, 'r') as file:
    links_list = json.load(file)

# Define the output file for the content
output_file = 'links_content.json'

# Call the function to scrape content and save it to a JSON file
scrape_and_save_content(links_list, output_file)