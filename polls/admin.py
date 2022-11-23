from django.contrib import admin
from .models import Question, Choice, Chat


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


class ChatAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                ['name']
            ),
        }),
        ('Text', {
            'fields': (
                ['message']
            )
        })
    )
    list_display = ('name', 'message', 'date')
    

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
admin.site.register(Chat, ChatAdmin)

