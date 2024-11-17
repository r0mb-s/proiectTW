# In your app's pipeline.py or any accessible file
def save_google_profile(backend, user, response, *args, **kwargs):
    """Populate the user model with Google data."""
    if backend.name == 'google-oauth2':
        user.google_id = response.get('sub')  # Google user ID
        user.google_picture_url = response.get('picture')  # Profile picture
        user.save()
