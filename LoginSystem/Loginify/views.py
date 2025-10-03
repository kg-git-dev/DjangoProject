from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetails
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def home_view(request):
  """
  A simple view that returns "Hello World" for testing purposes.
  """
  return HttpResponse("Hello, world!")

def signup(request):
    """
    Handles user registration.
    - Renders the signup form.
    - Processes POST requests to create a new user.
    - Redirects to the login page on success.
    - Handles existing email errors.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not all([username, email, password]):
            return render(request, 'signup.html', {'error': 'All fields are required.'})

        try:
            # Hash the password before saving it to the database
            hashed_password = make_password(password)
            new_user = UserDetails.objects.create(
                Username=username,
                Email=email,
                Password=hashed_password 
            )
            new_user.save()
            # Redirect to the login page upon successful signup
            return redirect('login')
        except IntegrityError:
            # This will be triggered by the unique=True on the Email field
            return render(request, 'signup.html', {'error': 'An account with this email already exists.'})

    return render(request, 'signup.html')


def login(request):
    """
    Handles user login.
    - Renders the login form.
    - Processes POST requests to authenticate a user.
    - Renders a success page on successful login.
    - Shows an error for invalid credentials.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not all([email, password]):
            return render(request, 'login.html', {'error': 'Email and password are required.'})

        try:
            user = UserDetails.objects.get(Email=email)
            
            # Use check_password to compare the plain password with the stored hash.
            if check_password(password, user.Password):
                return render(request, 'login_success.html', {'username': user.Username})
            else:
                raise UserDetails.DoesNotExist
        except UserDetails.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials. Please try again.'})

    return render(request, 'login.html')
