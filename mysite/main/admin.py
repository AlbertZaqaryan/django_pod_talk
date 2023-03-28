from django.contrib import admin
from .models import HomeLogo, HomeInfo, HomeSlider, HomeFooterBg, LastEpisode
# Register your models here.


admin.site.register(HomeLogo)
admin.site.register(HomeInfo)
admin.site.register(HomeFooterBg)
admin.site.register(LastEpisode)


@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']