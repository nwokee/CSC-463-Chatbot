#               AI Assistance 
# --------------------------------------------------- 
# The project team used Claude Sonnet 4.5 as a
# a coding assistant for this scraper, specifically 
# with html handling and implementing the correct 
# libraries. The project team then modified, tested, 
# and debugged the script to ensure it correctly 
# retrieves and structures verse metadata 
# from OpenBible.info for use in the knowledge base.

import requests
from bs4 import BeautifulSoup # type: ignore
import csv
import time
import re
from urllib.parse import urljoin, quote


class OpenBibleScraper:

    def __init__(self, base_url='https://www.openbible.info/topics/', delay=2):
        # base initializations
        self.base_url = base_url
        self.delay = delay
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.topic_keywords = {}

    def get_keywords(self, csv_filename):
        # goes into topic keyword csv and stores the trigger words for each topic
        try:
            with open(csv_filename, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) >= 2:
                        topic = row[0].strip()
                        keywords = row[1].strip()
                        self.topic_keywords[topic] = keywords
            print(f"Loaded {len(self.topic_keywords)} topics with keywords")
            return True
        except Exception as e:
            print(f"Error loading topic keywords: {e}")
            return False

    def get_topic_url(self, topic):
        # Converts any given topic to the correct url for openbible.info
        topic_standardization = topic.lower().strip().replace(' ', '_')
        return urljoin(self.base_url, topic_standardization)

    def parse_relevance(self, relevance_string):
        
        # set defaults
        result = {
            'translation': 'N/A',
            'votes': 0,
            'raw': relevance_string
        }
        
        if not relevance_string or relevance_string == "N/A":
            return result
        
        # extract translation
        if '/' in relevance_string:
            result['translation'] = relevance_string.split('/')[0].strip()

        # extract vote count 
        vote_match = re.search(r'([\d,]+)\s+helpful votes?', relevance_string)
        if vote_match:
            votes_str = vote_match.group(1).replace(',', '')
            result['votes'] = int(votes_str)
        
        return result
    
    def scrape_verses(self, topic, max_verses=30):
        # scrapes openbible for a given topic, returning a list of dicts with the verse metadata
        url = self.get_topic_url(topic)
        print(f"getting data from: {url}")

        trigger_keywords = self.topic_keywords.get(topic, 'N/A')

        try:
            # sens get request
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            # parse html
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # get all verse entries before parsing
            verses_data = []
            verse_blocks = soup.find_all('div', class_='verse')
            
            print(f"Found {len(verse_blocks)} verse blocks")

            for idx, block in enumerate(verse_blocks):
                if max_verses and idx >= max_verses:
                    break

                # verse reference (John 3:16)
                reference_tag = block.find('a', class_='bibleref')
                reference = reference_tag.get_text(strip=True) if reference_tag else "Unknown"

                # relevance score (upvotes and translation)
                relevance_tag = block.find('span', class_='note')
                relevance = relevance_tag.get_text(strip=True) if relevance_tag else "N/A"
                parsed_relevance = self.parse_relevance(relevance)

                # Extra verse text
                text_tag = block.find('p')
                text = text_tag.get_text(strip=True) if text_tag else ""

                # Bible Gateway Link
                reference_tag = block.find('a', class_='bibleref')
                if reference_tag:
                    reference = reference_tag.get_text(strip=True)
                    verse_url = reference_tag.get('href', url) 
                else:
                    reference = "Unknown"
                    verse_url = url

                if text and reference != "Unknown":
                    verses_data.append({
                        'topic': topic,
                        'trigger_keywords': trigger_keywords,
                        'reference': reference,
                        'text': text,
                        'votes': parsed_relevance['votes'],
                        'translation': parsed_relevance['translation'],
                        'url': verse_url
                    })
                    
            print(f"Successfully scraped {len(verses_data)} verses for topic '{topic}'")
            return verses_data
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return []
        except Exception as e:
            print(f"Error parsing data: {e}")
            return []
                
    def scrape_multiple_topics(self, topics, max_verses_per_topic=30):
        
        all_verses = []

        for idx, topic in enumerate(topics):
            print(f"Scraping topic {idx + 1}/{len(topics)}: {topic}")

            verses = self.scrape_verses(topic, max_verses_per_topic)
            all_verses.extend(verses)

            time.sleep(self.delay)
        
        return all_verses

    def save_to_csv(self, verses_data, filename=None):
        #save scraped data for later

        # verses werent scraped
        if not verses_data:
            print("No data to save")
            return
        
        # filename doesn't exist, make a new one
        if not filename:
            topic = verses_data[0]['topic']
            filename = f"{topic.replace(' ', '_')}_verses.csv"
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        # try to save to csv
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['topic', 'trigger_keywords', 'reference', 'text', 'votes', 'translation', 'url']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(verses_data)
            
            print(f"Data saved to {filename}")
            print(f"Total verses saved: {len(verses_data)}")
            return True
        
        except Exception as e:
            print(f"Error saving to CSV: {e}")
            return False
        
    def get_verse_count(self, topic):
        # get the number of verses available for a topic

        url = self.get_topic_url(topic)


        # same get request as above
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            verse_blocks = soup.find_all('div', class_='verse')
            return len(verse_blocks)
        except:
            return 0



if __name__ == "__main__":
    scraper = OpenBibleScraper(delay=2)
    verse_ct = 30

    scraper.get_keywords('keywords.csv')    
    print(list(scraper.topic_keywords.keys()))
    topics = list(scraper.topic_keywords.keys())
    verses = scraper.scrape_multiple_topics(topics, max_verses_per_topic=verse_ct)
    print(f"Total verses scraped: {len(verses)}")
    scraper.save_to_csv(verses, 'bible_verses_output.csv')