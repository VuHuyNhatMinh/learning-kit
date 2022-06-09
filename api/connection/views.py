from pydoc import cli
from django.core.exceptions import BadRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
import json

from .mqtt import Client


@api_view(['POST'])
def test(request:Request, *args, **kwargs):
    print(request.data)  
    context = request.data

    if context.get('mail', '') != '':
        client = Client()
        client.publish(json.dumps(context))
        return Response(200)  

    raise BadRequest('Invalid request.')
