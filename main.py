import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('dataset.csv')
df = df[df['Type'].isin(['TV', 'Movie'])]
df.reset_index(drop=True, inplace=True)

df.rename(columns={
    'anime_id': 'id',
    'Name': 'name',
    'Genres': 'genre',
    'Synopsis': 'overview',
    'Image URL': 'img_url'
    }, inplace=True)
selected_features = ['id','name','genre', 'overview', 'img_url']
anime = df[selected_features]
anime['tags'] = anime['overview']+anime['genre']
anime = anime.drop(columns=['overview', 'genre'])
anime.head()

cv=CountVectorizer(max_features=11978, stop_words='english')
vector=cv.fit_transform(anime['tags'].values.astype('U')).toarray()
similarity=cosine_similarity(vector)
anime[anime['name']=="Trigun"].index[0]

distance = sorted(list(enumerate(similarity[2])), reverse=True, key=lambda vector:vector[1])
for i in distance[0:5]:
    print(anime.iloc[i[0]]['name'])

def recommend(animes):
    index = anime[anime['name']==animes].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    for i in distance[0:5]:
        print(anime.iloc[i[0]]['name'])

pickle.dump(anime, open('anime_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))
pickle.load(open('anime_list.pkl', 'rb'))


