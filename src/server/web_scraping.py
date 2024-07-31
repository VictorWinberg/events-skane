import requests
from bs4 import BeautifulSoup

# Get the content
r = requests.get(' https://evenemang.malmo.se/')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the information
select_headings = soup.select("#main-content > a > article > div > div.break-word.prose.w-full.break-words > h3")
select_time = soup.select("#main-content > a > article > figure > figcaption > time")
select_place = soup.select("#main-content > a > article > div > div.mt-1\/2-gutter.flex.flex-col-reverse.flex-wrap.gap-1\/2-gutter.lg\:mt-1\/4-gutter.lg\:flex-row-reverse.lg\:items-center.lg\:justify-end > footer > p > span")
time_elements = soup.select("#main-content > a > article > figure > figcaption > time")
datetime_values = [elem.get('datetime') for elem in time_elements]

for index, item in enumerate(select_place, start=0): 
    print(f"Vad: {select_headings[index].get_text().strip()}, När: {datetime_values[0]}, Plats: {select_place[index].getText().strip()}")


# Questions And thoughts.

# Define what information an events needs to have by minimum
# For each "event", add source URL to event. 
# Make a list of objects 
# For each object, perhaps use LLM to categories events? Add additional descriptions? 
# Use LLM to en-rich data? 