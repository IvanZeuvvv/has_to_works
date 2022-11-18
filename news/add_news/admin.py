from django.contrib import admin
from .models import Articles, Comments
from add_news.models import Articles


class CommentInLine(admin.TabularInline):
    model = Comments
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'anons', 'date_add', 'update_date']
    list_filter = ['activity']
    inlines = [CommentInLine]

    actions = ['mark_as_activity', 'mark_as_not_activity']

    def mark_as_activity(self, request, queryset):
        queryset.update(activity=True)


    def mark_as_not_activity(self, request, queryset):
        queryset.update(activity=False)

    mark_as_activity.short_description = 'Перевести в статус "Активно"'
    mark_as_not_activity.short_descriptions = 'Перевести в статус "Не активно"'




class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'text_comment', 'news']
    list_filter = ['username']

    actions = ['mark_as_activity', 'mark_as_not_activity']

    def mark_as_activity(self, request, queryset):
        queryset.update(status='a')

    def mark_as_not_activity(self, request, queryset):
        queryset.update(status='d')

    mark_as_activity.short_description = 'Перевести в статус "Активно"'
    mark_as_not_activity.short_descriptions = 'Перевести в статус "Удалено администратором"'
    #inlines = [CommentInLine]


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Comments, CommentAdmin,)


# Register your models here.
