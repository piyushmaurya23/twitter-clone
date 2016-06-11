from django.core.urlresolvers import reverse,reverse_lazy
from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from rest_framework.generics import ListCreateAPIView

from .models import Tweet
from .serializers import TweetSerializer


# Create your views here.


class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    fields = [
        'content',
        'image',
    ]

    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)


class TweetListView(LoginRequiredMixin, ListView):
    model = Tweet
    queryset = Tweet.objects.all()


class TweetUpdateView(LoginRequiredMixin, UpdateView):
    model = Tweet
    fields = [
        'content',
        'image',
    ]

    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetUpdateView, self).form_valid(form)


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy('users:detail')

    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class TweetDetailView(LoginRequiredMixin, DetailView):
    model = Tweet


class TweetAPIView(ListCreateAPIView):
    model = Tweet
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

