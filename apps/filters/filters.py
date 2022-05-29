import django_filters
from apps.userprofile.models import Profile


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        exclude = ['profile_image']
        fields = ['usernickname', 'interests', 'gender',]

