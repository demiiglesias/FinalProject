from tkinter import *
import pandas as pd
# import main

root = Tk()
root.title('Movie Recommendation Engine')
root.geometry("700x500")

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
    c = Toplevel()
    c.title('Collaborative Based Filtering')
    c.geometry("700x500")

    m = Label(c, text='Pick 3 of your favorite genres ', font="Verdana 15")
    m.place(x=60, y=10)

    # Genres for check-box
    action = IntVar()
    chk = Checkbutton(c, text="Action", variable=action).place(x=60, y=40)
    children = IntVar()
    chk = Checkbutton(c, text="Children", variable=children).place(x=60, y=100)
    sci_fi = IntVar()
    chk = Checkbutton(c, text="Sci-Fi", variable=sci_fi).place(x=60, y=340)
    adventure = IntVar()
    chk = Checkbutton(c, text="Adventure", variable=adventure).place(x=60, y=60)
    animation = IntVar()
    chk = Checkbutton(c, text="Animation", variable=animation).place(x=60, y=80)
    comedy = IntVar()
    chk = Checkbutton(c, text="Comedy", variable=comedy).place(x=60, y=120)
    thriller = IntVar()
    chk = Checkbutton(c, text="Thriller", variable=thriller).place(x=60, y=360)
    romance = IntVar()
    chk = Checkbutton(c, text="Romance", variable=romance).place(x=60, y=320)
    horror = IntVar()
    chk = Checkbutton(c, text="Horror", variable=horror).place(x=60, y=240)
    drama = IntVar()
    chk = Checkbutton(c, text="Drama", variable=drama).place(x=60, y=160)
    crime = IntVar()
    chk = Checkbutton(c, text="Crime", variable=crime).place(x=60, y=140)
    mystery = IntVar()
    chk = Checkbutton(c, text="Mystery", variable=mystery).place(x=60, y=300)
    fantasy = IntVar()
    chk = Checkbutton(c, text="Fantasy", variable=fantasy).place(x=60, y=200)
    documentary = IntVar()
    chk = Checkbutton(c, text="Documentary", variable=documentary).place(x=60, y=180)
    imax = IntVar()
    chk = Checkbutton(c, text="Imax", variable=imax).place(x=60, y=260)
    war = IntVar()
    chk = Checkbutton(c, text="War", variable=war).place(x=60, y=380)
    musical = IntVar()
    chk = Checkbutton(c, text="Musical", variable=musical).place(x=60, y=280)
    film_noir = IntVar()
    chk = Checkbutton(c, text="Film-Noir", variable=film_noir).place(x=60, y=220)
    western = IntVar()
    chk = Checkbutton(c, text="Western", variable=western).place(x=60, y=400)

    def show():
        list_of_movie_genres = []

        if action.get() == 1:
            list_of_movie_genres.append("Action")

        if adventure.get() == 1:
            list_of_movie_genres.append("Adventure")

        if animation.get() == 1:
            list_of_movie_genres.append("Animation")

        movie = pd.read_csv("movies.csv")
        movies = Toplevel()
        movies.title('Movies')
        movies.geometry("700x500")
        my_label = Label(movies, text="Genre")

        x = Label(movies, text='Here are some movies you may like ', font="Verdana 15").place(x=60, y=30)
        y = Label(movies, text='Please rate 10 movies ', font="Verdana 15").place(x=60, y=400)

        genre_1 = Label(movies, text=list_of_movie_genres[0], font="Verdana 12").place(x=60, y=80)
        genre_2 = Label(movies, text=list_of_movie_genres[1], font="Verdana 12").place(x=60, y=160)
        genre_3 = Label(movies, text=list_of_movie_genres[2], font="Verdana 12").place(x=60, y=240)

        # movie_1 = main.get_movie_from_genre(genre_1)
        # movie_2 = main.get_movie_from_genre(genre_1)
        # movie_3 = main.get_movie_from_genre(genre_2)
        # movie_4 = main.get_movie_from_genre(genre_2)
        # movie_5 = main.get_movie_from_genre(genre_3)
        # movie_6 = main.get_movie_from_genre(genre_3)

        text = movie.iloc[0]['title']
        mv = Label(movies, text=text).place(x=60, y=100)
        #mv = Label(movies,text=movie_1).place(x=60,y=100)
        text = movie.iloc[1]['title']
        mv = Label(movies, text=text).place(x=60, y=120)
        text = movie.iloc[2]['title']
        mv = Label(movies, text=text).place(x=60, y=180)
        text = movie.iloc[3]['title']
        mv = Label(movies, text=text).place(x=60, y=200)
        text = movie.iloc[4]['title']
        mv = Label(movies, text=text).place(x=60, y=260)
        text = movie.iloc[5]['title']
        mv = Label(movies, text=text).place(x=60, y=280)

        def mini_win():
            mini_window = Tk()
            user_title = Label(mini_window, text="Please enter title of a movie you have seen in the list:")
            user_title_text = Entry(mini_window)
            button_1 = Button(mini_window, text="Click me to enter title")
            user_title.grid(row=0, column=0)
            user_title_text.grid(row=0, column=1)
            button_1.grid(row=1, column=0)

            label_2 = Label(mini_window, text="Please enter a rating:")
            entry_2 = Entry(mini_window)
            button_2 = Button(mini_window, text="Click me to enter rating")
            label_2.grid(row=2, column=0)
            entry_2.grid(row=2, column=1)
            button_2.grid(row=3, column=0)

           # movie_rated = user_title_text.get() #returns movie title inputted
            #movie_ranking = entry_2.get()
            def retrieve_input():
                movie_rated = user_title_text.get() #returns movie title inputted
                return movie_rated
            print("movie",retrieve_input())
        #opens mini_window window
        next2 = Button(movies, text="Click here to rate movie", command=mini_win).place(x=500, y=380)


        my_label.pack()
        movies.mainloop()
    #opens next window
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
