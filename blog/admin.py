from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Bus,Schedule,MyUser,Booking


admin.site.register(Bus)
admin.site.register(Schedule)
admin.site.register(MyUser,UserAdmin)
admin.site.register(Booking)

# admin.site.register(Customer)



# Register your models here.
