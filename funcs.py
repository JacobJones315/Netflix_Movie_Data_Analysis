import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

netflix_df= pd.read_csv('netflixdata.csv')

#removing all TV Show from df leaving only movies
netflix_subset = netflix_df[netflix_df['type'] != 'TV Show']

#selecting only certain columns to make a new movie df
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

#looking at movies < 60 min
short_movies = netflix_movies[netflix_movies['duration'] < 60]

Popular_genres = netflix_movies[(netflix_movies['genre'] == 'Children') | (netflix_movies['genre'] == 'Stand-Up') | \
 (netflix_movies['genre'] == 'Documentaries') | (netflix_movies['genre'] == 'Action') | (netflix_movies['genre'] == 'Comedies') | (netflix_movies['genre'] == 'Dramas') ]

long_movies= netflix_movies[netflix_movies['duration'] > 60]

netflix_streaming = netflix_movies[netflix_movies['release_year'] >= 2007]

# Initialize a list to store colors
colors = []

# Iterate through rows and assign colors based on genre
for index, row in netflix_movies.iterrows():
    genre = row['genre']
    if genre == 'Children':
        colors.append('blue')
    elif genre == 'Documentaries':
        colors.append('green')
    elif genre == 'Stand-Up':
        colors.append('red')
    else:
        colors.append('gray')  

    

##
fig, ax = plt.subplots(dpi = 100)
ax.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)
plt.xlabel('Release year')
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release (Genres)")



Duration_by_year= netflix_movies.groupby('release_year')['duration'].agg(['mean', 'std']).reset_index()

##
fig_zx = plt.figure(dpi= 100)
zx =sns.lineplot(data = netflix_movies, x = 'release_year', y ='duration', ci =95, color = 'blue', label ='Mean')

zx.set_xlabel('Release year')
zx.set_ylabel("Duration (min)")
zx.set_title("Movie Duration by Year of Release")
legend_labels = ['Mean', '95% Confidence Interval']
zx.legend(legend_labels)

##
fig_ab = plt.figure(dpi= 100)
ab =sns.lineplot(data = netflix_streaming, x = 'release_year', y ='duration', ci = 95, color = 'red', label ='Mean')

ab.set_xlabel('Release year')
ab.set_ylabel("Duration (min)")
ab.set_title("Netflix Movie Duration Since Online Streaming Post 2007")
legend_labels = ['Mean', '95% Confidence Interval']
ab.legend(legend_labels)

##
plt.figure(dpi= 100)
plt.hist(netflix_streaming['duration'], bins = 17, edgecolor = 'black', color ='skyblue', range=(40,200))

plt.xlabel('Duration (min)')
plt.ylabel("Number of Movies")
plt.title("Netflix Movie Lengths Since Introduction of Online Streaming")

##
colors2 = {'Documentaries': 'red', 'Stand-Up': 'blue', 'Children': 'green', 'Comedies':'Black', 'Action':'orange', 'Dramas' : 'pink'}

fig_ac = plt.figure(dpi= 100)
ac=sns.scatterplot(x='release_year', y='duration', hue='genre', palette=colors2, data=Popular_genres)


ac.set_xlabel('Release year')
ac.set_ylabel('Duration (min)')
ac.set_title('Popular Movie Genre Durations ')

# legend
plt.legend(title='Genres', loc = 'upper left')
plt.tight_layout()

