from django import forms

from online_library.books.models import Book


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description'
                }
            ),

            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image'
                }
            ),

            'book_type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..'
                }
            ),
        }


class BookCreateForm(BookBaseForm):
    pass


class BookEditForm(BookBaseForm):
    pass
