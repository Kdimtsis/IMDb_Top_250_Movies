import requests
from bs4 import BeautifulSoup as bs
import re
from csv import writer


class Imdb():

    """A CLASS THAT GENERATES A CSV FILE WITH DETAILS
       FOR THE TOP 250 MOVIES BY RATING ON IMDb"""

    def __init__(self):
        self.name = "Imdb top 250 movies"


    def page_links(self):

        """FUNCTION THAT GENERATES LINK FOR EACH PAGE"""

        number = 1
        list_links = []

        while number < 251:
            link = f"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start={number}&ref_=adv_nxt"
            list_links.append(link)
            number += 50
        return list_links


    def get_movie_data(self):

        """A FUNCTION THAT SCRAPES ALL MOVIE DATA"""

        page_links = self.page_links()
        movie_details = []

        for url in page_links:

            # Change default language
            headers = {"Accept-Language": "en-US,en;q=0.5"}
            data = requests.get(url, headers=headers)

            soup = bs(data.text, "html.parser")

            # List with all movie boxes in each page
            movies = soup.find_all("div", {"class", "lister-item-content"})


            # Scrape details for every 50 movies on each page
            for movie in movies:

                ranking = movie.find("h3")("span")[0].text.replace(".", "")
                title = movie.find("a").text
                description = movie.find("div", {"class", "ratings-bar"}).find_next("p").text
                year = movie.find("span", {"class", "lister-item-year"}).text.replace("(", "").replace(")", "")

                try:
                    movie_suitability = movie.find("span", {"class", "certificate"}).text
                except:
                    movie_suitability = "Not rated"

                category = movie.find("span", {"class", "genre"}).text
                minutes = movie.find("span", {"class", "runtime"}).text
                rating = movie.strong.extract().text
                votes = movie.find("p", {"class", "sort-num_votes-visible"}).find("span").find_next("span").text
                director = movie.find("p", {"class", "text-muted"}).find_next("p").find_next("p").find("a").text

                find_stars = movie.find("p", {"class", "text-muted"}).find_next("p").find_next("p").text.partition("Stars:")[2].strip()
                stars = [x.strip() for x in find_stars.split(",")]

                gross = movie.find_all("p")[-1].find_all("span")[-1].text

                movie_details.append((ranking,title,description,year,movie_suitability,category,minutes,rating,votes,director,stars,gross))


        return movie_details

    def write_to_csv(self):

        """FUNCTION THAT WRITES ALL DATA TO CSV"""

        details = self.get_movie_data()

        with open("imdb_movies.csv", "w", newline="", encoding="utf-8") as file:
            csv_writer = writer(file)
            csv_writer.writerow(["Ranking","Title","Description","Year","Movie Suitability","Category","Minutes","Rating","Votes","Director","Stars","Gross"])

            for row in details:
                csv_writer.writerow(row)

        return "Csv file is ready"


imdb = Imdb()
print(imdb.write_to_csv())