import requests
import whois
import logging
import ssl
from datetime import datetime
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Configuration Options
LOG_FILE_PATH = 'phishing_detector.log'
RECENT_REGISTRATION_DAYS = 30
MAX_WORKERS = 10
REQUEST_TIMEOUT = 5
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
BLACKLIST_URL = 'https://www.some-blacklist-service.com/check?domain='

# ... [Previous functions]

def is_blacklisted(domain):
    """Check if the domain is blacklisted."""
    try:
        response = requests.get(BLACKLIST_URL + domain, timeout=REQUEST_TIMEOUT, headers={'User-Agent': USER_AGENT})
        if 'blacklisted' in response.text:
            return True
    except:
        pass
    return False

def has_redirects(domain):
    """Check if the domain redirects to another URL."""
    try:
        response = requests.get(f'http://{domain}', timeout=REQUEST_TIMEOUT, headers={'User-Agent': USER_AGENT}, allow_redirects=False)
        return 300 <= response.status_code < 400
    except:
        pass
    return False

def check_domain(phishing_domain):
    # ... [Previous checks]
    
    if is_blacklisted(phishing_domain):
        print(f'{phishing_domain} is blacklisted.')
        logging.info(f'{phishing_domain} is blacklisted.')
    
    if has_redirects(phishing_domain):
        print(f'{phishing_domain} has redirects.')
        logging.info(f'{phishing_domain} has redirects.')

if __name__ == '__main__':
    setup_logging()
    
    mode = input('Enter 1 for default mode or 2 for interactive mode: ')
    
    if mode == '2':
        domain = input('Enter the domain to check: ')
    else:
        domain = 'example.com'
    
    phishing_domains = generate_phishing_domains(domain) + enhanced_domain_generation(domain)
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(check_domain, phishing_domains)
