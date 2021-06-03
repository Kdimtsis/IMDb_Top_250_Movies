# Folder preview

## This folder contains:
1) A python script that scrapes data using Beautiful Soup and writes them to a Csv file.    
3) The raw csv file 
4) A jupyter notebook script that cleans the csv using Pandas
5) The clean csv file

Data was collected from: https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc

*Tools that were used: requests, Beautiful Soup, Csv writer, pandas*

## Class Analysis

### 1) Collect movie data

To collect the data for the top 250 movies by user rating i used **Beautiful Soup**. At first generated the urls for all pages. Each page on IMDb returns 50 results. I noticed a pattern in the url of each page. The only thing that was different was the number that indicated the first movie on each page. So in the first page it was 1, in the second page it was 1+50=51 etc. The urls were stored in a list.

![image](https://user-images.githubusercontent.com/72921465/119202280-1df09200-ba99-11eb-8f2d-e7c8121114fa.png)

1) First i located each box movie 

![image](https://user-images.githubusercontent.com/72921465/119202866-62c8f880-ba9a-11eb-943b-c583a81ce2ae.png)

2) For each of the 250 movies i collected the following data:

Ranking, Title, Description, Year, Genre (movie suitability , Category, Duration, Rating, Total Votes, Director, Stars, Gross, Image url

