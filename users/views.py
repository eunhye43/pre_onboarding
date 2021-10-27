import json
import bcrypt
import jwt
import re

from django.views         import View
from django.http          import JsonResponse
from json.decoder         import JSONDecodeError

from users.models import User
from my_settings  import SECRET_KEY, ALGORITHM

class SignUpView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            name         = data['name']
            password     = data['password']
            email        = data['email']
            
            email_validation    = re.compile('^[a-z0-9]+@[a-z0-9]+\.[a-z0-9.]+$', re.I)
            password_validation = re.compile('^(?=.*[a-z])(?=.*[0-9]).{8,}', re.I)

            if not email_validation.match(email):
                return JsonResponse({'Message': 'Invalid_Email'}, status=400)

            if not password_validation.match(password):
                return JsonResponse({'Message': 'Invalid_Password'}, status=400)
            
            hashed_password= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name         = name,
                password     = hashed_password,
                email        = email
                )

            return JsonResponse({'Message': 'Success'}, status = 201)

        except KeyError:
            return JsonResponse({'Message': 'Key_Error'}, status = 400)

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(email=data['email'])
            hashed_password = user.password.encode('utf-8')

            if not bcrypt.checkpw(data['password'].encode('utf-8'), hashed_password):
                return JsonResponse({'Message': 'Invalid_User'}, status=401)
            
            Access_Token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm = ALGORITHM)

            return JsonResponse({'Access_Token': Access_Token}, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({'Message': 'Decode_Error'}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({'Message': 'Not_Found_Error'}, status=404)
        
        except KeyError:
            return JsonResponse({'Message': 'Key_Error'}, status=400)