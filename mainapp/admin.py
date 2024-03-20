from django.contrib import admin

from .utils import dynamic_models, get_admin_options, html_img
from .models import Services, Tag, InfoSlider, Menu, Entertainment


class ServicesAdmin(admin.ModelAdmin):
    form = dynamic_models(Services)
    fields, readonly_fields, list_display, search_fields = get_admin_options()

    def html_img(self, img):
        return html_img(self, img)


class MenuAdmin(admin.ModelAdmin):
    form = dynamic_models(Menu)
    fields, readonly_fields, list_display, search_fields = get_admin_options()

    def html_img(self, img):
        return html_img(self, img)


class EntertainmentAdmin(admin.ModelAdmin):
    form = dynamic_models(Entertainment)
    fields, readonly_fields, list_display, search_fields = get_admin_options()

    def html_img(self, img):
        return html_img(self, img)


class InfoSliderAdmin(admin.ModelAdmin):
    form = dynamic_models(InfoSlider)


admin.site.register(Services, ServicesAdmin)
admin.site.register(Tag)
admin.site.register(InfoSlider, InfoSliderAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Entertainment, EntertainmentAdmin)

admin.site.site_header = 'ᚱECREᛏION CENᛏEᚱ админ-панель'
