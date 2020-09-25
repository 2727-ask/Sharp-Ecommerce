from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Ads
from .models import Orders
from .models import OrderUpdate
from .models import Product_Rating


admin.site.register(Product)
admin.site.register(Ads)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Product_Rating)


