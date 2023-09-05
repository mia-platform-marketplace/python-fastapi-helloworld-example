from fastapi import APIRouter, Request, status

from src.schemas.message_schema import MessageResponseSchema


router = APIRouter()


@router.get(
    "/",
    response_model=MessageResponseSchema,
    status_code=status.HTTP_200_OK,
    tags=["python-fastapi-template"]
)
async def hello_world(request: Request):
    """
    Say Hello
    """

    logger = request.state.logger
    logger.debug('Test logger from hello world endpoint')

    return {"message": "Hello World!"}
