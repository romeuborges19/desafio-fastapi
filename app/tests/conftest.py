from redis_om import Migrator

from app.models.user_model import User
from app.schemas.user_schema import UserAuthentication
from app.services.cache_service import cache
from app.services.user_service import UserService
from app.core.config import settings


# Estas funções garantem que um usuário de testes seja criado e deletado
# junto com seus dados relacionados na instância de cache

def pytest_sessionstart(session):
    Migrator().run()
    user_auth = UserAuthentication(
        username=f"errado_essa_bosta{settings.TEST_USERNAME}",
        email=settings.TEST_EMAIL,
        password=settings.TEST_PASSWORD
    )

    UserService.create_user_not_async(user_auth)

def pytest_sessionfinish(session):
    user = UserService.get_user_by_email_not_async(settings.TEST_EMAIL)

    if user:
        cache.rd.delete(user.pk)
        User.Meta.database.delete(f":app.models.user_model.User:{user.pk}")