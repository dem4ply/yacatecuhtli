from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_nested import routers
from .views import Person_view

router = routers.SimpleRouter()
router.register( r'person', Person_view, base_name='person' )

#contact_router = routers.NestedSimpleRouter( router, r'whatsapp',
#	lookup='whatsapp' )

#contact_router.register( r'contact', views.Contact_view,
#	base_name='contact' )

urlpatterns = router.urls
#urlpatterns += contact_router.urls
#urlpatterns += send_message_router.urls

print(urlpatterns)

#urlpatterns = format_suffix_patterns( urlpatterns, suffix_required=True,
#	allowed=[ 'json', 'xml' ] )