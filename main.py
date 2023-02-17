######################### script to automate opening website on chrome #####################################
####### extract data from website onto csv ##################
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"

##path containing chrome driver
path = "/Users/awadsharif/Downloads/chromedriver_mac64/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

##xpath containing subtitle and text of each card on website
#//div[@class="teaser__copy-container"]
#find by xpath

##NOTE: using find_element returns first element of website. find_elements finds more than 1 match

#returns a list of title/subtitles corresponding to each div named "teaser__copy-container"
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

##build a dataframe using these empty lists
titles = []
subtitles = []
links = []
#use for loop to loop through every copy_container containing subtitle and text
#container div contains the div for subtitle and text!
#use find_element since looping through each element!
for container in containers:

    #title (.text ONLY gets text of element)
    title = container.find_element(by="xpath", value='./a/h3').text

    #subtitle (.text ONLY gets text of element)
    subtitle = container.find_element(by="xpath", value='./a/p').text

    #get the link (ONLY from href!)
    link = container.find_element(by="xpath", value='./a').get_attribute("href")

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)
# #return title and subtitle separately
# title = driver.find_elements(by='xpath', value='div[@class="teaser__copy-container"]/a/h3')
#
# subtitle = driver.find_elements(by='xpath', value='div[@class="teaser__copy-container"]/a/p')
my_dict = {'titles': titles, 'subtitles': subtitles, "links": links}
df_headlines = pd.DataFrame(my_dict)

##export to csv file
df_headlines.to_csv('headline.csv')

##close the driver after exporting csv
driver.quit()