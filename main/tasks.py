from celery import shared_task
import pandas as pd
from main.models import Movie

@shared_task
def importMovies(arq_path):
    # Leitura do arquivo Excel com Pandas
    df = pd.read_excel(arq_path)
    # Iteração sobre as linhas e criação de objetos Filme
    for _, row in df.iterrows():
        new_movie = Movie.objects.create(
            title=row['titulo'],
            watched_date=row['data_assistida'],
            gender=row['genero'],
            wish_list=row['quero_assistir']
        )

        new_movie.save()