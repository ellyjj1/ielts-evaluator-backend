from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from decouple import config

CHATGPT_API_KEY = config('CHATGPT_API_KEY')


def chatgpt_view(request):
    api_key = CHATGPT_API_KEY


@csrf_exempt
def chatgpt_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_input = data.get("content", "")

        api_url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": "Bearer " + CHATGPT_API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gpt-3.5-turbo-1106",
            "messages": [
                {"role": "system", "content": "You are an IELTS examiner.  "
                                              "Evaluate and give scores from 0 to 9 on each of the following aspects:"
                                              "Task Achievement and Response, Coherence and Cohesion, Lexical Resources, Grammatical Range and Accuracy. "
                                              "give a detailed feedback and example to improve  "
                                              "in addition, at last part give a over all score."},
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(api_url, headers=headers, json=payload)
        response_data = response.json()

        assistant_response = response_data['choices'][0]['message']['content']

        return JsonResponse({"response": assistant_response})
    return JsonResponse({"error": "Invalid request"}, status=400)
