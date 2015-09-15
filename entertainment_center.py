import fresh_tomatoes
import media


class EntertainmentCenter():

    """ Creates a list of favorite Movies and displays them on a webpage."""

    def create_movies(self):
        """ Generates the list of favorite Movies

            Returns : list of favorite movies
        """
        toy_story = media.Movie(
            "Toy Story",
            "A story of a boy and his toys that come to life",
            "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
            "https://www.youtube.com/watch?v=ZZv1vki4ou4")
        avatar = media.Movie(
            "Avatar",
            "A marine in alien planet",
            "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
            "https://www.youtube.com/watch?v=5PSNL1qE6VY")
        departed = media.Movie(
            "Departed",
            "Cops and Gangsters",
            "https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg",
            "https://www.youtube.com/watch?v=auYbpnEwBBg")
        shrek = media.Movie(
            "Shrek",
            "Fairy tale",
            "https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",
            "https://www.youtube.com/watch?v=W37DlG1i61s")
        cars = media.Movie(
            "Cars",
            "Cars animation movie",
            "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
            "https://www.youtube.com/watch?v=SbXIj2T-_uk")
        inside_out = media.Movie(
            "Inside out",
            "animation",
            "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",  # noqa
            "https://www.youtube.com/watch?v=seMwpP0yeu4")

        movies_list = [toy_story, avatar, departed, shrek, cars, inside_out]
        return movies_list

    def display_favorite_movies(self):
        """ Displays the list of favorite movies on a webpage """
        fresh_tomatoes.open_movies_page(self.create_movies())

EntertainmentCenter().display_favorite_movies()
