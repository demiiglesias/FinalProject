from tkinter import *
from tkinter import ttk
import content_based
import movie_fetcher
import Item_Item

root = Tk()
root.title('Movie Recommendation Engine')
root.geometry("700x500")
root.configure(background='black')


def content():
    window1 = Toplevel()
    window1.title('Content-Based Filtering')
    window1.geometry("700x500")

    m = Label(window1, text='Pick 3 of your favorite genres ', font="Verdana 15")
    m.place(x=60, y=10)
    count = IntVar()
    # Genres for check-box
    action = IntVar()
    chk = Checkbutton(window1, text="Action", variable=action).place(x=60, y=40)
    children = IntVar()
    chk = Checkbutton(window1, text="Family", variable=children).place(x=60, y=60)
    sci_fi = IntVar()
    chk = Checkbutton(window1, text="Science Fiction", variable=sci_fi).place(x=60, y=80)
    adventure = IntVar()
    chk = Checkbutton(window1, text="Adventure", variable=adventure).place(x=60, y=100)
    animation = IntVar()
    chk = Checkbutton(window1, text="Animation", variable=animation).place(x=60, y=120)
    comedy = IntVar()
    chk = Checkbutton(window1, text="Comedy", variable=comedy).place(x=60, y=140)
    thriller = IntVar()
    chk = Checkbutton(window1, text="Thriller", variable=thriller).place(x=60, y=160)
    romance = IntVar()
    chk = Checkbutton(window1, text="Romance", variable=romance).place(x=60, y=180)
    horror = IntVar()
    chk = Checkbutton(window1, text="Horror", variable=horror).place(x=60, y=200)
    drama = IntVar()
    chk = Checkbutton(window1, text="Drama", variable=drama).place(x=60, y=220)
    crime = IntVar()
    chk = Checkbutton(window1, text="Crime", variable=crime).place(x=60, y=240)
    mystery = IntVar()
    chk = Checkbutton(window1, text="Mystery", variable=mystery).place(x=60, y=260)
    fantasy = IntVar()
    chk = Checkbutton(window1, text="Fantasy", variable=fantasy).place(x=60, y=280)
    war = IntVar()
    chk = Checkbutton(window1, text="War", variable=war).place(x=60, y=300)
    musical = IntVar()
    chk = Checkbutton(window1, text="Music", variable=musical).place(x=60, y=320)
    western = IntVar()
    chk = Checkbutton(window1, text="Western", variable=western).place(x=60, y=340)

    def show():
        window1.destroy()
        window2 = Toplevel()
        window2.title('Movies')
        window2.geometry("700x500")

        list_of_movie_genres = []
        if action.get() == 1:
            list_of_movie_genres.append("Action")

        if adventure.get() == 1:
            list_of_movie_genres.append("Adventure")

        if animation.get() == 1:
            list_of_movie_genres.append("Animation")

        if sci_fi.get() == 1:
            list_of_movie_genres.append("Science Fiction")

        if children.get() == 1:
            list_of_movie_genres.append("Family")

        if comedy.get() == 1:
            list_of_movie_genres.append("Comedy")

        if thriller.get() == 1:
            list_of_movie_genres.append("Thriller")

        if romance.get() == 1:
            list_of_movie_genres.append("Romance")

        if horror.get() == 1:
            list_of_movie_genres.append("Horror")

        if drama.get() == 1:
            list_of_movie_genres.append("Drama")

        if crime.get() == 1:
            list_of_movie_genres.append("Crime")

        if mystery.get() == 1:
            list_of_movie_genres.append("Mystery")

        if fantasy.get() == 1:
            list_of_movie_genres.append("Fantasy")

        if war.get() == 1:
            list_of_movie_genres.append("War")

        if musical.get() == 1:
            list_of_movie_genres.append("Music")

        if western.get() == 1:
            list_of_movie_genres.append("Western")

        Label(window2, text='Here are some movies you may like ', font="Verdana 15").place(x=20, y=30)
        Label(window2, text=list_of_movie_genres[0], font="Verdana 15").place(x=30, y=80)
        Label(window2, text=list_of_movie_genres[1], font="Verdana 15").place(x=30, y=180)
        Label(window2, text=list_of_movie_genres[2], font="Verdana 15").place(x=30, y=280)

        movies_one_two = movie_fetcher.get_movies_from_genre(list_of_movie_genres[0])
        movies_three_four = movie_fetcher.get_movies_from_genre(list_of_movie_genres[1])
        movie_five_six = movie_fetcher.get_movies_from_genre(list_of_movie_genres[2])

        mv = Label(window2, text=movies_one_two).place(x=30, y=120)
        mv2 = Label(window2, text=movies_three_four).place(x=30, y=220)
        mv3 = Label(window2, text=movie_five_six).place(x=30, y=320)
        # place(x=365, y=60)

        user_title_label = Label(window2, text="Please enter your favorite movie:")
        user_title_label.place(x=360, y=30)
        user_input = Entry(window2, width=30)
        user_input.place(x=365, y=60)

        def give_Rec():

            final_input = user_input.get()
            window2.destroy()
            last_window = Toplevel()
            last_window.geometry("700x500")
            last_window.title('Movies Recommended for you')
            Label(last_window, text='We think you will love these movies too!', font="Verdana 15", border="2")
            recommendations = content_based.recommender(str(final_input))
            Label(last_window, text=recommendations).place(x=240, y=120)

        ttk.Button(window2, text="Next", command=give_Rec).place(x=350, y=400)
        # opens up the small window to input title of favorite movie and get recommendations based off that input

        window2.mainloop()

    next3 = ttk.Button(window1, text="Next", command=show).place(x=350, y=400)
    window1.mainloop()


