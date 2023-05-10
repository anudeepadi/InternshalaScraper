# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random

# Define a function to get BeautifulSoup object of a URL
def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

# Set initial variables for scraping
url = 'https://internshala.com/internships/work-from-home-internships/page-'
pages = 100
internships = []

# Loop through all pages and collect internship data
for page in range(pages):
    soup = get_soup(url + str(page))
    internships.extend(soup.find_all('div', {'class': 'individual_internship'}))
    time.sleep(random.randint(1, 3))

# Create a dictionary to store internship data
internship_dict = { 
    'Title': [],
    'Company': [],
    'Location': [],
    'Duration': [],
    'Stipend': [],
    'Link': []
}

# Loop through all internships and store data in dictionary
for i in internships:
    internship_dict['Title'].append(i.find('a', class_ = 'view_detail_button').text)
    internship_dict['Company'].append(i.find('a', class_ = 'link_display_like_text view_detail_button').text)
    internship_dict['Location'].append(i.find('a', class_ = 'location_link view_detail_button').text)
    internship_dict['Duration'].append(i.find_all('div', class_ = 'item_body')[1].text)
    if i.find('span', class_ = 'stipend') == None:
        internship_dict['Stipend'].append('None')
    else:
        internship_dict['Stipend'].append(i.find('span', class_ = 'stipend').text)
    internship_dict['Link'].append("https://internshala.com" + i.find('a', class_ = 'view_detail_button')['href'])
    
# Create a pandas dataframe from the internship dictionary
df = pd.DataFrame(internship_dict)

# Remove unnecessary characters and duplicates from the dataframe
df = df.replace(r'\n', '', regex=True)
df = df.replace(r'\t', '', regex=True)
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Strip leading and trailing spaces from Company and Duration columns
df['Company'] = df['Company'].str.strip()
df['Duration'] = df['Duration'].str.strip()

# Print the number of internships scraped
print("The number of internships scraped are:", len(df))

# Replace 'incentives' with '' in Stipend column if present
if 'incentives' in df['Stipend']:
    df['Stipend'] = df['Stipend'].replace('incentives', '')

# Sort the dataframe by Stipend column in ascending order
df.sort_values(by=['Stipend'], inplace=True, ascending=True)

# Save the sorted dataframe as a JSON file
df.to_json('internships.json', orient='records')
