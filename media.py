import webbrowser

class Movie():
    
    """ Data structure to store movie related information.
        1. Title
        2. Story line
        3. Poster url
        4. Trailer url
    """
    
    def __init__(self, movie_title, movie_storyline, movie_poster_url, movie_youtube_url):
        print("Initialize the movie object for " + movie_title)
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_youtube_url
