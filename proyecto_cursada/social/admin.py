from django.contrib import admin
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Administrador").exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)