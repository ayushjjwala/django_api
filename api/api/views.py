from django.http import JsonResponse

def sample_api_view(request):
    data = {
        'message': 'Hello, this is your API response!',
        'status': 'success'
    }
    return JsonResponse(data)