def collaborative():
    window1 = Toplevel()
    window1.title('Collaborative Based Filtering')
    window1.geometry("700x500")

    m = Label(window1, text='Pick 3 of your favorite genres ', font="Verdana 15")
    m.place(x=60, y=10)
    count = IntVar()
    # Genres for check-box
    action = IntVar()
    chk = Checkbutton(window1, text="Action", variable=action).place(x=60, y=40)
    children = IntVar()
    chk = Checkbutton(window1, text="Family", variable=children).place(x=60, y=60)
    sci_fi = IntVar()
    chk = Checkbutton(window1, text="Science Fiction", variable=sci_fi).place(x=60, y=80)
    adventure = IntVar()
    chk = Checkbutton(window1, text="Adventure", variable=adventure).place(x=60, y=100)
    animation = IntVar()
    chk = Checkbutton(window1, text="Animation", variable=animation).place(x=60, y=120)
    comedy = IntVar()
    chk = Checkbutton(window1, text="Comedy", variable=comedy).place(x=60, y=140)
    thriller = IntVar()
    chk = Checkbutton(window1, text="Thriller", variable=thriller).place(x=60, y=160)
    romance = IntVar()
    chk = Checkbutton(window1, text="Romance", variable=romance).place(x=60, y=180)
    horror = IntVar()
    chk = Checkbutton(window1, text="Horror", variable=horror).place(x=60, y=200)
    drama = IntVar()
    chk = Checkbutton(window1, text="Drama", variable=drama).place(x=60, y=220)
    crime = IntVar()
    chk = Checkbutton(window1, text="Crime", variable=crime).place(x=60, y=240)
    mystery = IntVar()
    chk = Checkbutton(window1, text="Mystery", variable=mystery).place(x=60, y=260)
    fantasy = IntVar()
    chk = Checkbutton(window1, text="Fantasy", variable=fantasy).place(x=60, y=280)
    war = IntVar()
    chk = Checkbutton(window1, text="War", variable=war).place(x=60, y=300)
    musical = IntVar()
    chk = Checkbutton(window1, text="Music", variable=musical).place(x=60, y=320)
    western = IntVar()
    chk = Checkbutton(window1, text="Western", variable=western).place(x=60, y=340)

    def show():
        window1.destroy()
        window2 = Toplevel()
        window2.title('Movies')
        window2.geometry("700x500")

        list_of_movie_genres = []
        if action.get() == 1:
            list_of_movie_genres.append("Action")

        if adventure.get() == 1:
            list_of_movie_genres.append("Adventure")

        if animation.get() == 1:
            list_of_movie_genres.append("Animation")

        if sci_fi.get() == 1:
            list_of_movie_genres.append("Science Fiction")

        if children.get() == 1:
            list_of_movie_genres.append("Family")

        if comedy.get() == 1:
            list_of_movie_genres.append("Comedy")

        if thriller.get() == 1:
            list_of_movie_genres.append("Thriller")

        if romance.get() == 1:
            list_of_movie_genres.append("Romance")

        if horror.get() == 1:
            list_of_movie_genres.append("Horror")

        if drama.get() == 1:
            list_of_movie_genres.append("Drama")

        if crime.get() == 1:
            list_of_movie_genres.append("Crime")

        if mystery.get() == 1:
            list_of_movie_genres.append("Mystery")

        if fantasy.get() == 1:
            list_of_movie_genres.append("Fantasy")

        if war.get() == 1:
            list_of_movie_genres.append("War")

        if musical.get() == 1:
            list_of_movie_genres.append("Music")

        if western.get() == 1:
            list_of_movie_genres.append("Western")

        Label(window2, text='Here are some movies you may like ', font="Verdana 15").place(x=20, y=30)
        Label(window2, text=list_of_movie_genres[0], font="Verdana 15").place(x=30, y=80)
        Label(window2, text=list_of_movie_genres[1], font="Verdana 15").place(x=30, y=180)
        Label(window2, text=list_of_movie_genres[2], font="Verdana 15").place(x=30, y=280)

        movies_one_two = movie_fetcher.get_movies_from_genre(list_of_movie_genres[0])
        movies_three_four = movie_fetcher.get_movies_from_genre(list_of_movie_genres[1])
        movie_five_six = movie_fetcher.get_movies_from_genre(list_of_movie_genres[2])

        mv = Label(window2, text=movies_one_two).place(x=30, y=120)
        mv2 = Label(window2, text=movies_three_four).place(x=30, y=220)
        mv3 = Label(window2, text=movie_five_six).place(x=30, y=320)
        # place(x=365, y=60)

        user_title_label = Label(window2, text="Please enter your favorite movie:")
        user_title_label.place(x=360, y=30)
        user_input = Entry(window2, width=30)
        user_input.place(x=365, y=60)

        # stores user liked
        user_liked_movies_list = []

        def give_Rec():
            final_input = user_input.get()
            # destroy() closes previous windows except the first
            window2.destroy()
            # mini_window.destroy()
            last_window = Toplevel()
            last_window.geometry("700x500")

            last_window.title('Movies Recommended for you')

            user_liked_movies_list.append(final_input)
            recommendations = Item_Item.rec(str(user_liked_movies_list[0]))

            Label(last_window, text=recommendations).place(x=240, y=120)

        window2_enter = ttk.Button(window2, text="Next", command=give_Rec).place(x=350, y=400)
        # opens up the small window to input title of favorite movie and get recommendations based off that input

        window2.mainloop()

    next3 = ttk.Button(window1, text="Next", command=show).place(x=350, y=400)
    window1.mainloop()


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
