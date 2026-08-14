import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise # Import WhiteNoise directly

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 1. Initialize the base Django application instance
base_application = get_wsgi_application()

# 2. Wrap the application inside WhiteNoise so it handles all static URLs natively
application = WhiteNoise(base_application, root=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'))

# 3. Expose the app hook mapping for the Vercel platform container
app = application
