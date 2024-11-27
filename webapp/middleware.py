from django.shortcuts import redirect

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            rutas_libres = ['/login/', '/register/']
            if not request.path in rutas_libres:
                return redirect('login')

        response = self.get_response(request)
        return response