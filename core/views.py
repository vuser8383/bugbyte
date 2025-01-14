from django.shortcuts import render
from core.models import Restaurant, Rating, Sale
from django.db.models import Sum, Prefetch
from django.utils import timezone

# Create your views here.
def index(request):
  month_ago = timezone.now() - timezone.timedelta(days=30)
  monthly_sales = Prefetch(
    'sales', # lookup
    queryset=Sale.objects.filter(datetime__gte=month_ago) # queryset
  )
  restaurants = Restaurant.objects.prefetch_related('ratings', monthly_sales).filter(ratings__rating=5)
  restaurants = restaurants.annotate(total=Sum('sales__income'))
  # restaurants = Restaurant.objects.prefetch_related('ratings', 'sales')\
  #   .filter(ratings__rating=5)\
  #   .annotate(total=Sum('sales__income'))
  # ratings = Rating.objects.only('rating', 'restaurant__name').select_related('restaurant')
  # context = {'ratings': ratings}
  # restaurants = Restaurant.objects.filter(name__istartswith='p').prefetch_related("ratings", "sales")
  print(restaurants)
  print([r.total for r in restaurants])
  context = {'restaurants': restaurants}
  return render(request, "core/index.html", context)