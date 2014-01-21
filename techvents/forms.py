'''
Convenience forms for adding and updating ``Event`` and ``Occurrence``s.

'''
from datetime import datetime, date, time, timedelta

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget

from dateutil import rrule
from swingtime.conf import settings as swingtime_settings
from swingtime import utils
from swingtime.models import *

class EventForm(forms.ModelForm):
    '''
    A simple form for adding and updating Event attributes

    '''

    #===========================================================================
    class Meta:
        model = UserEvent

    #---------------------------------------------------------------------------
    def __init__(self, *args, **kws):
        super(UserEvent, self).__init__(*args, **kws)
        self.fields['description'].required = False


