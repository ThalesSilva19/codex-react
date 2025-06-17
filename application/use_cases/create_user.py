from application.ports.use_case import UseCase
from domain.models.user import UserCreate, User


class CreateUserUseCase(UseCase[UserCreate, User]):
    def execute(self, data: UserCreate) -> User:
        # In a real scenario we would persist the user using a repository.
        return User(email=data.email, password=data.password)
