from django import forms
from models import MovementRequest


class MovementRequestForm(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = MovementRequest
        fields = ('uid','robot_to_send',
                    'joint_1','joint_2','joint_3',
                    'joint_4','joint_5','joint_6',)
