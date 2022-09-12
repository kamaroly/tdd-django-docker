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
    
@pytest.mark.django_db
def test_get_single_movie(client, add_movie):
    
    movie = add_movie(title="The Book Of Eli", genre= "Biography", year="2009")
    response = client.get(f"/api/movies/{movie.id}/")
    
    assert response.status_code == 200
    assert response.data["title"] == "The Book Of Eli"

def test_get_movie_incorrect_id(client):
    response = client.get(f"/api/movies/foo/")
    assert response.status_code == 404

@pytest.mark.django_db
def test_get_all_movies(client, add_movie):
    movie_one= add_movie(title="The Book Of Eli", genre="True Movie", year="2019")
    movie_two= add_movie(title="Never Split the difference", genre="Biograph", year="2018")
    
    response = client.get(f"/api/movies/")
    
    assert response.status_code == 200
    assert response.data[0]["title"] == movie_one.title
    assert response.data[1]["title"] == movie_two.title
