from django.views.generic import DetailView, TemplateView, UpdateView, ListView

from django.contrib.auth.models import User

from profiles.models import Profile
from utils import requires_login

class TestView(TemplateView):
    template_name = "test.html"

class ProfileViewMixin(object):
    context_object_name = "profile"
    model = Profile

class ProfileListView(ProfileViewMixin, ListView):
    pass

class ProfileDetailView(ProfileViewMixin, DetailView):
    template_name = "profiles/profile.html"

@requires_login
class ProfileUpdateView(ProfileViewMixin, UpdateView):
    pass

@requires_login
class UserUpdateView(UpdateView):
    context_object_name = "profile"
    template_name = "profiles/edit.html"

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)