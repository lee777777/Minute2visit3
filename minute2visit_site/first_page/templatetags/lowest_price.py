from django import template
from ..models import Tour

register = template.Library()

@register.filter
def lowest_price(value):
    tour = Tour.objects.get(id=value)
    price_of_one = tour.price_of_one
    price_of_2_to_4 = tour.price_of_2_to_4
    price_of_5_to_9 = tour.price_of_5_to_9
    price_of_10_to_15 = tour.price_of_10_to_15
    price_of_16_to_20 = tour.price_of_16_to_20
    prices =   [price_of_one,price_of_2_to_4 ,price_of_5_to_9, price_of_10_to_15,price_of_16_to_20]
    min = prices[0]
    for i in range(len(prices)):
        if prices[i] <min:
         min = prices[i]
    return min