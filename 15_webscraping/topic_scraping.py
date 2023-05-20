from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from scraping1 import *

base_url = "https://github.com/topics/"
git_base_url="https://github.com"

def func1(topic_urls):
    for topic_name,topic_url in zip(topic_names,topic_urls):
        print(topic_url)

        response = requests.get(topic_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        username_class = 'f3 color-fg-muted text-normal lh-condensed'
        username_details = soup.find_all('h3',username_class)


        username_names =[]
        for user_detail_tag in username_details:
            username_names.append(user_detail_tag.text.strip().split("\n")[0])



        project_url_class = 'text-bold wb-break-word'
        project_url_details = soup.find_all('a',project_url_class)

        project_urls =[]
        for project_tags in project_url_details:
            project_urls.append(git_base_url+project_tags.get("href"))


        star_class = 'Counter js-social-count'
        star_details = soup.find_all('span',star_class)

        stars =[]
        for i in star_details:
            stars.append(int(re.sub(r'[^0-9]','',i.get("title"))))

        # print(username_names,project_urls,stars)

        project_dict = {"username_names":username_names,
                    "project_urls":project_urls,
                    "stars":stars}

        project_df =pd.DataFrame(project_dict)

        project_df.to_csv(topic_name+".csv",index=False)




func1(topic_urls)