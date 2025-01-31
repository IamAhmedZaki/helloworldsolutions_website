from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from .serializer import ContactSerializer
from rest_framework import status

# Static views
def index(request):
    return render(request, 'index.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def portfolio_details2(request):
    return render(request, 'portfolio-details2.html')

def portfolio_details3(request):
    return render(request, 'portfolio-details3.html')

def sarter_page(request):
    return render(request, 'sarter-page.html')

def service_details(request):
    return render(request, 'service-details.html')

def service_details2(request):
    return render(request, 'service-details2.html')

def service_details3(request):
    return render(request, 'service-details3.html')

def service_details4(request):
    return render(request, 'service-details4.html')

def service_details5(request):
    return render(request, 'service-details5.html')

def service_details6(request):
    return render(request, 'service-details6.html')

# API View for handling contact form submissions
class ContactView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)

        # Validate the serializer data
        if serializer.is_valid():
            try:
                # Send the email
                send_mail(
                    subject=f"Contact Form: {serializer.validated_data['subject']}",
                    message=f"Name: {serializer.validated_data['name']}\n"
                            f"Email: {serializer.validated_data['email']}\n\n"
                            f"Message:\n{serializer.validated_data['message']}",
                    from_email=serializer.validated_data['email'],
                    recipient_list=['mahmedzaki670@gmail.com'],  # Your email
                    fail_silently=False,
                )
                return Response({"message": "Your message has been sent successfully!"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": f"Failed to send email: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # Return serializer errors if validation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
