from django.shortcuts import render
from django.views import View
# importamos la libreria generic
from .models import *


# Create your views here.
class IndexView(View):
    def get(self, request):
        listaAlumnos = TblAlumno.objects.all()
        return render(request, 'index.html', {'alumnos': listaAlumnos})


class CursosView(View):
    def get(self, request):
        listaCursos = TblCurso.objects.all()
        return render(request, 'cursos.html', {'cursos': listaCursos})
