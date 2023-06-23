# This project will take you through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).

# You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)

# To avoid problems with rate limits and site accessibility, we have provided a cache file with results for all the queries you need to make to both OMDB and TasteDive. Just use requests_with_caching.get() rather than requests.get(). If you’re having trouble, you may not be formatting your queries properly, or you may not be asking for data that exists in our cache. We will try to provide as much information as we can to help guide you to form queries for which data exists in the cache.

# Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.

# Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

# Try invoking your function with the input “Black Panther”.

# HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache. If any other parameters are included, then the function will not be able to recognize the data that you’re attempting to pull from the cache. Remember, you will not need an api key in order to complete the project, because all data will be found in the cache.

# The cache includes data for the following queries:

# q
# type
# limit
# Black Panther
# <omitted>
# <omitted>
# Black Panther
# <omitted>
# 5
# Black Panther
# movies
# <omitted>
# Black Panther
# movies
# 5
# Tony Bennett
# <omitted>
# 5
# Tony Bennett
# movies
# 5
# Captain Marvel
# movies
# 5
# Bridesmaids
# movies
# 5
# Sherlock Holmes
# movies
# 5


import requests_with_caching
import json

def get_movies_from_tastedive(title):
    endpoint = 'https://tastedive.com/api/similar'
    param = {}
    param['q'] = title
    param['limit'] = 5
    param['type'] = 'movies'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)

def extract_movie_titles(dic):
    list = []
    for i in dic['Similar']['Results']:
        list.append(i['Name'])
    return(list)

def get_related_titles(titles_list):
    list = []
    for i in titles_list:
        new_list = extract_movie_titles(get_movies_from_tastedive(i))
        for i in new_list:
            if i not in list:
                list.append(i)
    print(list)
    return list

def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))

def get_movie_rating(data):
    rating = 0
    for i in data['Ratings']:
        if i['Source'] == 'Rotten Tomatoes':
            rating = int(i['Value'][:-1])
            #print(rating)
    return rating 

def get_sorted_recommendations(list):
    new_list = get_related_titles(list)
    new_dict = {}
    for i in new_list:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    #print(sorted(new_dict, reverse=True))
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]

