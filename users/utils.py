import jwt

from django.http   import JsonResponse

from my_settings   import SECRET_KEY, ALGORITHM
from users.models  import User

def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
            user         = User.objects.get(id=payload['id'])
        
            request.user = user
        
        except jwt.DecodeError:
            return JsonResponse({'Message': 'Invalid_Token'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'Message': 'Invalid_User'}, status=404)
        
        return func(self, request, *args, **kwargs)
    return wrapper