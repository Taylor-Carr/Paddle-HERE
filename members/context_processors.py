from members.models import UserProfile

def profile_picture(request):
    profile = None
    if request.user.is_authenticated:
        profile = UserProfile.objects.filter(user=request.user).first()  
    return {'profile': profile}


