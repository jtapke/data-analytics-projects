from scraper import ApartmentScraper
from dbops import DatabaseOperations        

def main():
    url = "https://sightmap.com/embed/apt_building"
    scraper = ApartmentScraper(url)
    db = DatabaseOperations()
    
    scraper.scrape() # Collect data

    # Check and save only changed apartments
    for apartment in scraper.data:
        db.save_apartments(apartment)
    
    db.close()
    scraper.close()
    
if __name__ == "__main__":
    main()
