# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView, DeleteView

from .models import User, UserAddress
from twitter.tweets.models import Tweet


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        """
        This has been overridden to add `car` to the templates context,
        so you can use {{ car }} etc. within the template
        """
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context["address"] = UserAddress.objects.all()
        context["tweet"] = Tweet.objects.all()
        return context


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = [
        'first_name',
        'last_name',
        'about_me',
        'mobile_number',
        'profile_pic',
    ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(StaffuserRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserAddressCreateView(LoginRequiredMixin, CreateView):
    model = UserAddress
    fields = [
        'address1',
        'address2',
        'city',
        'pin_code',
    ]

    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserAddressCreateView, self).form_valid(form)


class UserAddressListView(LoginRequiredMixin, ListView):
    model = UserAddress
    queryset = UserAddress.objects.all()


class UserAddressUpdateView(LoginRequiredMixin, UpdateView):
    model = UserAddress
    fields = [
        'address1',
        'address2',
        'city',
        'pin_code',
    ]

    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserAddressUpdateView, self).form_valid(form)


class UserAddressDetailView(LoginRequiredMixin, DetailView):
    model = UserAddress


class UserAddressDeleteView(LoginRequiredMixin, DeleteView):
    model = UserAddress
    success_url = reverse_lazy('users:detail')

    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})
