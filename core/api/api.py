from tastypie.api import Api
from resources import PostResource

v1 = Api("v1")
v1.register(PostResource())

