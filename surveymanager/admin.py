from surveymanager.models import *
from django.contrib import admin

class SurveyChoiceInline(admin.TabularInline):
    model = SurveyChoice.next_question.survey
    extra = 4

class SurveyQuestionInline(admin.TabularInline):
    model = SurveyQuestion.survey.through
    extra = 4

class SurveyChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice','next_question')

class SurveyQuestionAdmin(admin.ModelAdmin):
    fields = ['question','survey']
    #inlines = [SurveyChoiceInline]


class QuestionAdmin(admin.ModelAdmin):
    fields = ['question']
    list_filter = ['question']
    search_fields = ['question']

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['choice']
    list_filter = ['choice']
    search_fields = ['choice']

class SurveyAdmin(admin.ModelAdmin):
    fields = ['name','created']
    list_filter = ['created']
    search_fields = ['name']
    
    inlines = [SurveyQuestionInline, SurveyChoiceInline]


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Survey,SurveyAdmin)
admin.site.register(SurveyChoice,SurveyChoiceAdmin)
admin.site.register(SurveyQuestion,SurveyQuestionAdmin)
