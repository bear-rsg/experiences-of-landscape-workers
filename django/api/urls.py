from rest_framework import routers
from . import api

# Build a router using rest_framework
router = routers.DefaultRouter()
# Project
router.register('project', api.ProjectViewSet, 'api-project')
# Journal Entry Tag
router.register('journalentrytag', api.JournalEntryTagViewSet, 'api-journalentrytag')
# Journal Entry
router.register('journalentry', api.JournalEntryViewSet, 'api-journalentry')
# Journal Entry Image
router.register('journalentryimage', api.JournalEntryImageViewSet, 'api-journalentryimage')
# Journal Entry Analysis Code
router.register('journalentryanalysiscode', api.JournalEntryAnalysisCodeViewSet, 'api-journalentryanalysiscode')
# Journal Entry Analysis
router.register('journalentryanalysis', api.JournalEntryAnalysisViewSet, 'api-journalentryanalysis')


# Use router to set Django URL patterns
urlpatterns = router.urls
