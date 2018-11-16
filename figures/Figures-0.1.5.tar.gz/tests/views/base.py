
import pytest

from django.contrib.auth import get_user_model

from rest_framework.test import (
    APIRequestFactory,
    #RequestsClient, Not supported in older  rest_framework versions
    force_authenticate,
    )

from tests.views.helpers import create_test_users

@pytest.mark.django_db
class BaseViewTest(object):

    request_path = '/'
    view_class = None

    get_action = dict(get='list')

    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.callers = create_test_users()


    @pytest.mark.skip()
    @pytest.mark.parametrize('username, status_code', [
        ('regular_user', 403),
        ('staff_user', 200),
        ('super_user', 200),
        ('superstaff_user', 200),
    ])
    def test_get_authentication(self, username, status_code):
        '''
        Provides authentication testing
        Tests in the inherited classes provide for testing results

        Currently expect the view_class to be derived from the
        Django Rest Framework ViewSetMixin class. This requires
        the action in the 'as_view' call
        '''
        request = APIRequestFactory().get(self.request_path)
        user = get_user_model().objects.get(username=username)
        force_authenticate(request, user=user)

        # This is a (temporary we hope) hack to support views
        # that can be derived from either APIView or ViewSetMixin
        if self.get_action:
            view = self.view_class.as_view(self.get_action)
        else:
            view = self.view_class.as_view()
        response = view(request)
        assert response.status_code == status_code

    @property
    def staff_user(self):
        return get_user_model().objects.get(username='staff_user')
