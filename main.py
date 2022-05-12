import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters
from linkedin_jobs_scraper.filters import TypeFilters, ExperienceLevelFilters
from linkedin_jobs_scraper.filters import RemoteFilters


logging.basicConfig(level = logging.INFO)


def scdata(data: EventData):
  print('[SCDATA]', data.title, data.company, data.company_link,data.date, 
  data.link, data.insights, len(data.description))

def err(error):
  print('[ERROR]', error)

def end():
  print('[END]')
  
  
  
data_scraper = LinkedinScraper(
  #custom chrome executable path
  chrome_executable_path = None,

  #custom chrome options
  chrome_options = None,

  #overribes headless mode only if chrome_options ia None
  headless = True,

  #how many threads will be spawned to run queries concurrently
  max_workers = 1,
  
  #slow down the scraper to avoid "Too many requests 429" errors
  slow_mo = 1
)


