from fastapi import FastAPI
from controller import person_controller, location_controller, typedoc_controller

app = FastAPI()
app.include_router(person_controller.router)
app.include_router(location_controller.router)
app.include_router(typedoc_controller.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
