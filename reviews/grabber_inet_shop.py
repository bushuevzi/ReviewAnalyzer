import os
import glob
import csv
from bs4 import BeautifulSoup
import pandas as pd

# это для записи в csv
with open('test.csv', 'w', encoding="utf-8") as csvFile:
# with open('reviews.csv', 'w', encoding="utf-8") as csvFile:
    writer = csv.writer(csvFile, delimiter=';', lineterminator='\n')
    writer.writerow(["feature", 0])

    # здесь начинаем парсить
    folederName = "./html"
    files = glob.glob(folederName+'/test/*Для теста.html')
    # files = glob.glob(folederName+'/*.html')


    complited = 0
    for fileName in files:
        opinions = []
        
        with open(fileName, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html5lib")
            opinions_html = soup.find('div', {'id': 'scroll-to-reviews-list'})

            for opinion_texts in opinions_html:
                try:
                    opinion = ""
                    # Каждый отзыв состоит из нескольких секций, секция состоит из заголовка и описания
                    opinionSections = opinion_texts.contents[0].contents[2].contents[2]
                    for opinionSection in opinionSections:                            
                        opinion += opinionSection.contents[0].text.replace('\n','') + opinionSection.contents[1].text.replace('\n','') + '. '
                    opinions.append(opinion)
                except:
                    continue
        
        # Закидываем данные в csv
        lable = 1
        if (('Отзывы 1' in fileName) or ('Отзывы 2' in fileName)):
            lable = 0
        for opinion in opinions:
            writer.writerow([opinion, int(lable)])
        complited += 1

        # отображение
        print("Compleated " + str(complited) + ' from ' + str(len(files)))
