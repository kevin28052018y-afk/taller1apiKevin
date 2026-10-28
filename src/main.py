from fastapi import FastAPI, HTTPException, status

from src.controllers import (
    create_trainee,
    delete_trainee,
    get_all_trainees,
    get_trainee_by_id,
    update_trainee,
)
from src.models.model import TraineeModel, TraineeUpdateModel

app = FastAPI(
    title="Gestión de datos de los aprendices",
    description="API simple con FastAPI para gestionar los datos de los aprendices",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message": "Hello API "}

@app.post("/trainees", response_description="Registrar un nuevo aprendiz", status_code=status.HTTP_201_CREATED)
def create_trainee_route(trainee: TraineeModel):
    return create_trainee(trainee)

@app.get("/trainees", response_description="Obtener todos los aprendices")
def get_trainees_route():
    return get_all_trainees()


@app.get("/trainees/{trainee_id}", response_description="Obtener un aprendiz por su ID")
def get_trainee_route(trainee_id: str):
    trainee = get_trainee_by_id(trainee_id)
    if trainee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aprendiz no encontrado",
        )
    return trainee

@app.put("/trainees/{trainee_id}", response_description="Actualizar un aprendiz existente")
def update_trainee_route(trainee_id: str, data: TraineeUpdateModel):
    trainee = update_trainee(trainee_id, data)
    if trainee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aprendiz no encontrado o sin datos para actualizar",
        )
    return trainee

@app.delete("/trainees/{trainee_id}", response_description="Eliminar un aprendiz existente")
def delete_trainee_route(trainee_id: str):
    if not delete_trainee(trainee_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aprendiz no encontrado",
        )
    return {"message": "Aprendiz eliminado correctamente"}