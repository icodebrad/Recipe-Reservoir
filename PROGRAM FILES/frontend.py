import tkinter as tk 
from tkinter import messagebox
from backend import *
#import sqlite3 - to be used for login registration

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



'''
def submitact():
     
    user = Username.get()
    passw = password.get()
  
    print(f"The name entered by you is {user} {passw}")
  
    logintodb(user, passw)
  
 
def logintodb(user, passw):
     
    # If password is entered by the 
    # user
    if passw:
        db = sqlite3.connect(host ="localhost",
                                     user = user,
                                     password = passw,
                                     db ="College")
        cursor = db.cursor()
         
    # If no password is entered by the
    # user
    else:
        db = sqlite3.connect(host ="localhost",
                                     user = user,
                                     db ="College")
        cursor = db.cursor()
         
    # A Table in the database
    savequery = "select * from STUDENT"
     
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
         
        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        print("Query Executed successfully")
         
    except:
        db.rollback()
        print("Error occurred")
  
 
root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")
  
 
# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)
 
submitbtn = tk.Button(root, text ="Login", 
                      bg ='blue', command = submitact)
submitbtn.place(x = 150, y = 135, width = 55)
 
root.mainloop()
'''
'''
#import haslib
#import backend

root = Tk()
root.title("Login - Recipe Reservoir")
root.geometry("750x750")
#root.configure(background="White")
root.iconbitmap("RR.ico")

def login(user, pwd):
   user_pass_keys = {}
   f = open("credentials.txt", 'r')

   for i, line in enumerate(f):
      line = [x.strip('\n') for x in line.split(", ")]

      for word in line:
         if (user in line[0:1]) and (pwd in line[2:3]):
            print("USER PASSWORD FOUND\n LOGIN SUCCESSFUL")
            user_pass_keys[word].append(str(i+1))
         else:
            print("USER OR PASSWORD NOT FOUND")
            user_pass_keys[word] = [str(i+1)]
   f.close()

def reg_win():
   reg_win = Toplevel(root)
   reg_win.geometry("500x500")
   reg_win.title("Register - Recipe Reservoir")
   reg_win.iconbitmap("RR.ico")

   USER_EXIST = False
            
   reg_welcome_lab = Label(reg_win, text="Register a Recipe Reservoir Account")
   reg_welcome_lab.pack(anchor=N, side=TOP)
   
   reg_lab_user = Label(reg_win, text="Enter username:")
   reg_lab_user.pack(anchor=CENTER)
   new_user = Entry(reg_win)
   new_user.pack(anchor=CENTER)

   reg_lab_pwd = Label(reg_win, text="Enter password:")
   reg_lab_pwd.pack(anchor=CENTER)
   new_pwd = Entry(reg_win, show="*")
   new_pwd.pack(anchor=CENTER)

   conf_lab = Label(reg_win, text="Confirm password:")
   conf_lab.pack(anchor=CENTER)
   conf_pwd = Entry(reg_win, show="*")
   conf_pwd.pack(anchor=CENTER)

   info_lab = Label(reg_win, text=None)

##   while True:
##      print(USER_EXIST)
##      if new_user and new_pwd and conf_pwd:
##         USER_EXIST = True
##         break
##      else:
##         continue

   def register(user, pwd, conf_pwd):
      username = user.get()
      password = pwd.get()
      conf_password = conf_pwd.get()

      while True:
   ##      if not USER_EXIST:
   ##         print("No data found, proceed to Register")
   ##         sleep(.5)
         if password != conf_password:
            print("passwords do not match")
            messagebox.showerror("Passwords do not match.")
         elif password == conf_password:
            while True:
               if len(str(username)) < 3 or len(str(conf_password)) < 3:
                  print("pwd minimum length true")
                  messagebox.showerror("Please enter a minimum of 3 characters for username and password.")
                  break
               else:
                  #enc = conf_pwd.encode()
                  #hash1 = hashlib.md5(enc).hexdigest()
                  with open('credentials.txt', 'w') as f:
                     f.write(username + ", " + conf_password + "\n")
                     #f.write(hash1)
                     f.flush()
                  f.close()
                  print("You have registered successfully!")
                  # Display the submitted information
                  messagebox.showinfo(title=f"Registration Form Successfully Created!\n",
                                      message=f"Welcome to Recipe Reservoir!\nUsername: {username}\nPassword: {conf_password}")
                  break
         else:
            print("User already exists!")
            
   submit_acc = Button(reg_win, text="Register my Account", command=register(new_user, new_pwd, conf_pwd))
   submit_acc.pack(anchor=RIGHT, side=RIGHT)



##def signup():
##
##    reg_sys = Toplevel(root)
##    reg_sys.geometry("500x500")
##    reg_sys.title("User Registration")
##    reg_sys.iconbitmap("RR.ico")
##
##
##    if Conf_pwd == Password:
##        #enc = conf_pwd.encode()
##        #hash1 = hashlib.md5(enc).hexdigest()
##
##        with open('credentials.txt', 'w') as f:
##            f.write(Username + "\n")
##            f.write(Conf_pwd + "\n")
##            #f.write(hash1)
##        f.close()
##        print("You have registered successfully!")
##
##    else:
##        print("Incorrect password!")

'''
#USER REGISTRATION WIDGETS
'''
log_welcome_lab = Label(root, text="Login to your Recipe Reservoir Account")
log_welcome_lab.pack(anchor=N, side=TOP)

log_lab_user = Label(root, text="Enter username:")
log_lab_user.pack(anchor=CENTER)
inp_user = Entry(root)
inp_user.pack(anchor=CENTER)

log_lab_pwd = Label(root, text="Enter password:")
log_lab_pwd.pack(anchor=CENTER)
inp_pwd = Entry(root, show="*")
inp_pwd.pack(anchor=CENTER)

conf_lab = Label(root, text="Confirm password:")
conf_lab.pack(anchor=CENTER)
conf_pwd = Entry(root, show="*")
conf_pwd.pack(anchor=CENTER)

info_lab = Label(root, text=None)

log_submit_form = Button(root, text="Submit", command=login(inp_user, inp_pwd))
log_submit_form.pack(anchor=CENTER, side=TOP)

result_lab = Label(root, text=None)
result_lab.pack(anchor=CENTER)

#REG WIDGETS
reg_button = Button(root, text="Create an Account", command=reg_win)
reg_button.pack(anchor=CENTER, side=BOTTOM)

reg_label = Label(root, text="Don't have an account? Register one here!")
reg_label.pack(anchor=CENTER, side=BOTTOM)




def clearEntry():
    Searchresult.delete(1.0, END)
    RecentResults.delete(1.0, END)

def open_popup():
    top = Toplevel(root)
    top.geometry("220x35")
    top.title("Error message")
    top.iconbitmap("RR.ico")

    Label(top, text="Invalid input. Please enter a valid recipe.").place(x=0,y=0)

def recipeSearch(*args):
    Searchresult.delete(1.0, END)
    recipe = SearchString.get()
    if len(recipe) == 0:
        open_popup()
    else:
        Searchresult.insert(END,recipe+"\n")
        RecentSearches.append(recipe)
        RecentResults.insert(END,recipe+"\n")

def main():
   RecentSearches = []
   recipe_app = Toplevel(root)
   recipe_app.geometry("1920x1080")
   recipe_app.title("Recipe Reservoir")
   recipe_app.iconbitmap("RR.ico")

   #GRAPHICIAL USER INTERFACE

   #entry boxes
   SearchString = StringVar()
   Searchbar = Entry(recipe_app, textvariable = SearchString)
   ##Searchbar.grid(row=1, column=1)
   Searchbar.pack(side=TOP, anchor=N)

   #keybinds
   Searchbar.bind('<Return>', recipeSearch, add = '+')
   #Searchbar.bind('<FocusOut>', recipeSearch, add = '+')

   #text boxes
   Searchresult = Text(recipe_app, height=40, width=40)
   ##Searchresult.grid(row=2, column=10)
   Searchresult.pack(side=BOTTOM, anchor=S)

   RecentResults = Text(recipe_app, height=10, width=20)
   ##RecentResults.grid(row=2, column=1000)
   RecentResults.pack(side=RIGHT, anchor=E)

   #buttons
   searchButton = Button(recipe_app, text= "Search it!", command=recipeSearch)
   searchButton.pack(anchor=N)

   clearSearch = Button(recipe_app, text="Clear Results", command=clearEntry)
   ##clearSearch.grid(row=6, column=10)
   clearSearch.pack(side=RIGHT,anchor=NE)

   #labels
   recipeTitle = Label(recipe_app, bg="#a1c5ff", text="Enter a Recipe to search!")
   recipeTitle.pack(side=TOP, anchor=N)
   ##recipeTitle.pack(side=TOP)

   recipeOut = Label(recipe_app, bg="#a1c5ff", text="Your result:")
   ##recipeOut.grid(row=1, column=10)
   recipeOut.pack(side=BOTTOM, anchor=S)

if __name__ == "__main__":
    main()

root.mainloop

'''
