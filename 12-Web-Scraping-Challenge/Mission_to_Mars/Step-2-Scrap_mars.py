from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    #executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    # Using Temporary Driver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

##### Define Function Scrape #######
def scrape():

    ############# Get Latest headlines from NASA News Page #############
    
    # Initialize Browser
    browser = init_browser()

    # Visit Mars Nasa News Website
    url_news = "https://mars.nasa.gov/news/"
    browser.visit(url_news)

    # HTML object
    html_news = browser.html

    # Parse HTML with Beautiful Soup
    soup_news = bs(html_news, 'html.parser')

    # Find the Frist News Title.
    news_title = soup_news.find_all(['div','a'], class_='content_title')[1].text

    # Find the First Newe Paragraph below the news.    
    news_p = soup_news.find('div', class_='article_teaser_body').text

    # Find Featured image of the article
    relative_img_path = soup_news.find_all('img')[15]["src"]
    img_news = 'https://mars.nasa.gov' + relative_img_path

    # Close the browser after scraping
    browser.quit()


    ############# Get Mars Facts Table using Pandas #############
    
    url_pandas = 'https://space-facts.com/mars/'

    tables_mars = pd.read_html(url_pandas)
    df_mars = tables_mars[0]
    df_mars.columns = ['Description', 'Value']
    df_mars1 = df_mars.set_index('Description')
    
    # Mars Mars facts DataFrame to HTML
    html_mars = df_mars1.to_html()
    html_mrs = html_mars.replace('\n', '')


     
 ############# USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres #############
    
    # Initialize Browser
    browser = init_browser()
    url_hem = [
            'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced',
            'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
            'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced',
            'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
             ]

    # Empty List
    mars_hem = []

    # Loop through the links
    for url in url_hem:
        pic_h = {}

         # Click on the link
        browser.visit(url)

         # Scrape
        html_m = browser.html
        soup_m = bs(html_m, 'html.parser')

         # scrape the title
        title_m = soup_m.find('h2', class_='title').get_text()
    
         # Scrape Image URL
        images_mars = soup_m.find_all('div', class_='downloads')
        
        for image in images_mars:
            image_m = image.find('a')
            img_m = image_m['href']


         # add both Title and Image URL to "pic" dictionary 
        pic_h['title'] = title_m
        pic_h['img_url'] = img_m
         # append to Pic
        mars_hem.append(pic_h)

  
    Hemisphere_image_urls = mars_hem

    # Close the browser after scraping
    browser.quit()


# print(scrape())


 ############ Store data in a dictionary  #########

    mars_data = {
        "news_title" : news_title,
        "news_para" : news_p,
        "max_temp" : img_news,
        "html_mars" : html_mrs,
        "Hemisphere_image_urls" : Hemisphere_image_urls
    }

    #  Return results
    return mars_data