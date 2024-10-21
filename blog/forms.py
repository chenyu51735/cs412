from django import forms
from .models import Comment, Article


class CreateCommentForm(forms.ModelForm):
    '''A form to add a Comment on an Article to the database'''

    class Meta:
        model = Comment
        fields = ['article', 'author', 'text']
class CreateArticleForm(forms.ModelForm):
    '''A form to add a new Article to the database.'''
    class Meta:
        '''Associate this form with the Article model; select fields to add.'''
        model = Article
        fields = ['author', 'title', 'text', 'image_file']
