# CV.ee Scraper
This little bot gathers available job positions for IT from cv.ee and serves them on a Flask webserver. A bot made for running on a Raspberry Pi.
## Setup
### Prerequisites
Have the Flask framework and BeautifulSoup4 installed (```$ pip3 install flask``` and ```$ pip3 install beautifulsoup4``` ).

### Starting up
Run ```$ python3 setup.py```.
This creates a Sqlite database with a table to store scraped data, and then runs ```scraper.py``` to collect the first batch of data.

Now the webserver is ready to be run: ```$ python3 webpage.py```

The site is viewable from ```http://localhost:5550```. If the ```port 5550``` is open, it will also be publicly available.

### Setting up a cron job
To make it scrape automatically, a cron job could be set up. 

Running ```$ crontab -e``` and adding the following line to the editor:

```@hourly python3 /your/path/to/cv.ee-scraper/scraper.py```

makes the scraping script run every hour.

--------------
--------------
--------------

![Preview](https://i.imgur.com/bXIl8D4.png)
