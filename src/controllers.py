from bson import ObjectId
from src.models.database import collection
from src.models.model import TraineeModel, TraineeUpdateModel


def helper_trainee(trainee: dict) -> dict:
    return {
        "id": str(trainee["_id"]),
        "document": trainee["document"],
        "firstname": trainee["firstname"],
        "lastname": trainee["lastname"],
        "email": trainee["email"],
        "age": trainee["age"],
        "program": trainee["program"],
        "record_number": trainee["record_number"],
    }


def create_trainee(trainee: TraineeModel):
    trainee_dict = trainee.model_dump()
    result = collection.insert_one(trainee_dict)
    new_trainee = collection.find_one({"_id": result.inserted_id})
    return helper_trainee(new_trainee)

def get_all_trainees():
    trainees = []
    for trainee in collection.find():
        trainees.append(helper_trainee(trainee))
    return trainees

def get_trainee_by_id(trainee_id: str):
    if not ObjectId.is_valid(trainee_id):
        return None

    trainee = collection.find_one({"_id": ObjectId(trainee_id)})
    if trainee:
        return helper_trainee(trainee)
    return None


def update_trainee(trainee_id: str, data: TraineeUpdateModel):
    if not ObjectId.is_valid(trainee_id):
        return None

    data_update = {
        k: v for k, v in data.model_dump().items() if v is not None
    }
    if not data_update:
        return None

    collection.update_one({"_id": ObjectId(trainee_id)}, {"$set": data_update})
    trainee_updated = collection.find_one({"_id": ObjectId(trainee_id)})
    if trainee_updated:
        return helper_trainee(trainee_updated)
    return None


def delete_trainee(trainee_id: str):
    if not ObjectId.is_valid(trainee_id):
        return False

    trainee = collection.find_one({"_id": ObjectId(trainee_id)})
    if trainee:
        collection.delete_one({"_id": ObjectId(trainee_id)})
        return True
    return False