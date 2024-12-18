from django.contrib import admin
from .models import Profile
from django.utils.html import format_html


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo_preview')
    search_fields = ('user__username',)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" style="width:50px; height:50px; object-fit:cover;" />')
        return "Sem foto"
    photo_preview.short_description = "Foto de Perfil"