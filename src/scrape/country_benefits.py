# Gather data on what countries offer, free health insurance etc.
# Maternity Leave, PTO Days, Working Hours, Paid Holidays Off, Cleaniness, 
# https://www.william-russell.com/blog/countries-best-worker-benefits/#method

from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://codesubmit.io/blog/software-engineer-salary-by-country/'
)

print(response.status_code)