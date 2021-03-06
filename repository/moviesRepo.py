from domain.stuff import *
from repository.repoException import *
from assig9.assig9 import *


class moviesRepository:

    def __init__(self):
        self.movies = Iterable()

    def add(self, movie):
        self.movies.append(movie)

    def findID(self, ID):
        for i in range(0, len(self.movies)):
            if self.movies[i].ID == ID:
                return True
        return False

    '''
    def find(self, movie):
        for i in range(0, len(self.movies)):
            if self.movies[i] == movie:
                return i
        return False
    '''

    def remove(self, movie):
        if self.find(movie) != False:
            del self.movies[self.find(movie)]
        else:
            raise ValueError("We do not have the movie at the shop!")

    def update(self, movie, movieN):
        self.movies[self.find(movie)] = movieN

    def getAll(self):
        return self.movies

    def __str__(self):
        r = ""
        for i in self.movies:
            r += str(i)
        return r

