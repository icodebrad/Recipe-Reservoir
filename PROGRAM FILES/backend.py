import requests

API_KEY = "8d164d079e494106b1586dd079f13bde"

# Base URL for the complex search endpoint
BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"

def search_recipes(query):
    # Define query parameters
    params = {
        "query": query,       # Search term
        "number": 5,          # Number of results to return
        "apiKey": API_KEY     # Your Spoonacular API key
    }
    
    # Make the GET request to the Spoonacular API
    response = requests.get(BASE_URL, params=params)
    
    # Check if the connection was successful
    if response.status_code == 200:
        print("Connection successful!")
        # Convert the response to JSON and return the results
        return response.json()
    else:
        print(f"Failed to connect. Status code: {response.status_code}")
        return None

# Example test to search for recipes with the word "pasta"
if __name__ == "__main__":
    search_term = "pasta"
    results = search_recipes(search_term)
    
    if results:
        print(f"Found {len(results['results'])} recipes for '{search_term}':")
        for recipe in results['results']:
            print(f" - {recipe['title']}")
    else:
        print("No results found.")



'''
from flask import Flask, render_template, request
from urllib.parse import unquote

#Creating the app
app = Flask(__name__)

API_KEY = '8d164d079e494106b1586dd079f13bde'

# Define the route for the "Home" button
@app.route('/home', methods=['GET'])
def home():
    #Render the main page with empty recipe list and search query
    return render_template('index.html', recipes=[], search_query='')

#Define the main route for the app
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #If a form is submitted
        query = request.form.get('search_query', '')
        #Perform a search for recipes with the given query
        recipes = search_recipes(query)
        #Render the main page with the search results and the search query
        return render_template('index.html', recipes=recipes, search_query=query)
    
	#If it is a GET request or no form submitted
    search_query = request.args.get('search_query', '')
    decoded_search_query = unquote(search_query)
    #Perform a search for recipes with the decoded search query
    recipes = search_recipes(decoded_search_query)
    #Render the main page
    return render_template('index.html', recipes=recipes, search_query=decoded_search_query)

#Function to search for recipes based on the provided query
def search_recipes(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': 10,
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
	}

'''