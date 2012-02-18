from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from core.models import Post

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        authorization = Authorization()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get']
