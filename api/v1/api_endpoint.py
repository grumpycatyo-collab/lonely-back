import json
import logging as log

from fastapi import APIRouter, HTTPException, Body, status

log.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level='INFO')

router = APIRouter()

@router.get("/getApi", responses={400: {"description": "Invalid Input"}, 200: {"description": "OK"}})
def get_api():
    api_string = "Hello World"
    return api_string