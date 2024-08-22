from django.http import JsonResponse

def sample_api_view(request):
    data = {
        'message': 'Hello, this is your API response!',
        'status': 'success'
    }
    return JsonResponse(data)


def get_data(request):
    data = {"message": "GET request successful!"}
    return JsonResponse(data)

def post_data(request):
    if request.method == 'POST':
        data = {"message": "POST request successful!"}
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)