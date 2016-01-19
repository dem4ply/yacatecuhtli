from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_nested import routers
from .views import Item_view, Category_view

router = routers.SimpleRouter()
router.register( r'item', Item_view, base_name='item' )
router.register( r'category', Category_view, base_name='category' )

item_router = routers.NestedSimpleRouter( router, r'category',
	lookup='category' )
item_router.register( r'item', Item_view,
	base_name='category_item' )

urlpatterns = router.urls + item_router.urls

urlpatterns = format_suffix_patterns( urlpatterns, suffix_required=True,
	allowed=[ 'json', 'xml' ] )
