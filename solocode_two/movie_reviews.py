from random import choice


def round_to_half(n):
    # rounds a number to the nearest half
    # https://stackoverflow.com/questions/1329426/how-do-i-round-to-the-nearest-0-5
    return round(n * 2) / 2


class Review:
    def __init__(self, rating, review):
        self.rating = self.set_rating(rating)
        self.review = review

    def set_rating(self, rating):
        if rating < 0 or rating >= 5:
            raise Exception("Rating outside of range (0-5)")
        return round_to_half(rating)

    def get_rating(self):
        return self.rating

    def get_review(self):
        return self.review

    def display(self):
        print(f"{self.rating}-star review: \n\t{self.review}")


class Movie:
    def __init__(self, title):
        self.title = title
        self.reviews: list[Review] = []

    def add_review(self, review):
        self.reviews.append(review)

    def get_average_rating(self):
        scores = [review.get_rating() for review in self.reviews]

        return round_to_half(sum(scores) / len(scores))

    def get_best_review(self):
        top_reviews = []
        sorted_reviews = sorted(
            self.reviews, key=lambda a: a.get_rating(), reverse=True
        )  # sort by rating, descending
        top_review_score = sorted_reviews[0].get_rating()
        for review in sorted_reviews:
            if review.get_rating() == top_review_score:
                top_reviews.append(review)

        return choice(top_reviews)

    def get_worst_review(self):
        top_reviews = []
        sorted_reviews = sorted(
            self.reviews, key=lambda a: a.get_rating()
        )  # sort by rating, ascending
        bottom_review_score = sorted_reviews[0].get_rating()
        for review in sorted_reviews:
            if review.get_rating() == bottom_review_score:
                top_reviews.append(review)

        return choice(top_reviews)


def main():
    # Write a review of Star Wars
    star_wars = Movie("Star Wars")
    star_wars.add_review(Review(4.5, "Pretty good! I recommend it!"))
    star_wars.add_review(Review(2.5, "Eh. Skip it."))
    star_wars.add_review(Review(3, "It's okay, I guess."))

    print(f"Average rating: {star_wars.get_average_rating()}")
    print("Best review:")
    star_wars.get_best_review().display()
    print("Worst review:")
    star_wars.get_worst_review().display()


if __name__ == "__main__":
    main()
