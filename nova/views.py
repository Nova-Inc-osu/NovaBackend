from django.http import HttpResponse, JsonResponse
from nova.models import Doctor, Patient, Conversation, Message
from django.contrib.auth.models import User
from django.core import serializers

# Create your views here.
def index(request):
  return HttpResponse("Hello, world. You're at the NOVA index.")

# Schema: {"conversations": List<List<{from: String, text: String}>>}
def conversations(request, patient_id):
  try:
    logged_in_doctor = Doctor.objects.get(user=request.user)

    patient = Patient.objects.get(pk=patient_id)

    conversations_with_messages = []

    if patient.doctor == logged_in_doctor:
      conversations = Conversation.objects.filter(participant=patient)

      conversations_with_messages = [serializers.serialize('json', [msg,]) for convo in conversations for msg in Message.objects.filter(conversation=convo)]

      response_data = {'conversations': conversations_with_messages}
      return JsonResponse(response_data)

    else:
      response_data = {'conversations': [], 'thisIsntYourPatient': True}
      return JsonResponse(response_data)

  except Doctor.DoesNotExist as dne:
    response_data = {'conversations': [], 'youreNotADoctor': True}
    return JsonResponse(response_data)

# Schema: {"data": List<Int>}
def anxiety(request):
  response_data = {'data': [3, 2, 5, 1, 7, 5, 2]}
  return JsonResponse(response_data)