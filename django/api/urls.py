from rest_framework import routers
from . import api

# Build a router using rest_framework
router = routers.DefaultRouter()
router.register('journalentry', api.JournalEntryViewSet, 'api-journalentry')
router.register('project', api.ProjectViewSet, 'api-project')

# Use router to set Django URL patterns
urlpatterns = router.urls