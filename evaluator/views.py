# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import requests
# import json
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
#
# CHATGPT_API_KEY = os.getenv('CHATGPT_API_KEY')
#
# SECRET_KEY = os.getenv('SECRET_KEY')
#
#
# @csrf_exempt
# def chatgpt_view(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         user_input = data.get("content", "")
#
#         api_url = "https://api.openai.com/v1/chat/completions"
#         headers = {
#             "Authorization": "Bearer " + CHATGPT_API_KEY,
#             "Content-Type": "application/json",
#         }
#         payload = {
#             "model": "gpt-3.5-turbo-1106",
#             "messages": [
#                 {"role": "system", "content": "You are an IELTS examiner.  "
#                                               "Evaluate and give scores from 0 to 9 on each of the following aspects:"
#                                               "Task Achievement and Response, Coherence and Cohesion, Lexical Resources, Grammatical Range and Accuracy. "
#                                               "give a detailed feedback and example to improve  "
#                                               "in addition, at last part give a over all score."},
#                 {"role": "user", "content": user_input}
#             ]
#         }
#
#         response = requests.post(api_url, headers=headers, json=payload)
#         response_data = response.json()
#         print("Full API Response:", response_data)  # Debugging line
#
#         assistant_response = response_data['choices'][0]['message']['content']
#
#         return JsonResponse({"response": assistant_response})
#     return JsonResponse({"error": "Invalid request"}, status=400)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

CHATGPT_API_KEY = os.getenv('CHATGPT_API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

@csrf_exempt
def chatgpt_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_input = data.get("content", "")

            api_url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Authorization": "Bearer " + CHATGPT_API_KEY,
                "Content-Type": "application/json"
            }
            payload = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are an IELTS examiner.  "
                                                  "Evaluate and give scores from 0 to 9 on each of the following aspects:"
                                                  "Task Achievement and Response, Coherence and Cohesion, Lexical Resources, Grammatical Range and Accuracy. "
                                                  "Give a detailed feedback and example to improve. "
                                                  "In addition, at last part give an overall score."},
                    {"role": "user", "content": user_input}
                ]
            }

            response = requests.post(api_url, headers=headers, json=payload)
            response_data = response.json()
            print("Full API Response:", response_data)  # Debugging

            # Check for errors in the response
            if response.status_code != 200:
                return JsonResponse({'error': response_data.get('error', 'An error occurred')}, status=response.status_code)

            # Check if 'choices' key exists in the response
            if 'choices' in response_data:
                assistant_response = response_data['choices'][0]['message']['content']
                return JsonResponse({"response": assistant_response})
            else:
                return JsonResponse({'error': 'No choices found in the response'}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': f'Missing key in response: {e}'}, status=500)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=405)

