from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm
from django.templatetags.static import static

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to MySQL
            return redirect('success_page')  # Redirect after successful save
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def movie_detail(request, movie_id):
    movies = [
        {'id': 1, 'title': 'Movie 1', 'src': static('images/POSTER1.png')},
        {'id': 2, 'title': 'Movie 2', 'src': static('images/POSTER2.png')},
        {'id': 3, 'title': 'Movie 3', 'src': static('images/POSTER3.png')},
        {'id': 4, 'title': 'Movie 4', 'src': static('images/POSTER4.png')},
        {'id': 5, 'title': 'Movie 5', 'src': static('images/POSTER5.png')},
        {'id': 6, 'title': 'Movie 6', 'src': static('images/POSTER6.png')},
    ]
    
    movie = next((m for m in movies if m['id'] == movie_id), None)
    
    if movie is None:
        return render(request, '404.html', status=404)
    
    return render(request, 'movie_detail.html', {'movie': movie})

def coming_soon_detail(request, id):
    coming_soon = {
        1: {'title': 'Coming Soon 1', 'description': 'Details about Coming Soon 1'},
        2: {'title': 'Coming Soon 2', 'description': 'Details about Coming Soon 2'},
    }
    
    coming_soon_info = coming_soon.get(id, {'title': 'Not Found', 'description': 'No details available'})
    
    return render(request, 'coming_soon_detail.html', {'coming_soon': coming_soon_info})

def celebrity_detail(request, id):
    celebrities = [
        {'id': 1, 'name': 'Celebrity 1', 'bio': 'Details about Celebrity 1', 'image': static('images/celeb1.png')},
        {'id': 2, 'name': 'Celebrity 2', 'bio': 'Details about Celebrity 2', 'image': static('images/celeb2.png')},
        {'id': 3, 'name': 'Celebrity 3', 'bio': 'Details about Celebrity 3', 'image': static('images/celeb3.png')},
        {'id': 4, 'name': 'Celebrity 4', 'bio': 'Details about Celebrity 4', 'image': static('images/celeb4.png')},
    ]
    
    celebrity = next((c for c in celebrities if c['id'] == id), None)

    if celebrity is None:
        return render(request, '404.html', status=404)

    return render(request, 'celebrity_detail.html', {'celebrity': celebrity})

def news_detail(request, id):
    news = {
        1: {'title': 'News 1', 'summary': 'Summary of News 1'},
        2: {'title': 'News 2', 'summary': 'Summary of News 2'},
    }
    
    news_info = news.get(id, {'title': 'Not Found', 'summary': 'No details available'})
    
    return render(request, 'news_detail.html', {'news': news_info})
