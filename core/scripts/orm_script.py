from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint


def run():
  pass
  # deleting multiple objects
  Restaurant.objects.all().delete()
  
  # update multiple objects
  # restaurant = Restaurant.objects.filter(name__istartswith='p')
  # print(restaurant)
  # restaurant.update(
  #   date_opened = timezone.now() - timezone.timedelta(days=365),
  #   website = "https://www.test.com"
  # )

  # restaurant = Restaurant()
  # restaurant.name = "My italian restaurant 2"
  # restaurant.latitude = 50.2
  # restaurant.longitude = 50.2
  # restaurant.date_opened = timezone.now()
  # restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN

  # restaurant.save()


  # restaurant = Restaurant.objects.first()

  # print(restaurant.name)

  # restaurant.name = "New Restaurant Name"

  # restaurant.save(update_fields=['name'])

  # print(connection.queries)
  
  # user = User.objects.first()
  # restaurant = Restaurant.objects.first()
  # # Rating.objects.create(user=user,restaurant=restaurant,rating=9)
  # rating = Rating(user=user,restaurant=restaurant,rating=9)
  # rating.full_clean()
  # rating.save()
  # rating, created = Rating.objects.get_or_create(
  #   restaurant = restaurant, 
  #   user=user,
  #   rating=4
  # )
  # print(rating)
  # print(created)

  # print(Rating.objects.get_or_create(
  #   restaurant = restaurant, 
  #   user=user,
  #   rating=4
  # ))


  # print(restaurant.sales.all())
  
  # Sale.objects.create(
  #   restaurant = Restaurant.objects.first(),
  #   income=3.33,
  #   datetime = timezone.now()
  # )

  # Sale.objects.create(
  #   restaurant = Restaurant.objects.first(),
  #   income=4.33,
  #   datetime = timezone.now()
  # )
  
  # restaurant = Restaurant.objects.first()
  # access rating for the above restaurant using backward reference
  # print(restaurant.rating_set.first().rating)
  # print(restaurant.ratings.first().rating)

  #update 
  # restaurant = Restaurant.objects.first()
  # print(restaurant.name)
  # restaurant.name = "sldkjfklsdjfsldkjf"
  # restaurant.save()
  # pprint(connection.queries)
  
  
  # print(Rating.objects.exclude(rating=3))
  # print(Rating.objects.filter(rating__gte=3)) # __lte
  # print(Rating.objects.filter(rating=5))
  # restaurant = Restaurant.objects.first()
  # user = User.objects.first()
  # Rating.objects.create(user=user, restaurant=restaurant, rating=3)
  # print()
  # print(connection.queries)

  # restaurants = Restaurant.objects.first()
  # restaurants = Restaurant.objects.all()
  # restaurants = Restaurant.objects.all()[0]

  # Restaurant.objects.create(
  #     name="Pizza Shop",
  #     date_opened = timezone.now(),
  #     restaurant_type = Restaurant.TypeChoices.ITALIAN,
  #     latitude = 50.2,
  #     longitude=50.5
  # )
 
#  print(Restaurant.objects.last())
  # print(Restaurant.objects.count())
  
  

  # restaurant = Restaurant()
  # restaurant.name = "My italian restaurant"
  # restaurant.latitude = 50.2
  # restaurant.longitude = 50.2
  # restaurant.date_opened = timezone.now()
  # restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN

  # restaurant.save()