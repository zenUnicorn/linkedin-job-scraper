#import the libraries
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events
from linkedin_jobs_scraper.events import EventData
from linkedin_jobs_scraper.query import Query
from linkedin_jobs_scraper.query import QueryOptions
from linkedin_jobs_scraper.query import QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters
from linkedin_jobs_scraper.filters import TimeFilters
from linkedin_jobs_scraper.filters import TypeFilters
from linkedin_jobs_scraper.filters import ExperienceLevelFilters
from linkedin_jobs_scraper.filters import RemoteFilters
import logging

#Changing your root logger level
logging.basicConfig(level = logging.INFO)


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

# Let's create the functions that grabs the data from the LinkedIn job page.
def scdata(info: EventInfo):
  print('[SCDATA]', info.title, info.link, info.company, info.company_link, info.company_img_link, info.description 
   info.date, info.place)

def err(error):
  print('[ERR]', error)

def end():
  print('[END]')
  
  
 
#The Event listeners should be added.
data_scraper.on(Events.DATA, scdata)
data_scraper.on(Events.ERROR, err)
data_scraper.on(Events.END, end)



variables = [
  Query(
    options = QueryOptions(
      #blocks requests for sources like images and stylesheet
      optimize = True, 
      #this limits the number of jobs to scrape
      limit = 10 
    )
  ),
  Query(
    query = 'Designer',
    options = QueryOptions(
      optimize = False,
      apply_link = True,
      locations = ["United Kingdom"],
      limit = 10,
      filters = QueryFilters(
        company_jobs_url='https://www.linkedin.com/jobs/search?keywords=Designers&location=United%20Kingdom&0=&position=1&pageNum=0',
        relevance = RelevanceFilters.RELEVANT,
        time = TimeFilters.ANY,
        type = [
          TypeFilters.FULL_TIME,
          TypeFilters.ASSOCIATE,
          TypeFilters.DIRECTOR
        ],
        experience=[
          ExperienceLevelFilters.ASSOCIATE, 
          ExperienceLevelFilters.MID_SENIOR
        ]
      )
    )
  ),
]

#run the linkedIn Scrapper
data_scraper.run(variables)

