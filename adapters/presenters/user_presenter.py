from adapters.ports.presenter import Presenter
from domain.models.user import User


class UserPresenter(Presenter):
    def present(self, data: User) -> User:
        # In a real application you might serialize or transform the output
        return data
