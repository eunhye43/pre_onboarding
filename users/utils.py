import jwt

from django.http   import JsonResponse

from my_settings   import SECRET_KEY, ALGORITHM
from users.models  import User

def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None) # http header에 있는 토큰 받기
            payload      = jwt.decode(access_token, SECRET_KEY, algorithm=ALGORITHM) # 토큰 복호화
            user         = User.objects.get(id=payload['id']) # payload에 있는 유저와 확인 후 변수에 저장
            request.user = user
        
        except jwt.DecodeError:
            return JsonResponse({'Message': 'Invalid_Token'}, status=401) # 인증이 안돼서 자원을 이용할 수 없는 상태 = 미인증 상태

        except User.DoesNotExist:
            return JsonResponse({'Message': 'Invalid_User'}, status=404) # not found
        
        return func(self, request, *args, **kwargs)
    return wrapper