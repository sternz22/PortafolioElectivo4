from django.contrib import admin
from .models import Home
from .models import About
from .models import Contact
from .models import Red

class HomeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class RedAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Home, HomeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Red, RedAdmin)