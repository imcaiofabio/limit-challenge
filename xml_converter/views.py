from django.http import JsonResponse
from django.shortcuts import render
from xml_converter.services import convert_file
from rest_framework import status


def upload_page(request):
    match request.method:
        case "GET":
            return render(request, "upload_page.html")
        case "POST":
            file_name = list(request.FILES)[0]
            xml_content = request.FILES[file_name]

            converted_file = convert_file(xml_content)

            if not type(converted_file) is dict:
                return JsonResponse({'error': converted_file}, content_type='application/json', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return JsonResponse(converted_file, status=status.HTTP_200_OK)
        case default:
            return JsonResponse({'error': 'Invalid HTTP method'}, content_type='application/json', status=status.HTTP_405_METHOD_NOT_ALLOWED)
