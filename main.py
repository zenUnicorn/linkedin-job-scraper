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


#add event listeners
data_scraper.on(Events.DATA, scdata)
data_scraper.on(Events.ERROR, err)
data_scraper.on(Events.END, end)



queries = [
  Query(
    options = QueryOptions(
      optimize = True, #blocks requests for sources like images and stylesheet
      limit = 27 #this limits the number of jobs to scrape
    )
  ),
  Query(
    query = 'Designer',
    options = QueryOptions(
      locations = ["United Kingdom"],
      optimize = False,
      apply_link = True, #try to extract apply link
      limit = 5,
      filters = QueryFilters(
        company_jobs_url='https://www.linkedin.com/jobs/search?keywords=Designers&location=United%20Kingdom&0=&position=1&pageNum=0',
        relevance = RelevanceFilters.RECENT,
        time = TimeFilters.MONTH,
        type = [TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
        expereice = None,
      )
    )
  ),
]





