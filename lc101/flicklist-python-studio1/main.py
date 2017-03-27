import webapp2
import rand

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movie_titles = [
            "Love Actutally",
            "Star Wars Trilogy",
            "Sound of Music",
            "Lord of the Rings Trilogy",
            "10 Things I Hate About You"
        ]
        # TODO: randomly choose one of the movies, and return it
        index = random.randint(0, 4)
        return movie_titles[index]

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
