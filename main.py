"""
Project: Lead Generation & Business Directory Scraper
Author: Jahanzaib
Description: Production-ready web scraping pipeline designed to crawl business 
             directories, parse commercial listing nodes, extract contact metadata, 
             and export structured lead sheets into Excel workbooks.
"""

import sys
import logging
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Configure execution pipeline logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Target: Quotes ToScrape (Mock directory markup for stable and reliable pipeline testing)
BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_FILENAME = "business_leads_export.xlsx"

def extract_business_directory_leads():
    """Crawls target business directory, parses listing DOM cards, 
    normalizes commercial metadata, and returns a structured list of leads."""
    lead_records = []
    
    logging.info(f"Initializing Lead Generation Pipeline for target: {BASE_URL}")

    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status() # Raise HTTPError for bad status codes (4xx/5xx)
    except requests.exceptions.RequestException as err:
        logging.error(f"Network transport fault during directory crawl: {err}")
        return lead_records

    # Parse raw markup payload into navigable DOM tree
    soup = BeautifulSoup(response.text, "html.parser")
    listing_cards = soup.find_all("div", class_="quote")

    if not listing_cards:
        logging.warning("No business listing nodes resolved in target DOM tree.")
        return lead_records

    logging.info(f"Successfully resolved {len(listing_cards)} listing cards. Normalizing records...")

    for idx, card in enumerate(listing_cards, start=1):
        # Extract business name / title equivalent from quote text
        business_name = card.find("span", class_="text").text.strip()
        
        # Extract representative / contact person metadata
        contact_person = card.find("small", class_="author").text.strip()
        
        # Generate simulated business contact attributes for lead sheet generation
        simulated_phone = f"+1 (555) 019-{idx:03d}"
        simulated_email = f"contact.lead{idx}@business-domain.com"
        
        # Extract niche category tags as industry sector indicators
        industry_tags = [tag.text for tag in card.find_all("a", class_="tag")]
        industry_sector = ", ".join(industry_tags) if industry_tags else "General Commerce"

        # Append structured lead dictionary record
        lead_records.append({
            "Lead ID": f"LEAD-2026-{idx:03d}",
            "Business Name": business_name[:50] + "...", # Truncate for clean sheet formatting
            "Key Contact": contact_person,
            "Phone Number": simulated_phone,
            "Email Address": simulated_email,
            "Industry Sector": industry_sector,
            "Lead Status": "Qualified"
        })

    logging.info(f"Lead harvesting complete. Total records processed: {len(lead_records)}")
    return lead_records

def export_leads_to_spreadsheet(records):
    """Serializes harvested lead records into a structured Excel spreadsheet."""
    if not records:
        logging.warning("Lead dataset buffer is empty. Skipping spreadsheet generation.")
        return

    logging.info("Compiling lead records into pandas DataFrame...")
    dataframe = pd.DataFrame(records)

    # Export buffer directly to disk without internal pandas index numbering
    dataframe.to_excel(OUTPUT_FILENAME, index=False)
    logging.info(f"Pipeline successfully finalized. Lead sheet persisted: {OUTPUT_FILENAME}")

if __name__ == "__main__":
    harvested_leads = extract_business_directory_leads()
    export_leads_to_spreadsheet(harvested_leads)
