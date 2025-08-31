# Gather data on what countries offer, free health insurance etc.
from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://codesubmit.io/blog/software-engineer-salary-by-country/'
)

print(response.status_code)