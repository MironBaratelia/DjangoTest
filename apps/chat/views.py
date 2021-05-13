from django.contrib.auth import *
from django.urls import reverse

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from apps.chat.forms import ConversationForm
from apps.chat.models import *
from apps.accounts.forms import *

def index_view(request):
    print(request.user)
    context = {
        'sections': Section.objects.all(),
    }
    response = render(request, 'chat/index.html', context=context)
    response.set_cookie('color', 'black', max_age=30)
    return response

class SectionView(TemplateView):

    template_name = 'chat/section.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        section_id = kwargs.get('section_id')
        conversations = Conversation.objects.filter(section_id=section_id)
        conversation_id = self.request.GET.get('conversation')
        if conversation_id:
            messages = Message.objects.filter(conversation=conversation_id)
        else:
            messages = []
        conversation_form = kwargs.get('conversation_form', ConversationForm())

        context.update({
            'section_id': section_id,
            'conversation_id': conversation_id,
            'conversations': conversations,
            'messages': messages,
            'conversation_form': conversation_form,
        })
        return context

    def post(self, request, *args, **kwargs):
        user = self.request.user
        section_id = kwargs.get('section_id')
        conversation_id = self.request.GET.get('conversation')

        form_type = request.POST.get('form')
        if form_type == 'conversation':

            conversation_form = ConversationForm(request.POST)
            if user.is_anonymous:
                conversation_form.add_error(None, 'Вы не вошли в систему')
            elif conversation_form.is_valid():
                conversation = conversation_form.save(commit=False)
                conversation.section_id = section_id
                conversation.user = user
                conversation.save()

            if not conversation_form.is_valid():
                kwargs['conversation_form'] = conversation_form

        elif form_type == 'message' and conversation_id:
            message = request.POST.get('message')
            Message.objects.create(conversation_id=conversation_id, text=message, user=user)

        return self.get(request, *args, **kwargs)