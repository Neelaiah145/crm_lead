from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib import messages

from .models import Contact_lead
from .serializers import Contact_leadSerializer


class ContactList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "leads_page.html"

    def get(self, request):
        contacts = Contact_lead.objects.all()
        serializer = Contact_leadSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Contact_leadSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)









class DeleteLeadManagement(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "leads_page.html"

    def get(self, request):

        delete_id = request.GET.get("delete_id")
        selected_ids = request.GET.get("selected_ids")

        if delete_id:
            Contact_lead.objects.filter(id=delete_id).delete()
            messages.success(request, "Lead deleted successfully")

        elif selected_ids:
            ids = selected_ids.split(",")
            Contact_lead.objects.filter(id__in=ids).delete()
            messages.success(request, "Selected leads deleted successfully")

        contacts = Contact_lead.objects.all()
        serializer = Contact_leadSerializer(contacts, many=True)

        return Response({
            "contacts": serializer.data
        })