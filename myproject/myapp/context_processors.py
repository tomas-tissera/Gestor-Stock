# myapp/context_processors.py

def user_role(request):
    if request.user.is_authenticated:
        # Verifica el rol del usuario
        if request.user.groups.filter(name='Encargado').exists():
            return {'role': 'Encargado'}
        elif request.user.groups.filter(name='Empleados').exists():
            return {'role': 'Empleados'}
        else:
            return {'role': 'Invitado'}
    return {'role': 'Invitado'}
