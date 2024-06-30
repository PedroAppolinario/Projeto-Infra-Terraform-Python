from fastapi import FastAPI
import psycopg2 as pg

api = FastAPI()
conn = pg.connect(
    host="db",
    port="5432",
    user="postgres",
    password="postgres",
    database="postgres",
)

@api.get("/")
def index():
    return {"Hello, World!"}

