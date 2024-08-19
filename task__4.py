import requests
from bs4 import BeautifulSoup
import csv

def scrape_products(url):
  """Scrapes product information from an e-commerce website and saves it to a CSV file.

  Args:
      url: The URL of the e-commerce website.

  Returns:
      None. Saves the scraped data to a CSV file.
  """

  # Get the HTML content of the website
  response = requests.get(url)
  response.raise_for_status()  # Raise an exception for bad status codes
  html_content = response.text

  # Parse the HTML content using BeautifulSoup
  soup = BeautifulSoup(html_content, 'html.parser')

  # Find the product elements on the page (adjust selectors as needed)
  products = soup.find_all('div', class_='product')  # Example selector, change as required

  # Create a list to store the scraped product information
  product_data = []

  # Loop through each product and extract the relevant information
  for product in products:
    # Extract the product name, price, and rating using BeautifulSoup
    name = product.find('h2', class_='product-title').text.strip()
    price = product.find('span', class_='product-price').text.strip()
    rating = product.find('span', class_='product-rating').text.strip()

    # Append the product information to the list
    product_data.append([name, price, rating])

  # Save the scraped data to a CSV file
  with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Grocery', 'Price', 'Rating'])

    # Write the product data to the CSV file
    writer.writerows(product_data)

  print('Product information scraped and saved to products.csv')

# Example usage
scrape_products('https://www.flipkart.com/')  