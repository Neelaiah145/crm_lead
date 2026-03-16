from django.shortcuts import render,redirect

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact_lead
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import Contact_leadSerializer

class ContactList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "leads_page.html"
    def get(self, request):
        contacts = Contact_lead.objects.all()
        serializer = Contact_leadSerializer(contacts, many=True)
        return Response({"contacts":serializer.data})
   

    def post(self, request):
        serializer = Contact_leadSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
 

class DeleteLeadManagement(APIView):

    def get(self, request):

        delete_id = request.GET.get("delete_id")

        if delete_id:
            Contact_lead.objects.filter(id=delete_id).delete()
            return redirect("contact_lead/")

        selected_ids = request.GET.get("selected_ids")

        if selected_ids:
            ids = selected_ids.split(",")
            Contact_lead.objects.filter(id__in=ids).delete()

        return redirect("contact_lead")