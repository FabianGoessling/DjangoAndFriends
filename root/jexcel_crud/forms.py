from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import inlineformset_factory

from .models import Book, Site


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'value')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-control'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.disable_csrf = True
        super(BookForm, self).__init__(*args, **kwargs)



def SiteSet(extra):
    return inlineformset_factory(parent_model=Book,
                                model=Site,
                                extra=extra,
                                fields=('page',),
                                can_delete=False,
                                )

class sitesetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_tag = False
        self.form_class = 'form-row'
        self.render_required_fields = True
        #self.add_input(Submit('submit', 'Submit'))
        self.disable_csrf = True