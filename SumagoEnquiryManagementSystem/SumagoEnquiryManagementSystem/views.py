from django.shortcuts import redirect

def department_index(request):
    return redirect('{}_department:index'.format(str(request.user.userextrainfo.department).lower()))
