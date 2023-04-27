from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, get_code, get_token


class NoPutRouter(DefaultRouter):
    """
    Роутер отключает метод "Put".
    """
    def get_method_map(self, viewset, method_map):
        bound_methods = super().get_method_map(viewset, method_map)
        if 'put' in bound_methods.keys():
            del bound_methods['put']
        return bound_methods


router = NoPutRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', get_token),
    path('v1/auth/signup/', get_code),
]
