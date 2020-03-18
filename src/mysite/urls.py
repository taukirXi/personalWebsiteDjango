from django.urls import path
from .views import (home,
                    portfolio,
                    contact,
                    )

urlpatterns = [
    path('', home, name='home'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),

]
