from django.http import JsonResponse

def bad_request(error):
    return JsonResponse({"error":error}, status=400)

def bad_method(error="Bad method"):
    return JsonResponse({"error":error}, status=405)