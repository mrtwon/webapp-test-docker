from uuid import UUID
from fastapi import FastAPI
import redis
from repository.repository_todo import TodoRepo
from schema import TodoSchema, CreateTodoSchema
from services import TodoService
import database.tables

app = FastAPI()


@app.get('/todos')
async def route_get_todo_list() -> list[TodoSchema]:
    todo_service = TodoService()
    result = await todo_service.get_todo_list()
    return result


@app.get('/todo/{todo_id}')
async def route_get_todo(todo_id: UUID) -> TodoSchema:
    todo_service = TodoService()
    result = await todo_service.get_todo(todo_id)
    return result


@app.post('/todo')
async def route_add_todo(schema: CreateTodoSchema) -> TodoSchema:
    todo_service = TodoService()
    result = await todo_service.add_todo(schema)
    return result


@app.get('/redis/test')
async def route_test_redis() -> str:
    r = redis.StrictRedis(host="192.168.1.18", port=6379, decode_responses=True)
    result = r.get('test')
    return 'result = ' + str(result)


@app.post('/redis/test')
async def route_test_add_redis(text: str) -> str:
    r = redis.StrictRedis(host="192.168.1.18", port=6379, decode_responses=True)
    r.set('test', text)
    return 'new value ' + text
