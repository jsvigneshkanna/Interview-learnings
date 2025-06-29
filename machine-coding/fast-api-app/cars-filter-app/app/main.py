from fastapi import FastAPI
import uvicorn
from app.controllers.fetch_controller import router as car_routers

app = FastAPI(title='car fetcher', description='fetch cars with different filters')

app.include_router(car_routers, prefix='', tags=['cars'])

if __name__=='__main__':
    uvicorn.run('app.main:app', host='0.0.0.0', port=8080, reload=True)