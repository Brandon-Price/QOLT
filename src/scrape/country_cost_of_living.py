# Find data on how much it costs to live in a particular country, from rent, food, insurance, internet, price per good (how strong the currency is against the price of the good)
from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://codesubmit.io/blog/software-engineer-salary-by-country/'
)

print(response.status_code)