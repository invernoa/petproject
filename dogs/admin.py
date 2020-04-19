from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.
from .models import Dog, Kennel, DogBreed, User

class DogAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "units", "size", "hair", "breed", "created_at", "breed", "sex")

admin.site.register(Dog, DogAdmin)



class KennelAdmin(admin.ModelAdmin):

    def kennel_breeds(self, obj):
        return "\n".join([breed.name for breed in obj.breeds.all()])

    list_display = ("name", "creator", "kennel_breeds", "about", 'photo', 'city')

admin.site.register(Kennel, KennelAdmin)


class DogBreedAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "number", 'size', 'hair', 'country')


admin.site.register(DogBreed, DogBreedAdmin)


# class FCIgroupAdmin(admin.ModelAdmin):
#
#
#     list_display = ('name', 'number')
#
# admin.site.register(FCIGroup, FCIgroupAdmin)