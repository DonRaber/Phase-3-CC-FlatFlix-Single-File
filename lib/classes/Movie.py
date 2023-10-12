from statistics import mean

class Movie:

    all = []

    def __init__(self, title):
        self.title = title
        Movie.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception('Invalid Title')

    def reviews(self):
        from classes.Review import Review
        return [review for review in Review.all if review.movie is self]


    def reviewers(self):
        return list({review.viewer for review in self.reviews()})


    def average_rating(self):
        total_ratings = [review.rating for review in self.reviews() if review.movie is self]
        if len(total_ratings) > 0:
            return round(mean(total_ratings), 1)
        else:
            return None