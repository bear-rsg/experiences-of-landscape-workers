from rest_framework import routers
from . import api

# Build a router using rest_framework
router = routers.DefaultRouter()
router.register('api/journalentry', api.JournalEntryViewSet, 'api-journalentry')

# Use router to set Django URL patterns
urlpatterns = router.urls