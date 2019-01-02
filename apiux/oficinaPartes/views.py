from material.frontend.views import ModelViewSet
from . import models

# Create your views here.
class MyModelViewSet(ModelViewSet):
    model = models.MyModel

class EmpleadoListView(ModelViewSet.detail_view):
    model = models.Empleado