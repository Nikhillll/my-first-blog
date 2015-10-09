from django import forms
from models import Artical

class ArticleForm(forms.ModelForm):
	
	class Meta:
		model = Artical
		fields =  {'title','body','pub_date','hero_image','optional_image'}
		#fields = '__all__'
'''class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = {'name','body'}
'''