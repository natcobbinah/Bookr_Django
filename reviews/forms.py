from django import forms
from .models import Publisher, Review, Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

SEARCH_IN_CHOICES = (
    ("title", "Title"),
    ("contributor", "Contributor")
)


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(
        required=False,
        choices=SEARCH_IN_CHOICES
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.add_input(Submit("", "Search"))


class InstanceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        if kwargs.get("instance"):
            button_title = "Save"
        else:
            button_title = "Create"
        self.helper.add_input(Submit('', button_title))


class PublisherForm(InstanceForm):
    class Meta:
        model = Publisher
        fields = "__all__"


class ReviewForm(InstanceForm):
    class Meta:
        model = Review
        exclude = ("date_edited", "book")

    rating = forms.IntegerField(min_value=0, max_value=5)


class BookMediaForm(InstanceForm):
    class Meta:
        model = Book
        fields = ["cover", "sample"]
