from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError

from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "featured_image",
            "description",
            "demo_link",
            "source_link",
            "tags",
        ]
        widgets = {"tags": forms.CheckboxSelectMultiple}

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for k, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

        # self.fields["title"].widget.attrs.update(
        #     {"class": "input", "placeholder": "Add title"}
        # )
        # self.fields["description"].widget.attrs.update(
        #     {"class": "input", "placeholder": "Add description"}
        # )
        # self.fields["demo_link"].widget.attrs.update(
        #     {"class": "input", "placeholder": "Add demo link"}
        # )
        # self.fields["source_link"].widget.attrs.update(
        #     {"class": "input", "placeholder": "Add source link"}
        # )

    # делаем чтобы можно было выбрать не больше 3 тага
    # def clean_tags(self):
    #     value = self.cleaned_data["tags"]
    #     if len(value) > 3:
    #         raise ValidationError("You can't select more than 3 items.")
    #     # Always return a value to use as the new cleaned data, even if
    #     # this method didn't change it.
    #     return value


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            "value",
            "body",
        ]
        labels = {
            "value": "Place your vote",
            "body": "Add a comment with you vote",
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for k, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
