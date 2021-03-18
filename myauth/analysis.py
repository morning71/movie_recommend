import pymysql
import math
from collections import Counter
from pyecharts import *
from pyecharts import base
db = pymysql.connect('localhost','root','morning321','movie')
cursor = db.cursor()
select_sql = 'SELECT movie_type FROM myauth_movie_info;'
cursor.execute(select_sql)
movie_type_list = []
for i in cursor.fetchall():
    for j in i[0].split(','):
        if len(j) >0:
            movie_type_list.append(j)
        else:
            pass
result = Counter(movie_type_list)
result = base.Base.cast(result)
bar = Bar('电影类型统计-柱状图')
bar.add('电影类型：',result[0],result[1],mark_line = ['average'],mark_point=['max','min'])
bar.render()
wordcloud = WordCloud('电影类型-词云图')
wordcloud.add('电影类型-词云',result[0],result[1],word_size_range=[20,100])
select_score = 'SELECT movie_point FROM myauth_movie_info;'
cursor.execute(select_score)
score_list=[]
for i in cursor.fetchall():
    score_list.append(str(round(i[0]))+'分')
score_reslut = Counter(score_list)
score_reslut = base.Base.cast(score_reslut)
pie = Pie('电影分值统计-饼图')
pie.add('电影评分：',score_reslut[0],score_reslut[1],is_random=True,radius=[30,75])
page = Page('电影数据可视化')
page.add(bar)
page.add(wordcloud)
page.add(pie)
page.render('templates/movie/keshihua.html')

