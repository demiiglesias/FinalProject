from tkinter import *
from tkinter import ttk
import content_based
import movie_fetcher
import Item_Item
import CollaborativeFiltering2

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
        m.destroy()
        title = Label(top, text='We think you will love these movies too!', font="Verdana 15", border="2")
        title.place(x=200, y=70)
        user_input = user_fave_movie.get()
        recommendations = content_based.recommender(str(user_input))
        recommendations_display = Label(top, text=recommendations)
        recommendations_display.place(x=240, y=140)
        user_fave_movie.destroy()
        enter.destroy()

    enter = Button(top, text='Enter', command=entered)
    enter.place(x=200, y=180)

    top.mainloop()


# rating1 = Spinbox(c, from_=0, to=5, width=3)
#     rating1.pack(

def collaborative():
    c = Toplevel()
    c.title('Collaborative Based Filtering')
    c.geometry("700x500")

    m = Label(c, text='Pick 3 of your favorite genres ', font="Verdana 15")
    m.place(x=60, y=10)

    d = Label(c, text='Insert your favorite movie', font="Verdana 15")
    d.place(x=360, y=10)
    input = Entry(c).place(x=365, y=40)

    # Genres for check-box
    action = IntVar()
    chk = Checkbutton(c, text="Action", variable=action).place(x=60, y=40)
    children = IntVar()
    chk = Checkbutton(c, text="Family", variable=children).place(x=60, y=60)
    sci_fi = IntVar()
    chk = Checkbutton(c, text="Science-Fiction", variable=sci_fi).place(x=60, y=80)
    adventure = IntVar()
    chk = Checkbutton(c, text="Adventure", variable=adventure).place(x=60, y=100)
    animation = IntVar()
    chk = Checkbutton(c, text="Animation", variable=animation).place(x=60, y=120)
    comedy = IntVar()
    chk = Checkbutton(c, text="Comedy", variable=comedy).place(x=60, y=140)
    thriller = IntVar()
    chk = Checkbutton(c, text="Thriller", variable=thriller).place(x=60, y=160)
    romance = IntVar()
    chk = Checkbutton(c, text="Romance", variable=romance).place(x=60, y=180)
    horror = IntVar()
    chk = Checkbutton(c, text="Horror", variable=horror).place(x=60, y=200)
    drama = IntVar()
    chk = Checkbutton(c, text="Drama", variable=drama).place(x=60, y=220)
    crime = IntVar()
    chk = Checkbutton(c, text="Crime", variable=crime).place(x=60, y=240)
    mystery = IntVar()
    chk = Checkbutton(c, text="Mystery", variable=mystery).place(x=60, y=260)
    fantasy = IntVar()
    chk = Checkbutton(c, text="Fantasy", variable=fantasy).place(x=60, y=280)
    war = IntVar()
    chk = Checkbutton(c, text="War", variable=war).place(x=60, y=300)
    musical = IntVar()
    chk = Checkbutton(c, text="Musical", variable=musical).place(x=60, y=320)

    western = IntVar()
    chk = Checkbutton(c, text="Western", variable=western).place(x=60, y=340)

    def show():
        c.destroy()
        list_of_movie_genres = []

        if action.get() == 1:
            list_of_movie_genres.append("Action")

        if adventure.get() == 1:
            list_of_movie_genres.append("Adventure")

        if animation.get() == 1:
            list_of_movie_genres.append("Animation")

        if sci_fi.get() == 1:
            list_of_movie_genres.append("Science-Fiction")

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
            list_of_movie_genres.append("Musical")

        if western.get() == 1:
            list_of_movie_genres.append("Western")

        movies = Toplevel()
        movies.title('Movies')
        movies.geometry("700x500")

        x = Label(movies, text='Here are some movies you may like ', font="Verdana 15").place(x=20, y=30)
        # y = Label(movies, text='Please rate 5 movies ', font="Verdana 15").place(x=400, y=30)
        extra = Label(movies, text='Movies similar to your favorite movie:', font="Verdana 15").place(x=350, y=30)

        genre_1 = Label(movies, text=list_of_movie_genres[0], font="Verdana 15").place(x=30, y=80)
        genre_2 = Label(movies, text=list_of_movie_genres[1], font="Verdana 15").place(x=30, y=180)
        genre_3 = Label(movies, text=list_of_movie_genres[2], font="Verdana 15").place(x=30, y=280)

        movies_one_two = movie_fetcher.get_movies_from_genre(list_of_movie_genres[0])
        movies_three_four = movie_fetcher.get_movies_from_genre(list_of_movie_genres[1])
        movie_five_six = movie_fetcher.get_movies_from_genre(list_of_movie_genres[2])

        mv = Label(movies, text=movies_one_two).place(x=30, y=120)
        mv2 = Label(movies, text=movies_three_four).place(x=30, y=220)
        mv3 = Label(movies, text=movie_five_six).place(x=30, y=320)

        mv4 = Label(movies, text='1. ' + Item_Item.get_rec_movies()[0]).place(x=350, y=70)
        mv5 = Label(movies, text='2. ' + Item_Item.get_rec_movies()[1]).place(x=350, y=90)
        mv6 = Label(movies, text='3. ' + Item_Item.get_rec_movies()[2]).place(x=350, y=110)
        mv7 = Label(movies, text='4. ' + Item_Item.get_rec_movies()[3]).place(x=350, y=130)
        mv8 = Label(movies, text='5. ' + Item_Item.get_rec_movies()[4]).place(x=350, y=150)

        def mini_win():

            mini_window = Tk()
            mini_window.title('Rate Movies you have seen')
            user_title_label = Label(mini_window, text="Please enter title of a movie you have seen in the list:")
            user_title_label.grid(row=0, column=0)
            user_movie_input = Entry(mini_window)
            user_movie_input.grid(row=0, column=1)
            rating_label = Label(mini_window, text="Please enter a rating:")
            rating_label.grid(row=1, column=0)
            user_rating = Entry(mini_window)
            user_rating.grid(row=1, column=1)
            dict = {}
            count = 5

            def retrieve_movies():
                movie = user_movie_input.get()
                rating = user_rating.get()
                dict[movie] = rating
                print("dict", dict)
                str_count = str(count - len(dict))
                num_movies_rated_label = Label(mini_window, text="# movies left to rate: " + str_count)
                num_movies_rated_label.grid(row=4, column=1)

                return dict

            # To retrieve value when enter is selected
            enter_button = ttk.Button(mini_window, text="Enter", command=retrieve_movies)
            enter_button.grid(row=3, column=0)

            def clear():
                user_movie_input.delete(0, 'end')
                user_rating.delete(0, 'end')

            clear_button = ttk.Button(mini_window, text="Clear text", command=clear)
            clear_button.grid(row=3, column=1)

            def give_Rec():
                mini_window.destroy()
                movies.destroy()
                last_window = Toplevel()
                last_window.title('Movies Recommended for you')
                last_window.geometry("700x500")
                # returns list of movies

                keys_ = []
                values_ = []

                # list of keys
                keys_list = dict.keys()

                # list of values
                values_list1 = dict.values()
                for key in keys_list:
                    keys_.append(key)

                for value in values_list1:
                    values_.append(value)

                convert = {CollaborativeFiltering2.find_movie_Id(keys_[0]): values_[0],
                           CollaborativeFiltering2.find_movie_Id(keys_[1]): values_[1],
                           CollaborativeFiltering2.find_movie_Id(keys_[2]): values_[2],
                           CollaborativeFiltering2.find_movie_Id(keys_[3]): values_[3],
                           CollaborativeFiltering2.find_movie_Id(keys_[4]): values_[4]}

                print("convert list:", convert)

                CollaborativeFiltering2.write_to_file(convert)
                # Item_Item.write_to_file()

                list_of_recommended_movies = CollaborativeFiltering2.GUI_Output()
                a = Label(last_window, text='Movies Recommended For You', font="Verdana 15").place(x=60, y=0)
                mv = Label(last_window, text="1. " + list_of_recommended_movies[0]).place(x=60, y=120)
                mv = Label(last_window, text="2. " + list_of_recommended_movies[1]).place(x=60, y=140)
                mv = Label(last_window, text="3. " + list_of_recommended_movies[2]).place(x=60, y=160)
                mv = Label(last_window, text="4. " + list_of_recommended_movies[3]).place(x=60, y=180)
                mv = Label(last_window, text="5. " + list_of_recommended_movies[4]).place(x=60, y=200)
                exit_Button1 = ttk.Button(last_window, text="Click to Exit", command=last_window.destroy).place(x=300,
                                                                                                                y=400)

            open_last_window = ttk.Button(mini_window, text="Get Recommendations", command=give_Rec)
            open_last_window.grid(row=4, column=0)

            # num_movies_rated_label = Label(mini_window, text="# movies left to rate: " + str_count)
            # num_movies_rated_label.grid(row=4, column=1)

        # opens mini_window
        next2 = ttk.Button(movies, text="Click here to rate movies", command=mini_win).place(x=460, y=380)

        movies.mainloop()

    # opens next window
    next3 = ttk.Button(c, text="Next", command=show).place(x=350, y=400)
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
