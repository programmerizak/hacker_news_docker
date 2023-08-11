from django import forms


class ItemSearchForm(forms.Form):
	query = forms.CharField(label='Search for items', max_length=100)
	# initial = "", mean default selected is All, so users must not select
	category = forms.ChoiceField(label='Category', choices=[
		('', 'All'), ('jobs', 'Jobs'), ('story', 'Story'), ('comment', 'Comment'),
		('poll','Poll')
		],required=False)
	search_in_creator = forms.BooleanField(label='Search in Creator', required=False)
	search_in_score = forms.BooleanField(label='Search in Score', required=False)


######## SIMPLE SEARCH FORM
# class ItemSearchForm(forms.Form):
#     query = forms.CharField(label='Search for items', max_length=100)
