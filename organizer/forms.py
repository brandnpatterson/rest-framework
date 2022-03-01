from django.core.exceptions import ValidationError
from django.forms import CharField, ModelForm, SlugField
from django.forms.widgets import HiddenInput

from .models import NewsLink, Startup, Tag


class LowercaseNameMixin:
    """Form cleaner to lower case of name field"""

    def clean_name(self):
        """Ensure Tag name is always lowercase"""
        return self.cleaned_data["name"].lower()


class SlugCleanMixin:
    def clean_slug(self):
        slug = self.cleaned_data["slug"]
        if slug == "create":
            raise ValidationError(
                "Slug may not be 'create'."
            )
        return slug


class TagForm(LowercaseNameMixin, ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"

    def clean_name(self):
        return self.cleaned_data["name"].lower()


class StartupForm(
    LowercaseNameMixin, SlugCleanMixin, ModelForm
):
    class Meta:
        model = Startup
        fields = "__all__"


class NewsLinkForm(ModelForm):
    class Meta:
        model = NewsLink
        fields = "__all__"
        widgets = {"startup": HiddenInput()}

    def clean_slug(self):
        slug = self.cleaned_data["slug"]
        if slug in ["delete", "update", "add_article"]:
            raise ValidationError(
                f"Slug may not be '{slug}'."
            )
        return slug
