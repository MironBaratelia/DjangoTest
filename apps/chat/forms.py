from django import forms
from apps.chat.models import Section, Conversation, Message


class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ('text',)

    # def clean(self):
    #     text = self.cleaned_data['text']
    #     text = text.replace('привет', '***') #замена привет на ***
    #     return text


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)