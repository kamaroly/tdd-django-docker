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
    
    