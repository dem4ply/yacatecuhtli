from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_nested import routers
from .views import User_view

router = routers.SimpleRouter()
router.register( r'user', User_view, base_name='user' )

urlpatterns = router.urls

urlpatterns = format_suffix_patterns( urlpatterns, suffix_required=True,
	allowed=[ 'json', 'xml' ] )
