from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url = "https://github.com/topics/"
git_base_url="https://github.com"


response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')
topic_class = 'f3 lh-condensed mb-0 mt-1 Link--primary'
topic_details = soup.find_all('p',topic_class)


url_class = 'no-underline flex-1 d-flex flex-column'
url_details = soup.find_all('a',url_class)

topic_names=[]
for topic_tag in topic_details:
    topic_names.append(topic_tag.contents[0])
    
topic_urls = []
for url in url_details:
    topic_urls.append(git_base_url+url.get("href"))
    

# # topic_urls
# print(topic_names)
# print(topic_urls)


topic_dict = {"topic_name":topic_names,
              "topic_urls":topic_urls}

topic_df =pd.DataFrame(topic_dict)

topic_df.to_csv("topic_details1.csv",index=False)

