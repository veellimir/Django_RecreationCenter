from django.contrib import admin

from .models import Support, StatusSupport, CommentSupport


class Comment(admin.StackedInline):
    model = CommentSupport
    fields = ('comment_text', 'comment_date')
    readonly_fields = ('comment_date', )

    extra = 0


class SupportAdmin(admin.ModelAdmin):
    list_display = ('sp_status', 'sp_name', 'sp_phone', 'sp_date')
    list_display_links = ('sp_name', )
    list_editable = ('sp_status', 'sp_phone')
    search_fields = ('sp_name', 'sp_phone')
    list_filter = ('sp_status', )

    inlines = [Comment]


admin.site.register(Support, SupportAdmin)
admin.site.register(StatusSupport)
admin.site.register(CommentSupport)
