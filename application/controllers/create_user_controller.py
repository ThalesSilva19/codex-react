from application.ports.controller import Controller
from application.use_cases.create_user import CreateUserUseCase
from adapters.ports.presenter import Presenter
from domain.models.user import UserCreate, User


class CreateUserController(Controller):
    def __init__(self, use_case: CreateUserUseCase, presenter: Presenter):
        self.use_case = use_case
        self.presenter = presenter

    def handle(self, data: UserCreate) -> User:
        result = self.use_case.execute(data)
        return self.presenter.present(result)
