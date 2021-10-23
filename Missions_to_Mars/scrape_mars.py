# Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

# Define function to choose the executable path
def init_browser():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless = False)

# Connect to Mars News Site
browser = init_browser()

mars_news_url = "http://redplanetscience.com"
browser.visit(mars_news_url)

# HTML Object
html = browser.html

# Parse HTML with Beautiful Soup
news_soup = bs(html, "html.parser")    

# Retrieve the latest article's title
news_title = news_soup.find("div", class_ = "content_title")
news_title = news_title.text.strip()
print(news_title)

# Retrieve the latest article's paragraph
news_paragraph = news_soup.find("div", class_ = "article_teaser_body")
news_paragraph = news_paragraph.text.strip()
print(news_paragraph)

# Exit Browser
browser.quit()

# Connect to the image URL
browser = init_browser()

mars_featured_image_url = "http://spaceimages-mars.com/"
browser.visit(mars_featured_image_url)

# HTML Object
html = browser.html

# Parse HTML with Beautiful Soup
image_soup = bs(html, "html.parser")

# Assign the full url string to a variable called "featured_image_url"
featured_image = image_soup.find("img", class_ = "headerimage fade-in")
featured_image_url = mars_featured_image_url + featured_image["src"]
print(featured_image_url)

# Exit Browser
browser.quit()