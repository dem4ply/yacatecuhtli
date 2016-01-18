from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_nested import routers
from .views import Person_view, Country_view, Address_view

router = routers.SimpleRouter()
router.register( r'person', Person_view, base_name='person' )
router.register( r'country', Country_view, base_name='country' )
router.register( r'address', Address_view, base_name='address' )

address_router = routers.NestedSimpleRouter( router, r'person',
	lookup='person' )
address_router.register( r'address', Address_view,
	base_name='person_address' )

urlpatterns = router.urls + address_router.urls

urlpatterns = format_suffix_patterns( urlpatterns, suffix_required=True,
	allowed=[ 'json', 'xml' ] )
