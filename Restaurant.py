class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._reviews = []
        self.all_customers.append(self)

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self._name = name
        self._reviews = []
        self.all_restaurants.append(self)

    def name(self):
        return self._name

    def reviews(self):
        return self._reviews

    def customers(self):
        return list({review.customer() for review in self._reviews})

    def average_star_rating(self):
        if not self._reviews:
            return 0
        total_rating = sum(review.rating() for review in self._reviews)
        return total_rating / len(self._reviews)

    @classmethod
    def all(cls):
        return cls.all_restaurants


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        self.all_reviews.append(self)
        customer._reviews.append(self)
        restaurant._reviews.append(self)

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

    def rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls.all_reviews



customer1 = Customer("George", "Washington")
customer2 = Customer("John", "Mutwiri")

restaurant1 = Restaurant("Highland Park")
restaurant2 = Restaurant("Continental")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer1, restaurant2, 5)
review3 = Review(customer2, restaurant1, 3)

print(customer1.full_name()) 
print(customer2.given_name())
print(customer2.family_name())
print(restaurant1.name())  
print(restaurant2.name())
print(restaurant1.average_star_rating())
print(restaurant2.average_star_rating())
print(restaurant1.name() in restaurant2.customers())
print(review1.customer().full_name())