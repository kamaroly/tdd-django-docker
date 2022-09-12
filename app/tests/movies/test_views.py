import json
import pytest

from movies.models import Movie

@pytest.mark.django_db 

def test_add_movie(client):
    movies = Movie.objects.all()
    assert len(movies) == 0
    
    # When
    response = client.post(
        "/api/movies/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
            "year": "1998",
        },
        content_type="application/json"
    )
    # Then
    assert response.status_code == 201
    assert response.data["title"] == "The Big Lebowski"
    
    movies = Movie.objects.all()
    assert len(movies) == 1
    
@pytest.mark.django_db
def test_add_movie_invalid_json(client):
    movies = Movie.objects.all()
    
    assert len(movies) == 0
    
    response = client.post(
        "/api/movies/",
        {},
        content_type="application/json"
    )
    
    assert response.status_code == 400 
    
    movies = Movie.objects.all()
    assert len(movies) == 0
    
@pytest.mark.django_db
def test_add_movies_invalid_json_keys(client):
    movies = Movie.objects.all()
    assert len(movies) == 0
    
    response = client.post(
        "/api/movies/",
        {
            "title": "The Book Of Eli",
            "genre": "comedy",
        },
        content_type="application/json"
    )
    
    assert response.status_code == 400
    
    movies = Movie.objects.all()
    assert len(movies) == 0
    
    
    