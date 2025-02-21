from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Bus,Schedule,MyUser,Booking
from import_export.admin import ImportExportModelAdmin

class BusAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...


admin.site.register(Bus)
admin.site.register(Schedule)
admin.site.register(MyUser,UserAdmin)
admin.site.register(Booking,BusAdmin)


    

# admin.site.register(Customer)



# Register your models here.