from fastapi import FastAPI
from witch_doctor import WitchDoctor, InjectionType

from adapters.ports.presenter import Presenter
from adapters.presenters.user_presenter import UserPresenter
from application.ports.use_case import UseCase
from application.use_cases.create_user import CreateUserUseCase
from application.ports.controller import Controller
from application.controllers.create_user_controller import CreateUserController
from externals.ports.router import Router
from externals.fastapi.routers.user_router import UserRouter

app = FastAPI()

# Register dependencies
WitchDoctor.register(Presenter, UserPresenter, InjectionType.SINGLETON)
WitchDoctor.register(UseCase, CreateUserUseCase, InjectionType.SINGLETON)
WitchDoctor.register(
    Controller,
    CreateUserController,
    InjectionType.SINGLETON,
    args=[WitchDoctor.resolve(UseCase), WitchDoctor.resolve(Presenter)],
)
WitchDoctor.register(
    Router,
    UserRouter,
    InjectionType.SINGLETON,
    args=[WitchDoctor.resolve(Controller)],
)

user_router = WitchDoctor.resolve(Router).router
app.include_router(user_router)


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


def main():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
