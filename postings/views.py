import json

from datetime import date

from django.db.models import Q
from django.db.models import Count
from django.http      import JsonResponse
from django.views     import View

from .models      import Posting
from users.models import User
from users.utils  import login_required

class PostingDetailView(View):
    @login_required
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            
            Posting.objects.create(
                user_id    = user.id,
                title      = data['title'],
                content    = data['content']
                )
            return JsonResponse({'Message': 'Success!'}, status=201)
        
        except KeyError:
            return JsonResponse({'Message': 'Key_Error'}, status=400)

    def get(self, request, posting_id):
        try:
            posting = Posting.objects.get(id=posting_id)
            posting_info = {
                "user_id"          : posting.user.id,
                "user_name"        : posting.user.name,
                "posting_id"       : posting.id,
                "posting_title"    : posting.title,
                "posting_content"  : posting.content,
                "created_at"       : posting.created_at,
                "updated_at"       : posting.updated_at
                }

            return JsonResponse({'Message': posting_info}, status=200)

        except Posting.DoesNotExist:
            return JsonResponse({'Message': 'Does_Not_Exist_Error'}, status=400)
    
    @login_required
    def patch(self, request, posting_id):
        try:
            user    = request.user
            title   = request.GET.get('title')
            content = request.GET.get('content')

            selected_posting = Posting.objects.get(id=posting_id)
            
            if not user == selected_posting.user:
                return JsonResponse({'Message': 'Unauthorized_User'}, status=401)

            selected_posting.title   = title if title else selected_posting.title
            selected_posting.content = content if content else selected_posting.content
            selected_posting.save()
        
            return JsonResponse({'Message': 'Success!'}, status=201)
        
        except Posting.DoesNotExist:
            return JsonResponse({'Message': 'Not_Existed_Error'}, status=400)

        except KeyError:
            return JsonResponse({'Message': 'Key_Error'}, status=400)
            
    @login_required
    def delete(self, request, posting_id):
        try:
            user             = request.user
            selected_posting = Posting.objects.get(id=posting_id)

            if not user == selected_posting.user:
                return JsonResponse({'Message': 'Unauthorized_User'}, status=401)
            
            selected_posting.delete()

            return JsonResponse({'Message': 'Success!'}, status=200)
        
        except Posting.DoesNotExist:
            return JsonResponse({'Message': 'Not_Existed_Error'}, status=400)

class PostinglistView(View):
    def get(self, request):
        pagination        = int(request.GET.get('pagination', 0))
        limit             = int(request.GET.get('limit', 3))
        offset            = pagination * 3
        
        posts = Posting.objects.all()[offset:offset+limit]
        post_title_info = [
            {   
                "posting_id"       : post.id,
                "posting_title"    : post.title,
            } 
            for post in posts]

        return JsonResponse({'Message': post_title_info}, status=200)