from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact_lead
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from .serializers import Contact_leadSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login,logout
from rest_framework_simplejwt.tokens import RefreshToken



# Create your views here.
class LoginView(APIView):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.data.get('email') or request.POST.get('email')
        password = request.data.get('password') or request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            if request.content_type == "application/json":
                return Response({
                    "message": "Login successful",
                    "email": user.email,
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                })


            return redirect("contact_lead")

        if request.content_type == "application/json":
            return Response({"error": "Invalid credentials"})

        return render(request, "login.html", {"error": "Invalid credentials"})



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            logout(request)
            return Response({"message": "Logout successful"})
        except Exception as e:
            return Response({"error": str(e)})





def get(self, request):
    print(request.user)   
    return Response({"msg": "ok"})




















class ContactList(APIView):
    permission_classes = [IsAuthenticated]
    
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = "leads_page.html"

    def get(self, request):
        contacts = Contact_lead.objects.all()
        serializer = Contact_leadSerializer(contacts, many=True)
        return Response({"contacts": serializer.data})

    def post(self, request):
        serializer = Contact_leadSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)





class EditLeadContact(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name="edit_lead.html"
    def get(self, request, pk):
        contact = get_object_or_404(Contact_lead, pk=pk)
        return Response({"contact":contact})

    def post(self, request, pk):
        contact = get_object_or_404(Contact_lead, pk=pk)

        serializer = Contact_leadSerializer(
            contact,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            
            return Response({
                "success": "Lead updated successfully",
                "data": serializer.data
            })
            
        return Response(serializer.errors)
       







class DeleteLeadManagement(APIView):

    def get(self, request, id=None):

        selected_ids = request.GET.get("selected_ids")

        if selected_ids:
            ids = selected_ids.split(",")
            Contact_lead.objects.filter(id_in=ids).delete()
            return redirect("contact_lead")

        if id:
            contact = get_object_or_404(Contact_lead, id=id)
            return render(request, "delete.html", {"contact": contact})

        return redirect("contact_lead")


    def post(self, request, id):

        contact = get_object_or_404(Contact_lead, id=id)
        contact.delete()

        return redirect("contact_lead")
