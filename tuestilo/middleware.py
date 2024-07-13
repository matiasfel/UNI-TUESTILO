from django.shortcuts import redirect

class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/accounts/login/' and request.user.is_authenticated:
            return redirect('base')  # Cambia 'base' por el nombre de la vista a la que quieras redirigir
        response = self.get_response(request)
        return response
