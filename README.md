## Internshala Internships Scraper
This is a Python script to scrape internship data from the website https://internshala.com/. The script collects internship details such as Title, Company, Location, Duration, Stipend, and Link for remote internships and saves the data in a JSON file.

## Running the Script
To run the script, follow these steps:

1. Install the necessary libraries using pip install -r requirements.txt
2. Run the scrape.py file using the command python scrape.py
3. The script will start scraping data from all pages (100 pages by default) of the website.
4. The scraped data will be saved in a file named internships.json.
Note: The script has a sleep time of 1-3 seconds after each page request to avoid getting blocked by the website.

## Libraries used
The following libraries are used in this script:
1. BeautifulSoup: For parsing HTML content.
2. Requests: For making HTTP requests to the website.
3. Pandas: For data manipulation and analysis.

## Disclaimer
This script is intended for educational purposes only. Scraping data from websites without permission may be illegal and violate the website's terms of service. Use this script at your own risk.

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for details.
