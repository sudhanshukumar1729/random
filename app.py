from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.themoviedb.org/3/discover/movie"
IMG_PATH = "https://image.tmdb.org/t/p/w1280"
SEARCH_API = "https://api.themoviedb.org/3/search/movie"
API_KEY = "YOUR_API_KEY"  # Replace this with your API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search']
    if search_query:
        resp = requests.get(SEARCH_API, params={'api_key': API_KEY, 'query': search_query})
        data = resp.json()
        movies = data.get('results', [])
    else:
        resp = requests.get(API_URL, params={'api_key': API_KEY, 'sort_by': 'popularity.desc', 'page': 1})
        data = resp.json()
        movies = data.get('results', [])
    return render_template('index.html', movies=movies, img_path=IMG_PATH)

if __name__ == '__main__':
    app.run(debug=True)
