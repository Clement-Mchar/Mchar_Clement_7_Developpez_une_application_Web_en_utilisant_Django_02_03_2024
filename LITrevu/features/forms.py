from django import forms
from .models import Review, Ticket


class TicketForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        
    class Meta:
        model = Ticket
        exclude = ("user",)


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = Review
        exclude = (
            "ticket",
            "user",
        )


class ReviewResponse(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = Review
        fields = "__all__"
