import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv('dataset.csv')
df = df[df['Type'].isin(['TV', 'Movie'])]
df.reset_index(drop=True, inplace=True)
df.rename(columns={ 'anime_id': 'id', 'Name': 'title', 'Genres': 'genre', 'Synopsis': 'overview', 'Image URL': 'img_url'}, inplace=True)
anime = df[['title', 'genre', 'overview', 'img_url']].copy()
anime['tags'] = anime['overview'] + anime['genre']  
anime = anime.drop(columns=['overview', 'genre'])
cv=CountVectorizer(max_features=11978, stop_words='english')
vector=cv.fit_transform(anime['tags'].values.astype('U')).toarray()
similarity=cosine_similarity(vector)
pickle.dump(anime, open('anime_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))
pickle.load(open('anime_list.pkl', 'rb'))
