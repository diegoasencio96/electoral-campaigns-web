from django import forms
from .models import TypeMeeting, Meeting


class MeetingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)  # populates the post
        self.fields['type_activity'].queryset = TypeMeeting.objects.filter(campaign=self.current_user.campaign)

    class Meta:
        model = Meeting
        fields = '__all__'
