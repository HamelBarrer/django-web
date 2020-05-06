from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

from .models import Comment

from .forms import CommentForm, UserForm

from users.models import User


class IndexView(View):
    model = Comment
    template_name = 'home/index.html'
    form_class = CommentForm

    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')

    def get_context_data(self, **kwargs):
        context = {}
        context['commentaries'] = self.get_queryset()
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
