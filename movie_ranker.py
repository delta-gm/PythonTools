import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# everything that currently works in this script is uncommented. 

movies = pd.read_csv('IMDB-Movie-Data.csv')
to_drop = ['Description', 
            'Director']
movies.drop(to_drop, inplace=True, axis=1)

print(movies.index)

movies['AvgRating'] = (movies['Rating'] + movies['Metascore']/10)/2

def customRating(genre,rating):
    if 'Comedy' or 'Action' or 'Animation' or 'Sci-Fi' in genre:
        return min(10, rating+1)
    if 'Romance' or 'Musical' in genre:
        return max(0, rating-8)
    else:
        return rating 


movies['CustomRating'] = movies.apply(lambda x: customRating(x['Genre'], x['Rating']), axis=1)

genreSeries = movies['Genre'].str.split(',').apply(pd.Series, 1).stack()
genreSeries.index = genreSeries.index.droplevel(-1)
indiv_genres = genreSeries.value_counts()
print('Counts per Genre: \n')
print(indiv_genres, '\n')
genremovies = pd.DataFrame(genreSeries)
print(genremovies.index)
print('Movies per Category Combo: \n')
categories = movies['Genre'].str.split(',').value_counts()
print(categories)
print(len(indiv_genres))
print(genreSeries[:5])
print(genremovies[:5])
# movies.drop('Genre', axis=1, inplace=True)
# movies_outer = pd.merge(movies, genremovies, on=index, how='outer')
# print(movies_outer[:5])

def actor_rating(actors, rating):
    if 'Will Smith' in actors:
        return max(10, rating+7)
    else:
        return rating

actorSeries = movies['Actors'].str.split(',').apply(pd.Series, 1).stack()
actorSeries.index = actorSeries.index.droplevel(-1)
moviesByActor = actorSeries.value_counts()
print('Movies by Each Actor: \n')
print(moviesByActor[:20], '\n')

movies['ActorRating'] = movies.apply(lambda x: actor_rating(x['Actors'], x['CustomRating']), axis=1)
# print(movies[:3])

willSmithMovies = movies.sort_values('ActorRating', axis=0, ascending=False)
# # not_df = df[~((df['Rating']>8) | (df['Metascore']>80))]

willSmithMovies.drop('Metascore', axis=1, inplace=True)
print(willSmithMovies[0:15])




# trying to drop all rows that are not animated, and then boxplot the metascore by director
# def cartoon_filter(genre):
#     if 'Animated' not in genre:
#         movies.drop()



# cartoons = movies[~((movies['Genre']!='Comedy') | (movies['Genre']!='Animation'),dtype=object)]
# cartoons.boxplot(column='Metascore', by='Director')
# plt.show()