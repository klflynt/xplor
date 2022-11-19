import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from fizzbuzz.models import Fizzbuzz
from fizzbuzz.serializers import FizzbuzzSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    # """
    # # return JsonResponse({"message": "Hello there!1!"})
    # model_data = Fizzbuzz.objects.all().order_by("?").first()
    # data = {}
    # if model_data:
    #     data["id"] = model_data.id
    #     data["created_at"] = model_data.created_at
    #     data["useragent"] = model_data.useragent
    #     data["message"] = model_data.message
    #     # data = model_to_dict(model_data)
    # # return JsonResponse(data)
    # return Response(data)
    # # print(data.json())
    # """

    # instance = Fizzbuzz.objects.all().order_by("?").first()
    instance = Fizzbuzz.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = FizzbuzzSerializer(instance).data
    return Response(data)
# ||||||END = THIS WORKS - END||||