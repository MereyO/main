#
#
# from django.shortcuts import render
# from apps.common.forms import User
# from django.shortcuts import get_object_or_404
# from django.contrib.auth.decorators import login_required
# from apps.userprofile.models import Profile
#
# # def get_user_profile(request):
# #     user = User.objects.all()
# #     return render(request, 'common/users_profile.html', {"user":user})
#
#
# @login_required
# def userprofile(request, user_id=None):
#     if user_id:
#         user = User.objects.get(id=user_id)
#         Post = Profile.objects.order_by('bio', 'gender', 'usernickname')
#         return render(request,'common/users_profile.html', {'Post':Post,'User':user})
#     else:
#         user = User.objects.get(id=user_id)
#         Post = Profile.objects.order_by('bio', 'gender', 'usernickname')
#         return render(request,'common/users_profile.html', {'Post':Post,'User':user})
