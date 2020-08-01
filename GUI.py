from tkinter import *
from collaborativeFiltering import *

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


first_Label = Label(root, text="Welcome to the Movie Recommendation System", font="Verdana 20")
second_Label = Label(root, text="choose an algorithm for a movie recommendation", font="Verdana 20")
collaborative_Button = Button(root, text="Collaborative Filtering", font="Verdana 15")
content_Button = Button(root, text="Content Filtering", font="Verdana 15", command=content)


first_Label.place(x=130, y=70)
second_Label.place(x=120, y=100)
collaborative_Button.pack(padx=60, pady=20, side=LEFT)
content_Button.pack(padx=60, pady=20, side=RIGHT)


root.mainloop()
