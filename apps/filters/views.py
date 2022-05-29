import django_filters
from django.shortcuts import render, redirect
from apps.filters.filters import UserFilter
from apps.userprofile.models import Profile


def search(request):
    user_list = Profile.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'common/dashboard.html', {'filter': user_filter})