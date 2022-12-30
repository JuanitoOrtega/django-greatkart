from django.forms import ModelForm, TextInput
from store.models import ReviewRating


class ReviewRatingForm(ModelForm):
    
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
        widgets = {
            'subject': TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }