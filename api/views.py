from django.http import JsonResponse
from datetime import datetime
import pytz

def hng_api(request):
    response_data = {
        "email": "samuelt.oshin@gmail.com", 
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/yourusername/your-repo", 
    }
    return JsonResponse(response_data)
