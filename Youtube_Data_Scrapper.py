from selenium import webdriver
from bs4 import BeautifulSoup


urls = [
    'krishnaik06'
]
def main():
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com/user/{}/videos?view=0&sort=dd&flow=grid'.format(urls[0]))
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    yt_name = soup.find('yt-formatted-string',class_="style-scope ytd-channel-name")
    titles = soup.find_all('a',id='video-title')
    video_urls = soup.find_all('a',id='video-title')
    views = soup.find_all('span', class_="style-scope ytd-grid-video-renderer")
    #likes = soup.find_all('a', class_="yt-simple-endpoint style-scope ytd-toggle-button-renderer").format(video_urls[0])
    print('Channel : {}'.format(urls[0]))
    i = 0
    j = 0
    for title in titles[:10]:
        print('\n{}\t{}\t{}\t{}\thttps://www.youtube.com{}'.format(yt_name.text, title.text, views[i].text, views[i+1].text, video_urls[j].get('href')))
        i+=2
        j+=1
main()

