from selenium import webdriver
import csv
import time

driver = webdriver.Chrome()
driver.get('https://www.pro-football-reference.com/years/2022/draft.htm')
div = driver.find_element("id", "div_drafts")
body = div.find_element("tag name", "tbody")
rows = body.find_elements("tag name", "tr")

t0 = time.time()
with open("name_link.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Link to College Stats"])
    for row in rows:
        data = row.find_elements("tag name", "td")
        if len(data):
            if len(data[27].find_elements("tag name", "a")):
                #print(data[2].text, data[27].find_element("tag name", "a").get_attribute("href"))
                writer.writerow([data[2].text, data[27].find_element("tag name", "a").get_attribute("href")])
            else:
                #print(data[2].text, "NO COLLEGE STATS")
                writer.writerow([data[2].text, "NO COLLEGE STATS"])
