import requests
import pandas as pd


api_key3 = "d2857cdebe656538ba033c0ef8dad269"
api_key4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkMjg1N2NkZWJlNjU2NTM4YmEwMzNjMGVmOGRhZDI2OSIsInN1YiI6IjVmMjIyMzkzZGY4NTdjMDAzN2Q0YWY0NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.tLxbOPSn6RgNco4voWdQCb_YIO-_8WhjlCJMA5vJafA"


movie_id = 500
apiVer = 3
api_base_url = f'https://api.themoviedb.org/{apiVer}'
end_path = f"/search/movie"
search_query  = 'The Matrix'
final_url =f'{api_base_url}{end_path}?api_key={api_key3}&query={search_query}'
#print(final_url)

# todo: authourization

r = requests.get(final_url)
if r.status_code in range(200,299):
    data = r.json()
    results = data['results']
    if len(results) > 0 :
        movie_ids = set()
        for result in results:
            _id = result['id']
            movie_ids.add(_id)
    #print(list(movie_ids))

output = "search_results.csv"

movie_data = []
for movie_id in movie_ids:
    apiVer = 3
    api_base_url = api_base_url = f'https://api.themoviedb.org/{apiVer}'
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key3}"
    r = requests.get(endpoint)
    if r.status_code in range(200,299):
        data = r.json()
        movie_data.append(data)
        
# saving results

df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index = False)

