from fastapi import APIRouter
from externals.ports.router import Router
from application.controllers.create_user_controller import CreateUserController
from domain.models.user import UserCreate, User
from witch_doctor import WitchDoctor


class UserRouter(Router):
    def __init__(self, controller: CreateUserController):
        self._router = APIRouter()
        self.controller = controller
        self._router.post("/users")(self.create_user)

    @property
    def router(self) -> APIRouter:
        return self._router

    @WitchDoctor.injection
    async def create_user(self, data: UserCreate) -> User:
        return self.controller.handle(data)
