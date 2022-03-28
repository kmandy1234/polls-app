from django.contrib import admin
from .models import Questions, Choice
# Register your models here.

admin.site.site_header = "Polling App Admin Panel"
admin.site.site_title = "Poll Admin"
admin.site.index_title = "welcome to the pollster admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields': ['question_text']}),
                ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Questions, QuestionAdmin)