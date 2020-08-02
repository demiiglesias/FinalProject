from tkinter import *
import pandas as pd
from test import *
import nicksCode

# from collaborativeFiltering import *
# movies = pd.read_csv("movies.csv")
# genres = movies['genres']
#
# genres = list(dict.fromkeys(genres))
# print(genres)

root = Tk()
root.title('Movie Recommendation Engine')
root.geometry("700x500")
root.configure(background='black')


def content():
    top = Toplevel()
    top.title('Content Based Filtering')
    top.geometry("700x500")
    m = Label(top, text='Enter a favorite movie: ', font="Verdana 15")
    m.place(x=200, y=100)
    user_fave_movie = Entry(top, width=30)
    user_fave_movie.place(x=200, y=140)
    user_fave_movie.focus()

    def entered():
        m.forget()
        title = Label(top, text='We think you will love these movies too!', font="Verdana 15", border="2")
        title.place(x=200, y=40)
        user_input = user_fave_movie.get()
        recommendations = nicksCode.improved_recommendations(str(user_input))
        recommendations_display = Label(top, text=recommendations)
        recommendations_display.place(x=240, y=140)
        user_fave_movie.destroy()
        enter.destroy()

    enter = Button(top, text='Enter', command=entered)
    enter.place(x=200, y=180)

    top.mainloop()


def collaborative():
    c = Toplevel()
    c.title('Collaborative Based Filtering')
    c.geometry("700x500")

    m = Label(c, text='Pick 3 of your favorite genres ', font="Verdana 15")
    m.place(x=60, y=20)

    rating1 = Spinbox(c, from_=0, to=5, width=3)
    rating1.pack()
    # Genres for check-box
    action = StringVar()
    chk = Checkbutton(c, text="Action", variable=action).place(x=60, y=40)
    children = StringVar()
    chk = Checkbutton(c, text="Children", variable=children).place(x=60, y=380)
    sci_fi = StringVar()
    chk = Checkbutton(c, text="Sci-Fi", variable=sci_fi).place(x=60, y=60)
    adventure = StringVar()
    chk = Checkbutton(c, text="Adventure", variable=adventure).place(x=60, y=80)
    animation = StringVar()
    chk = Checkbutton(c, text="Animation", variable=animation).place(x=60, y=100)
    comedy = StringVar()
    chk = Checkbutton(c, text="Comedy", variable=comedy).place(x=60, y=120)
    thriller = StringVar()
    chk = Checkbutton(c, text="Thriller", variable=thriller).place(x=60, y=140)
    romance = StringVar()
    chk = Checkbutton(c, text="Romance", variable=romance).place(x=60, y=160)
    horror = StringVar()
    chk = Checkbutton(c, text="Horror", variable=horror).place(x=60, y=180)
    drama = StringVar()
    chk = Checkbutton(c, text="Drama", variable=drama).place(x=60, y=200)
    crime = StringVar()
    chk = Checkbutton(c, text="Crime", variable=crime).place(x=60, y=400)
    mystery = StringVar()
    chk = Checkbutton(c, text="Mystery", variable=mystery).place(x=60, y=220)
    fantasy = StringVar()
    chk = Checkbutton(c, text="Fantasy", variable=fantasy).place(x=60, y=240)
    documentary = StringVar()
    chk = Checkbutton(c, text="Documentary", variable=documentary).place(x=60, y=260)
    imax = StringVar()
    chk = Checkbutton(c, text="Imax", variable=imax).place(x=60, y=280)
    war = StringVar()
    chk = Checkbutton(c, text="War", variable=war).place(x=60, y=300)
    musical = StringVar()
    chk = Checkbutton(c, text="Musical", variable=musical).place(x=60, y=320)
    film_noir = StringVar()
    chk = Checkbutton(c, text="Film-Noir", variable=film_noir).place(x=60, y=340)
    western = StringVar()
    chk = Checkbutton(c, text="Western", variable=western).place(x=60, y=360)

    def show():
        my_label = Label(c, text="Genre")
        my_label.pack()

    c.mainloop()


ct_Button = PhotoImage(file='content.png')
co_Button = PhotoImage(file='collab.png')
first_Label = Label(root, text="Welcome to the Movie Recommendation System", font="Verdana 20", fg="white", bg="black")
second_Label = Label(root, text="choose an algorithm for a movie recommendation", font="Verdana 20", fg="white",
                     bg="black")
collaborative_Button = Button(root, image=co_Button, command=collaborative, borderwidth=0, bg="black")
content_Button = Button(root, image=ct_Button, command=content, borderwidth=0)

first_Label.place(x=130, y=70)
second_Label.place(x=120, y=100)
collaborative_Button.place(x=210, y=180)
content_Button.place(x=210, y=270)
root.mainloop()
