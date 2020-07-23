from bs4 import BeautifulSoup
import requests
import csv
import time

start_time = time.time()

# start of the 1st-link code
source = requests.get('https://reelgood.com/movies/source/crackle')
source.encoding = 'utf-8'
soup = BeautifulSoup(source.text, 'lxml')
table = soup.find('table', class_='css-1179hly')

# making and writing on a csv file
file = open('p3_scrape.csv', 'w')
writer = csv.writer(file)
# csv headings
heading = ['Title', 'Year', 'Rating', 'IMBd', 'Genre', 'Director', 'Disney+', 'HBO', 'HBO MAX', 'Hulu', 'Netflix',
           'Prime Video', 'Sony Crackle']
writer.writerow(heading)

# loop through each row which represents the movie information (on 1st link)
for row in table.find_all('tr', {'class': 'css-o6sgwe'}):

    link_to_movie = row.find('meta', itemprop='url')['content']
    title_ = row.find('td', class_='css-1u7zfla e126mwsw1').text

    year = row.find('td', class_='css-1u11l3y')
    rating = year.find_next_sibling('td', class_='css-1u11l3y')
    year = year.text
    rating = rating.text

    imbd = row.find('b', class_='css-1px39yc').text + "/10"

    # start of the second-link code
    sp_source = requests.get(link_to_movie)
    sp_source.encoding = 'utf-8'
    sp_soup = BeautifulSoup(sp_source.text, 'lxml')

    # everything we need from second-link code
    sp_schema = sp_soup.find('div', itemtype='//schema.org/Movie')

    # everything we need except info on director, actors, etc
    sp_center_area = sp_schema.find('div', class_='css-1jw3688 e14injhv6')

    # genre, tags, etc (top of center) area
    sp_top_details = sp_center_area.find('div', class_='css-1ss0qk ey4ir3j0')
    sp_genre = sp_top_details.find('a', class_='css-jmgx9u').text

    # platforms area (bottom of center) area
    sp_platforms = sp_center_area.find('nav', class_='css-1j9eqcs e1udhou15')

    # info on director, actors, etc
    sp_lower_area = sp_schema.find('div', class_='css-9gv43x e1yfir8f4')

    # director
    sp_director = sp_lower_area.find('a', class_='css-1mnyxfs egg5eqo1').h3.text

    # strings representing platforms
    disney_p = hbo = hbo_m = hulu = netflix = prime = crackle = None
    platforms = ["Disney+", "HBO", "HBO MAX", "Hulu", "Netflix", "Prime Video", "Sony Crackle"]

    # What the platforms the first movie has
    # HBO MAX
    # Prime Video
    # CBS All Access
    # Sony Crackle
    # Rent
    # Buy

    # section in the website's code where all their platforms have the same class name
    for section in sp_platforms.find_all('span', {'class': 'css-3g9tm3 e1udhou113'}):
        if section.text == "Rent" or section.text == "Buy":
            break
        # print(section.text)
        for x in platforms:
            if section.text in platforms[0]:
                disney_p = section.text

            if section.text in platforms[1]:
                hbo = section.text

            if section.text in platforms[2]:
                hbo_m = section.text

            if section.text in platforms[3]:
                hulu = section.text

            if section.text in platforms[4]:
                netflix = section.text

            if section.text in platforms[5]:
                prime = section.text

            if section.text in platforms[6]:
                crackle = section.text

    writer.writerow(
        [title_, year, rating, imbd, sp_genre, sp_director, disney_p, hbo, hbo_m, hulu, netflix, prime, crackle])

file.close()

print("time elapsed: {:.2f}s".format(time.time() - start_time))
