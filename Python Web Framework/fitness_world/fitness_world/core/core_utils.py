def user_permissions(request, user):
    if request.user.is_superuser:
        return True

    elif request.user != user:
        return False

    return True
