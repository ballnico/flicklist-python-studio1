#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomMovie():

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

class Index(webapp2.RequestHandler):
    def get(self):
        # choose a movie by invoking our new function
        movie = getRandomMovie()
        movie2 = getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>" + "<p>" + movie + "</p>" + "<h1>Tomorrow's Movie of the Day</h1>" + "<p>" + movie2 + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"


        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
