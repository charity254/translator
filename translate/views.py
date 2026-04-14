from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# Create your views here.

eng_to_sw = {
    "hello" : "habari",
    "buy maize":    "nunua mahindi",
    "good morning": "habari ya asubuhi",
    "are you gong to work?": "unaenda kazini?",
    "animals": "wanyama",
    "fruits": "matunda",
    "school": "shule",
    "go to bed": "enda kulala",
    "what do you want to eat?": "unataka kula nini?",
    "I have finished studying": "nimemaliza kusoma",
}

sw_to_eng = {v: k for k, v in eng_to_sw.items()}

def index(request):
    return render(request, 'translate/index.html')

@csrf_exempt
@require_POST
def translate_text(request):
    """
    POST /api/v1/translate-text
    Accepts: { "text": "...", "targetLanguage": "sw" or "en" }
    Returns: { "translatedText": "..." }
    """
    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400) 
    
    text = body.get('text', '').strip().lower()
    target = body.get('targetLanguage', '').strip().lower()
    
    if not text:
        return JsonResponse({'error': 'Text field cannot be empty'}, status=400)

    if not target:
        return JsonResponse({'error': 'targetLanguage field cannot be empty'}, status=400)
    if target == 'sw':
        translated = eng_to_sw.get(text, text)
    elif target == 'en':
        translated = sw_to_eng.get(text, text)
    else:
        translated = text
    return JsonResponse({'translatedText': translated})