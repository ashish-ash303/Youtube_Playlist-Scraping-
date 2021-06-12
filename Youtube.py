from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
# options.headless = True
driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=options)
driver.get('https://www.youtube.com/c/AbhishekUpmanyuu/videos')


videos = driver.find_elements_by_class_name(
    'style-scope ytd-grid-video-renderer')

video_list = []
for video in videos:

    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = video.find_element_by_xpath(
        './/*[@id="metadata-line"]/span[1]').text
    dys = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    vid_items = {
        "title": title,
        "views": views,
        "dy": dys
    }
    video_list.append(vid_items)

df = pd.DataFrame(video_list)
print(df)
df.to_csv('youtube.csv')
