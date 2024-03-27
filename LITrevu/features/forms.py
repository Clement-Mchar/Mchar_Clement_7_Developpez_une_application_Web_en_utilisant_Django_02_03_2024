from django import forms
from .models import Review, Ticket

RATINGS = (
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"), 
)

class TicketForm(forms.ModelForm):
    image=forms.ImageField(max_length=63,
        widget=forms.FileInput(
            attrs={"class": "ticket-image-update"}
        ), required=False )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = Ticket
        exclude = ("user",)


class ReviewForm(forms.ModelForm):
    rating=forms.TypedMultipleChoiceField(widget=forms.RadioSelect(attrs={"class": "checkbox"}), choices= RATINGS)

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
