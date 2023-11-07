from django.http import JsonResponse

def throwError(error):
    return JsonResponse({"error":error}, status=400)