from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Movie List"
sheet.append(['Movie Name','Year '])


try:
    response = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    soup = BeautifulSoup(response.text,'html.parser')
    # print(soup)
    movies = soup.find('tbody',class_='lister-list').find_all("tr")

    for movie in movies:
        # print(movie)
        movie_name = movie.find('td',class_='titleColumn').a.text
        year = movie.find('td', class_='titleColumn').span.text.replace('(',"")
        year = year.replace(')',"")
        # print(movie_name,year)
        sheet.append([movie_name,year])

        # break
except Exception as e:
    print(e)
excel.save("Movies.xlsx")