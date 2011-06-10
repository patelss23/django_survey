from django.db import models


class  Question(models.Model):
    """
    a class representing regular question
    """
    question = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    """
    a class representing regular choice
    """
    choice = models.CharField(max_length=200)

    def __unicode__(self):
        return self.choice

class Survey(models.Model):
    """
    a class representing survey
    """
    created = models.DateTimeField()
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class SurveyQuestion(models.Model):
    """
    a class representing a survey question 
    """
    question = models.ForeignKey(Question)
    #choice = models.ManyToManyField(SurveyChoice)
    survey = models.ManyToManyField(Survey)

    def __unicode__(self):
        return "SQ : " + self.question.question

class SurveyChoice(models.Model):
    """
    a class representing survey choice. 
    a survey choice has a next_question to be asked if selected and weight associated with it
    """
    choice = models.ForeignKey(Choice)
    weight = models.IntegerField()
    next_question = models.ForeignKey(SurveyQuestion)

    def __unicode__(self):
        return self.choice.choice 

