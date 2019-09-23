from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
  return HttpResponse("Hello, world. You're at the NOVA index.")

# Schema: {"conversations": List<List<{from: String, text: String}>>}
def conversations(request):
  conversation1 = [
    {"from": "nova", "text": "Hey it's Nova, how are you today?"},
    {"from": "patient", "text": "Doing pretty well!"},
    {"from": "nova", "text": "Good, anything not go well today?"},
    {"from": "patient", "text": "Nope!"},
    {"from": "nova", "text": "Ok, have a nice rest of your day!"},
  ]
  conversation2 = [
    {"from": "nova", "text": "Hey it's Nova, how are you today?"},
    {"from": "patient", "text": "Not so good. Feeling really down today."},
    {"from": "nova", "text": "Oh, I'm sorry to hear that. Can you give me any details?"},
  ]
  conversation3 = [
    {"from": "nova", "text": "Hey it's Nova, how are you today?"},
  ]

  response_data = {'conversations': [conversation1, conversation2, conversation3]}
  return JsonResponse(response_data)

# Schema: {"data": List<Int>}
def anxiety(request):
  response_data = {'data': [3, 2, 5, 1, 7, 5, 2]}
  return JsonResponse(response_data)