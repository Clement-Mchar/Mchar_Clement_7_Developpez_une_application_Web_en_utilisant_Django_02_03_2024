from django import forms
from .models import Review, Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ("user",)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = (
            "ticket",
            "user",
        )


class ReviewResponse(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
