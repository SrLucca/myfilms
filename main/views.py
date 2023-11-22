import os
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.db.models import Count
from datetime import date
from myfilms.settings import BASE_DIR

from .tasks import importMovies
import time

# Create your views here.

def homeView(request):

    #Request de cadastro de filme
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MovieForm()

    #Captação dos dados para criacao do chart
    movies = Movie.objects.all()
    watched_count = Movie.objects.filter(wish_list=False, watched_date__isnull=False).count()
    wish_list_count = Movie.objects.filter(wish_list=True).count()

    context = {
        'movies':movies,
        'form':form,
        'watched_count': watched_count,
        'wish_list_count': wish_list_count,
    }
    return render(request, 'pages/index.html', context)

def editMovie(request, id):
    #Marcar filme como assistido
    movie = Movie.objects.get(id=id)
    movie.wish_list = False

    #Definir data de assistido para hoje
    movie.watched_date = date.today()
    movie.save()
    return redirect('/')

def importSheet(request):
    if request.method == 'POST':
        arquivo = request.FILES.get('sheet')
        if arquivo:
            # Salve o arquivo temporariamente
            temporary_directory = os.path.join(BASE_DIR, 'planilhas')
            if not os.path.exists(temporary_directory):
                os.makedirs(temporary_directory)

            # Especifique um nome de arquivo para o arquivo a ser criado no diretório
            temporary_file_path = os.path.join(temporary_directory, 'temp_sheet.xlsx')
            print(temporary_file_path)
            #Passagem dos registros da planilha passada para a temporaria
            with open(temporary_file_path, 'wb+') as dest:
                for part in arquivo.chunks():
                    dest.write(part)

            # Chame a tarefa Celery
            importMovies.delay(temporary_file_path)

            time.sleep(1)
            return redirect('/')
