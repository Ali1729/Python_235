from topic_scraping import *
new_topic_urls=["https://github.com/topics/python11","https://github.com/topics/python-data-analysis"]
new_topic_names = ["python","python-data-analysis"]

for topic_url,topic_name in zip(new_topic_urls,new_topic_names):
    try:
        assert copy_topic_to_csv(topic_url,topic_name)
    except Exception as e:
        print("Exception occured")