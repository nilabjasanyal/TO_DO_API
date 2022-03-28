

import motor.motor_asyncio
from model import Todo

client = motor.motor_asyncio.AsyncIOMotorClient()

db = client.tododb
collection = db.todo


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(title, due, desc):
    await collection.update_one({"name": title}, {"$set": {"description": desc, "due_date": due}})
    document = await collection.find_one({"name": title})
    return document


async def fetch_one_todo(title):
    document = await collection.find_one({"name": title})
    return document


async def remove_todo(title):
    await collection.delete_one({"name": title})
    return True



