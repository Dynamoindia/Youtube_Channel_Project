from selenium import webdriver
from bs4 import BeautifulSoup
import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user = "root" , passwd = "Shivank@1234")
cursor = mydb.cursor()
#cursor.execute("create if not exist database Youtube_Scrapper")
#Youtube_table = "create table if not exist Youtube_scrapper.youtube_data(Youtuber_Name varchar(255), Titles varchar(255),Views varchar(100),Views varchar(100),Video_Url varchar(255))"


urls = [
    input("Please Enter Channel Name: ")
]
def main():
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com/user/{}/videos?view=0&sort=dd&flow=grid'.format(urls[0]))
    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, 'lxml')
    Youtuber_Name = soup.find('yt-formatted-string',class_="style-scope ytd-channel-name")
    Titles = soup.find_all('a',id='video-title')
    Video_Url = soup.find_all('a',id='video-title')
    Views = soup.find_all('span', class_="style-scope ytd-grid-video-renderer")
    PostDate = soup.find_all('span', class_="style-scope ytd-grid-video-renderer")
    print('Channel : {}'.format(urls[0]))
    i = 0
    j = 0
    for title in Titles[:10]:
        sql= "INSERT INTO Youtube_scrapper.youtube_data (Youtuber_Name, Titles, Views, PostDate, Video_Url) Values (Youtuber_Name, Titles, Views[i], PostDate[i+1], Video_Url[j].get('href'))"
    i+=2
    j+=1

main()



