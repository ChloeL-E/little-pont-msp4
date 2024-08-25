from django import forms

class DateInput(forms.DateInput):
    input_type = 'text'
    template_name = 'django/forms/widgets/date.html'

    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'datepicker'}
        super().__init__(*args, **kwargs)


class TimeInput(forms.TimeInput):
    input_type = 'text'
    template_name = 'django/forms/widgets/time.html'

    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'timepicker'}
        super().__init__(*args, **kwargs)