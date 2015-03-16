from django import forms
from library.models import Author, Book


class AuthorForm(forms.ModelForm):

    first_name = forms.CharField(max_length=128, help_text="First Name")
    last_name = forms.CharField(max_length=128, help_text="Last Name")
    birth = forms.DateTimeField()
    wiki = forms.URLField()

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Author
        fields = ('first_name', 'last_name', 'birth', 'wiki')


class BookForm(forms.ModelForm):

    title = forms.CharField(max_length=128, help_text="Book Title")
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label='author', required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Book
        fields = ('title', 'author')
        exclude = ('slug',)
