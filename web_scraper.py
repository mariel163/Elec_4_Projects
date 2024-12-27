import requests
from bs4 import BeautifulSoup
import csv

# URL of the page to scrape
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # List to store the Nation and Population data
    data = []

    # Locate the table containing the data
    table = soup.find('table', class_='wikitable')

    if table:
        # Iterate through rows of the table
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            if len(columns) > 1:  
                nation = columns[0].text.strip()  # Nation name
                population = columns[1].text.strip()  # Population
                data.append([nation, population])

        # Write data to a CSV file
        with open('data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Nation', 'Population'])  
            writer.writerows(data)

        print("Scraping completed. Data saved to data.csv")
    else:
        print("Table not found on the page. Check the structure.")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")


                       
                          
