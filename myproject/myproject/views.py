from django.http import JsonResponse

def main_page(reqeust):
    data = {
        'key1': 'value1',
        'key2': 'value2',
    }
    return JsonResponse(data)