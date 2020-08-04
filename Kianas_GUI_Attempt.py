from tkinter import *
from tkinter import ttk
import winsound
import pandas as pd
from PIL import ImageTk, Image
import main
import movie_fetcher

# import getPoster

root = Tk()
root.title('Movie Recommendation Engine')
root.geometry("700x500")
root.configure(background='black')
# import image
img1 = ImageTk.PhotoImage(file="movie_logo2.jpg")
my_label1 = Label(image=img1)
my_label1.pack(side="bottom")

img2 = ImageTk.PhotoImage(file="popcorn animated.jpg")
my_label2 = Label(image=img2)
my_label2.pack(side="right")

# play music
#winsound.PlaySound('africa-toto.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)


def content():
    top = Toplevel()
    top.title('Content Based Filtering')
    top.geometry("700x500")
    m = Label(top, text='Enter a favorite movie: ', font="Verdana 15")
    user_fave_movie = Entry(top, width=30)
    m.place(x=200, y=100)
    user_fave_movie.place(x=200, y=140)
    user_fave_movie.focus()

    def entered():
        m.forget()
        title = Label(top, text='We think you will love these movies too!', font="Verdana 15", border="2")
        title.place(x=200, y=40)
        user_input = user_fave_movie.get()
        # recommendations = nicksCode.improved_recommendations(str(user_input))
        # recommendations_display = Label(top, text=recommendations)
        # recommendations_display.place(x=240, y=140)
        user_fave_movie.destroy()
        enter.destroy()

    enter = ttk.Button(top, text='Enter', command=entered)
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
        c.destroy()
        list_of_movie_genres = []

        if action.get() == 1:
            list_of_movie_genres.append("Action")

        if adventure.get() == 1:
            list_of_movie_genres.append("Adventure")

        if animation.get() == 1:
            list_of_movie_genres.append("Animation")

        if sci_fi.get() == 1:
            list_of_movie_genres.append("Sci-Fi")

        if children.get() == 1:
            list_of_movie_genres.append("Children")

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

        if documentary.get() == 1:
            list_of_movie_genres.append("Documentary")

        if imax.get() == 1:
             list_of_movie_genres.append("Imax")

        if war.get() == 1:
            list_of_movie_genres.append("War")

        if musical.get() == 1:
            list_of_movie_genres.append("Musical")

        if film_noir.get() == 1:
            list_of_movie_genres.append("Film-Noir")

        if western.get() == 1:
            list_of_movie_genres.append("Western")

        movies = Toplevel()
        movies.title('Movies')
        movies.geometry("700x500")
        my_label = Label(movies, text="Genre")

        x = Label(movies, text='Here are some movies you may like ', font="Verdana 15").place(x=60, y=30)
        y = Label(movies, text='Please rate 5 movies ', font="Verdana 15").place(x=60, y=400)

        genre_1 = Label(movies, text=list_of_movie_genres[0], font="Verdana 12").place(x=60, y=80)
        genre_2 = Label(movies, text=list_of_movie_genres[1], font="Verdana 12").place(x=60, y=160)
        genre_3 = Label(movies, text=list_of_movie_genres[2], font="Verdana 12").place(x=60, y=240)

        movies_one_two = movie_fetcher.get_movies_from_genre(list_of_movie_genres[0])
        # getPoster.get_poster('http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)',)
        movies_three_four = movie_fetcher.get_movies_from_genre(list_of_movie_genres[1])
        movie_five_six = movie_fetcher.get_movies_from_genre(list_of_movie_genres[2])

        mv = Label(movies, text=movies_one_two).place(x=60, y=120)
        mv2 = Label(movies, text=movies_three_four).place(x=60, y=220)
        mv3 = Label(movies, text=movie_five_six).place(x=60, y=320)
        count = 5

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

            def retrieve_movies():
                newcount = count - 1
                movie = user_movie_input.get()
                rating = user_rating.get()
                dict[movie] = rating
                print("dict", dict)
                str_count = str(count - len(dict))
                print("Dictionary length:", len(dict))
                print("Str", str_count)
                num_movies_rated_label = Label(mini_window, text="# movies left to rate: " + str_count)
                num_movies_rated_label.grid(row=4, column=1)

                return dict

            str_count = str(count)

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
                print("list of keys",keys_list)
                # list of values
                values_list1 = dict.values()
                for key in keys_list:
                    keys_.append(key)

                print("New key list:", keys_)
                for value in values_list1:
                    values_.append(value)
                print("New values list:", values_)

                convert = {}
                convert[main.find_movie_Id(keys_[0])] = values_[0]
                convert[main.find_movie_Id(keys_[1])] = values_[1]
                convert[main.find_movie_Id(keys_[2])] = values_[2]
                convert[main.find_movie_Id(keys_[3])] = values_[3]
                convert[main.find_movie_Id(keys_[4])] = values_[4]

                print("Converted dictionary", convert)
                main.write_to_file(convert)

                list_of_recommended_movies = main.GUI_Output()
                a = Label(last_window, text='Movies Recommended For You', font="Verdana 15").place(x=60, y=0)
                mv = Label(last_window, text="1. " + list_of_recommended_movies[0]).place(x=60, y=120)
                mv = Label(last_window, text="2. " +list_of_recommended_movies[1]).place(x=60, y=140)
                mv = Label(last_window, text="3. " +list_of_recommended_movies[2]).place(x=60, y=160)
                mv = Label(last_window, text="4. " +list_of_recommended_movies[3]).place(x=60, y=180)
                mv = Label(last_window, text="5. " +list_of_recommended_movies[4]).place(x=60, y=200)
                exit_Button1 = ttk.Button(last_window, text="Click to Exit", command=last_window.destroy).place(x=300, y=400)


            open_last_window = ttk.Button(mini_window, text="Get Recommendations", command=give_Rec)
            open_last_window.grid(row=4, column=0)

            num_movies_rated_label = Label(mini_window, text="# movies left to rate: " + str_count)
            num_movies_rated_label.grid(row=4, column=1)

        # opens mini_window
        next2 = ttk.Button(movies, text="Click here to rate movie", command=mini_win).place(x=500, y=380)

        my_label.pack()
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

#collaborative_Button = ttk.Button(root, text="Collaborative Filtering", command=collaborative)
#content_Button = Button(root, text="Content Filtering", font="Verdana 15", command=content)

first_Label.place(x=130, y=70)
second_Label.place(x=120, y=100)
collaborative_Button.place(x=210, y=180)
content_Button.place(x=210, y=270)
exit_Button = ttk.Button(root,text="Click to Exit",command=root.destroy).place(x=300,y=400)
root.mainloop()


