from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from rest_framework import status
from xml_converter.services import convert_file


class ConverterViewSet(ViewSet):
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        file_name = list(request.FILES)[0]
        xml_content = request.FILES[file_name]

        converted_file = convert_file(xml_content)

        if not type(converted_file) is dict:
            return JsonResponse({'error': converted_file}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return JsonResponse(converted_file, status=status.HTTP_200_OK)
