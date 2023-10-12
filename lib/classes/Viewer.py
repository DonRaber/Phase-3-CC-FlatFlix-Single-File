class Viewer:

    all = []

    def __init__(self, username):
        self.username = username
        Viewer.all.append(all)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 5 < len(username) < 17:
            self._username = username
        else:
            raise Exception('Invalid username')

    def reviews(self):
        from classes.Review import Review
        return [review for review in Review.all if review.viewer is self]


    def reviewed_movies(self):
        return list({review.movie for review in self.reviews()})


    def has_reviewed_movie(self, movie):
        if movie in self.reviewed_movies():
            return True
        else:
            return False


    def add_review(self, movie, rating):
        from classes.Review import Review
        return Review(self, movie, rating)