import pytest

from django.contrib.auth.models import User
from users.models import BlogUser


@pytest.fixture()
def user_1(db):
    user = User.objects.create_user("test-user")
    return user


def test_user_create(user_1):
    """
    Test user create works, as well as testing if a bloguser instance is created when a User is created.
    """
    user_1.set_password("new-password")
    blogger = BlogUser.objects.all().count()
    assert blogger == 1
    assert user_1.check_password("new-password") is True
    assert user_1.username == "test-user"