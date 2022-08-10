import requests
import bs4 as bs4
import urllib3

import selenium.webdriver as webdriver


def search ( userQuery ):
    
    url = "https://www.google.com"
    
    driver = "C:\Windows\WinSxS\x86_netfx4-browser_files_b03f5f7f11d50a3a_4.0.15805.0_none_04f1e78822144171"
    
    browser = webdriver.Firefox()
    
    browser.get(url)

    searchBox = browser.find_element_by_id("query")
    searchBox.send_keys(userQuery)

    searchBox.submit()
    
    links = browser.find_elements_by_xpath( "//ol[@class='web_regular_results']//h3//a")
    
    results = []
    
    for link in links:
        href = link.get_attribute("href")
        results.append(href)
        
    browser.close()
        
    return results


