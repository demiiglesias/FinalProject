from tkinter import *
import pandas as pd
import CollaborativeFiltering2
# genres = movies['genres']
#
# genres = list(dict.fromkeys(genres))
# print(genres)

root = Tk()
root.title('Movie Recommendation Engine')
root.geometry("700x500")

#list of movies from genre
def get_top_2_movies(genre):
    list = ["movie1","movie2"]
    return list

def content():
    top = Toplevel()
    top.title('Content Based Filtering')
    top.geometry("700x500")
    m = Label(top, text='Enter a favorite movie: ', font="Verdana 15")
    user_fave_movie = Entry(top, width=30)
    m.place(x=200, y=100)
    user_fave_movie.place(x=200, y=140)

    def entered():
        my_label = Label(top, text=user_fave_movie.get())
        my_label.pack()

    enter = Button(top, text='Enter', command=entered)
    enter.place(x=200, y=190)

    top.mainloop()


def collaborative():
    count = 0
    c = Toplevel()
    c.title('Collaborative Based Filtering')
    c.geometry("700x500")

    m = Label(c, text='Pick 3 of your favorite genres ', font="Verdana 15")
    m.place(x=60, y=10)

    # Genres for check-box
    action = IntVar()
    chk = Checkbutton(c, text="Action", variable=action).place(x=60, y=40)
    children = IntVar()
    chk = Checkbutton(c, text="Children", variable=children).place(x=60, y=380)
    sci_fi = IntVar()
    chk = Checkbutton(c, text="Sci-Fi", variable=sci_fi).place(x=60, y=60)
    adventure = IntVar()
    chk = Checkbutton(c, text="Adventure", variable=adventure).place(x=60, y=80)
    animation = IntVar()
    chk = Checkbutton(c, text="Animation", variable=animation).place(x=60, y=100)
    comedy = IntVar()
    chk = Checkbutton(c, text="Comedy", variable=comedy).place(x=60, y=120)
    thriller = IntVar()
    chk = Checkbutton(c, text="Thriller", variable=thriller).place(x=60, y=140)
    romance = IntVar()
    chk = Checkbutton(c, text="Romance", variable=romance).place(x=60, y=160)
    horror = IntVar()
    chk = Checkbutton(c, text="Horror", variable=horror).place(x=60, y=180)
    drama = IntVar()
    chk = Checkbutton(c, text="Drama", variable=drama).place(x=60, y=200)
    crime = IntVar()
    chk = Checkbutton(c, text="Crime", variable=crime).place(x=60, y=400)
    mystery = IntVar()
    chk = Checkbutton(c, text="Mystery", variable=mystery).place(x=60, y=220)
    fantasy = IntVar()
    chk = Checkbutton(c, text="Fantasy", variable=fantasy).place(x=60, y=240)
    documentary = IntVar()
    chk = Checkbutton(c, text="Documentary", variable=documentary).place(x=60, y=260)
    imax = IntVar()
    chk = Checkbutton(c, text="Imax", variable=imax).place(x=60, y=280)
    war = IntVar()
    chk = Checkbutton(c, text="War", variable=war).place(x=60, y=300)
    musical = IntVar()
    chk = Checkbutton(c, text="Musical", variable=musical).place(x=60, y=320)
    film_noir = IntVar()
    chk = Checkbutton(c, text="Film-Noir", variable=film_noir).place(x=60, y=340)
    western = IntVar()
    chk = Checkbutton(c, text="Western", variable=western).place(x=60, y=360)

    if action == 1:
        a = 1

    def show():
            collab = CollaborativeFiltering2.get_movie_from_genre(action)
            movie = pd.read_csv("movies.csv")
            movies = Toplevel()
            movies.title('Movies')
            movies.geometry("700x500")
            my_label = Label(movies, text="Genre")

            x = Label(movies, text='Here are some movies you may like ', font="Verdana 15").place(x=60, y=30)
            y = Label(movies, text='Please rate 3 movies ', font="Verdana 15").place(x=60, y=400)
            action_genre = Label(movies, text='Action ', font="Verdana 12").place(x=60, y=80)
            horror_genre = Label(movies, text='Horror ', font="Verdana 12").place(x=60, y=160)
            test = Label(movies, text = collab, font = "Verdana 12").place(x=60,y=240)

            text = movie.iloc[0]['title']
            mv = Label(movies, text = text).place(x=60,y=100)
            text = movie.iloc[1]['title']
            mv = Label(movies, text=text).place(x=60, y=120)
            text = movie.iloc[2]['title']
            mv = Label(movies, text=text).place(x=60, y=180)
            text = movie.iloc[3]['title']
            mv = Label(movies, text=text).place(x=60, y=200)
            text = movie.iloc[4]['title']
            mv = Label(movies, text=text).place(x=60, y=260)
            #text = movie.iloc[5]['title']
            list1 = get_top_2_movies(collab)
            text = list1[0]
            mv = Label(movies, text=text).place(x=60, y=280)

            mini_window = Tk()
            label_1 = Label(mini_window,text ="Please enter title of a movie you have seen in the list:")
            entry_1 = Entry(mini_window)
            button_1 = Button(mini_window, text = "Click me to enter title")
            label_1.grid(row=0,column=0)
            entry_1.grid(row=0,column=1)
            button_1.grid(row=1,column=0)

            label_2 = Label(mini_window, text="Please enter a rating:")
            entry_2 = Entry(mini_window)
            button_2 = Button(mini_window, text="Click me to enter rating")
            label_2.grid(row=2, column=0)
            entry_2.grid(row=2, column=1)
            button_2.grid(row=3, column=0)

            title = entry_1.get()
            print(title)
            rating = entry_2.get()
            print(rating)

            my_label.pack()
            movies.mainloop()

    next = Button(c, text="Next", command=show).place(x=350, y=400)


    c.mainloop()


first_Label = Label(root, text="Welcome to the Movie Recommendation System", font="Verdana 20")
second_Label = Label(root, text="choose an algorithm for a movie recommendation", font="Verdana 20")
collaborative_Button = Button(root, text="Collaborative Filtering", font="Verdana 15", command=collaborative)
content_Button = Button(root, text="Content Filtering", font="Verdana 15", command=content)

first_Label.place(x=130, y=70)
second_Label.place(x=120, y=100)
collaborative_Button.pack(padx=60, pady=20, side=LEFT)
content_Button.pack(padx=60, pady=20, side=RIGHT)
root.mainloop()

