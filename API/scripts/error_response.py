from django.http import JsonResponse

def throw_error(error):
    return JsonResponse({"error":error}, status=400)