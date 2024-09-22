import requests
import tkinter as tk
from tkinter import messagebox

# API key to grant authorization
API_KEY = "8d164d079e494106b1586dd079f13bde"

# Base URL for the complex search endpoint
BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"

# Function to search recipes using the Spoonacular API
def search_recipes(query):
    params = {
        "query": query,       # Search term
        "number": 5,          # Number of results to return
        "apiKey": API_KEY     # Spoonacular API key
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", f"Failed to connect. Status code: {response.status_code}")
        return None

# Function to handle the search button click
def on_search_click():
    query = search_entry.get()  # Get search term from entry box
    if query:
        results = search_recipes(query)
        if results:
            display_results(results)
        else:
            result_box.delete(1.0, tk.END)  # Clear the result box if no results
            result_box.insert(tk.END, "No results found.")
    else:
        messagebox.showwarning("Input Error", "Please enter a search term.")

# Function to display the search results in the text box
def display_results(results):
    result_box.delete(1.0, tk.END)  # Clear previous results
    recipes = results.get('results', [])
    
    if recipes:
        for recipe in recipes:
            result_box.insert(tk.END, f"- {recipe['title']}\n")
    else:
        result_box.insert(tk.END, "No recipes found.")

# Create the main application window
root = tk.Tk()
root.title("Recipe Search")

# Set the window size
root.geometry("400x400")

# Create and place the label, entry box, and search button
search_label = tk.Label(root, text="Enter a recipe search term:")
search_label.pack(pady=10)

search_entry = tk.Entry(root, width=40)
search_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=on_search_click)
search_button.pack(pady=10)

# Create a text box to display the results
result_box = tk.Text(root, height=10, width=50)
result_box.pack(pady=20)

# Start the GUI event loop
root.mainloop()
