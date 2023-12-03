class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        self.__class__.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        self.__class__.all_restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        return list(set([review.customer() for review in self.reviews]))

    def average_star_rating(self):
        total_ratings = sum([review.rating() for review in self.reviews])
        num_reviews = len(self.reviews)
        if num_reviews == 0:
            return 0
        return total_ratings / num_reviews

    @classmethod
    def all(cls):
        return cls.all_restaurants


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.__class__.all_reviews.append(self)
        customer.reviews.append(self)
        restaurant.reviews.append(self)

    def rating(self):
        return self.rating

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews