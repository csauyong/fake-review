from bs4 import BeautifulSoup
import requests
import csv
import time
import random

movie_id_list = [24733428] 
grade_list = ['h', 'm', 'l']
pages_no = 10 #10
items_per_page = 20 #20

gradeDic = {
    "力荐":5,
    "推荐":4,
    "还行":3,
    "较差":2,
    "很差":1
}

csv_header = ['movie_name', 'id', 'short_comment', 'score', 'comment_time', 'votes']

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
for movie_id in movie_id_list:
    url = 'https://movie.douban.com/subject/{}/comments?status=P'.format(movie_id)
    request = requests.get(url=url, headers=header)
    besoup = BeautifulSoup(request.text, features="lxml")
    movie_name = besoup.select('h1')[0].text.split()[0]
    csv_file_name = movie_name+"_comment.csv"
    print(movie_name)
    time.sleep(random.randint(3,5))
    with open(csv_file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(csv_header)
        for grade in grade_list:
            for i in range(pages_no):
                start = i * items_per_page
                url = 'https://movie.douban.com/subject/{}/comments?percent_type={}&start={}&limit=20&status=P&sort=new_score'.format(movie_id, grade, start)
                request = requests.get(url=url, headers=header)
                besoup = BeautifulSoup(request.text, features="lxml")
                all_short_comment = besoup.select('span[class=short]')
                all_info = besoup.select('span[class=comment-info]')
                all_votes = besoup.select('span[class=comment-vote]')
                for j, (short_comment, info, votes_) in enumerate(zip(all_short_comment, all_info, all_votes)):
                    short_comment_ = short_comment.text.replace('\n','')
                    score = gradeDic[info.select('span[title]')[0].get('title')]
                    comment_time = info.select('span[title]')[1].get('title')
                    votes_ = [int(i) for i in votes_.text.split() if i.isdigit()][0]
                    id =  info.select('a')[0].text
                    print(movie_name, id, short_comment_, score, comment_time, votes_)
                    writer.writerow([movie_name, id, short_comment_, score, comment_time, votes_])
                time.sleep(random.randint(3,5))
        
        
