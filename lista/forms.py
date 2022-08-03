from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from lista.models import Review

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class VoteForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


