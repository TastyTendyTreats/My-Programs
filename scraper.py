from fileinput import filename
from os import link
from turtle import clear
import requests
#http://web.mta.info/developers/turnstile.html
url = "http://web.mta.info/developers/turnstile.html"
base_download_url = "http://web.mta.info/developers/"
list_of_links = []
def main():
    
    #get the web page
    web_page= requests.get(url)
    
    #find the location in the page where the links are
    #find the opening tag
    opening_tag_location = web_page.text.find('<div class="span-84 last">')
    #find the closing tag
    closing_tag_location = web_page.text.find('</div', opening_tag_location)
    link_container = web_page.text[opening_tag_location:closing_tag_location]
    
    #extract the links to the turnstile text files
    more_links = True
    end_of_link = -1
    while more_links:
        #find the href tags
        href_tag_location = link_container.find('href="', end_of_link + 1)
        if href_tag_location == -1:
            break

        #find the end of the link 
        end_of_link = link_container.find('"', href_tag_location + 6)
        file_link = link_container[href_tag_location + 6:end_of_link]
        #append the file link to the list
        list_of_links.append(file_link)
    counter = 0
    #get the text files the links point to
    for link in list_of_links:
        file_path_items = link.split("/")
        file_name = file_path_items[-1]
        print(f"Downloading...{file_name}")

        #request the file
        file_data = requests.get(base_download_url + link)
        counter += 1 
        if counter >= 10:
            downloaded_file = open("testfolder/" + file_name, "w")
            downloaded_file.write(file_data.text)
main()

