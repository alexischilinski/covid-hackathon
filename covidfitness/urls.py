from rest_framework import routers
from .api import ChallengeViewSet, AUTHUserChallengeViewSet, UserChallengeViewSet, AUTHCompletedChallengeViewSet, CompletedChallengeViewSet

router = routers.DefaultRouter()
router.register('api/challenges', ChallengeViewSet, 'challenges')
router.register('api/authuserchallenges', AUTHUserChallengeViewSet, 'authuserchallenges')
router.register('api/userchallenges', UserChallengeViewSet, 'userchallenges')
router.register('api/authcompletedchallenges', AUTHCompletedChallengeViewSet, 'authcompletedchallenges')
router.register('api/completedchallenges', CompletedChallengeViewSet, 'completedchallenges')

urlpatterns = router.urls