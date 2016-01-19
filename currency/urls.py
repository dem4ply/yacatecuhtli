from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_nested import routers
from .views import Currency_view, Bank_view

router = routers.SimpleRouter()
router.register( r'currency', Currency_view, base_name='currency' )
router.register( r'bank', Bank_view, base_name='bank' )

urlpatterns = router.urls

urlpatterns = format_suffix_patterns( urlpatterns, suffix_required=True,
	allowed=[ 'json', 'xml' ] )
