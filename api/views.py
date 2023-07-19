from django.shortcuts import render

from .serializers import serviceSerializer,testimonialSerializer,teamSerializer,projectSerializer, courseSerializer,blogSerializer, contactSerializer
from .models import Services, Testimonials, Team, Project, Blog, Course, Contact
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
import threading

# Create your views here.

class datathread(threading.Thread):
    def __init__(self, data):
        self.data = data
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.data.send()
        except Exception as e:
            print(e)
            pass


def home(request):
    ser = Services.objects.all()    
    testm = Testimonials.objects.all()    
    data = {
        'services':ser,
        'testimonials':testm
        }
    return render(request, 'index.html', data)


class serviceApiView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        
        ser = Services.objects.all()
        context = {}
        if len(ser) > 0:
            context["services"] = serviceSerializer(ser,many=True).data
        else:
            context["services"] = "Service not found"
        return Response(context, status=status.HTTP_200_OK)
        
        
    def post(self, request):
        data = request.data
        context = {}
        form = serviceSerializer(data=data)
        if not form.is_valid():
            return Response({'error': True, 'errors': form.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            form.save()
            context["services"] = form.data
            return Response(context, status=status.HTTP_200_OK)
        
# Testimonials
class testimonialApiView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        
        testm = Testimonials.objects.all()
        context = {}
        if len(testm) > 0:
            context["testimonials"] = testimonialSerializer(testm,many=True).data
        else:
            context["testimonials"] = "Service not found"
        return Response(context, status=status.HTTP_200_OK)
        
        
    def post(self, request):
        data = request.data
        context = {}
        form = testimonialSerializer(data=data)
        if not form.is_valid():
            return Response({'error': True, 'errors': form.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            form.save()
            context["testimonials"] = form.data
            return Response(context, status=status.HTTP_200_OK)
        
# Team
class teamApiView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        
        testm = Team.objects.all()
        context = {}
        if len(testm) > 0:
            context["team"] = teamSerializer(testm,many=True).data
        else:
            context["team"] = "Team not found"
        return Response(context, status=status.HTTP_200_OK)
        
        
    def post(self, request):
        data = request.data
        context = {}
        form = teamSerializer(data=data)
        if not form.is_valid():
            return Response({'error': True, 'errors': form.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            form.save()
            context["team"] = form.data
            return Response(context, status=status.HTTP_200_OK)
        
# Project
class projectApiView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        
        testm = Project.objects.all()
        context = {}
        if len(testm) > 0:
            context["project"] = projectSerializer(testm,many=True).data
        else:
            context["project"] = "Project not found"
        return Response(context, status=status.HTTP_200_OK)
        
        
    def post(self, request):
        data = request.data
        context = {}
        form = projectSerializer(data=data)
        if not form.is_valid():
            return Response({'error': True, 'errors': form.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            form.save()
            context["project"] = form.data
            return Response(context, status=status.HTTP_200_OK)
        
# Course
class courseAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, course_id=None):
        if course_id is not None:
            try:
                course = Course.objects.get(id=course_id)
                context = {
                    "course": courseSerializer(course).data
                }
                return Response(context, status=status.HTTP_200_OK)
            except Course.DoesNotExist:
                return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        
        courses = Course.objects.all()
        context = {
            "courses": courseSerializer(courses, many=True).data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        form = courseSerializer(data=data)
        if not form.is_valid():
            return Response({'error': True, 'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            form.save()
            context = {
                "course": form.data
            }
            return Response(context, status=status.HTTP_200_OK)

        
# Blog
class blogApiView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, blog_id=None):
        if blog_id is not None:
            try:
                blog = Blog.objects.get(id=blog_id)
                context = {
                    "blog": blogSerializer(blog).data
                }
                return Response(context, status=status.HTTP_200_OK)
            except Blog.DoesNotExist:
                return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        
        blogs = Blog.objects.all()
        context = {
            "blog": blogSerializer(blogs, many=True).data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        form = blogSerializer(data=data)
        if not form.is_valid():
            return Response({'error': True, 'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            form.save()
            context = {
                "blog": form.data
            }
            return Response(context, status=status.HTTP_200_OK)
        
# Contact or email from user
@api_view(['POST'])
def contact(request):
    if request.method == 'POST':
        serializer = contactSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'error': True, 'errors': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            # Save the contact details to the database
            contact = serializer.save()
           
            msg1="NG-CivilArchitects."
            html_content = render_to_string("email.html",{'user':contact.name,'email':contact.email,'phone':contact.phone_number,'desc':contact.query_description})
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                    msg1,
                    text_content,
                    settings.EMAIL_HOST_USER,
                    ['namoanishtharu@gmail.com','erjuniorsanjip@gmail.com','contact@ngcivilarchitects.com',contact.email]
                    )
            print('Sending Email')
            email.attach_alternative(html_content, "text/html")
            # datathread(email).start()
            email.send()    
            return Response({'message': 'Thank you for contacting us! We will get back to you soon.'})

    return Response({'error': 'Invalid form data.'}, status=status.HTTP_400_BAD_REQUEST)








    # def patch(self,request):
    #     try:
    #         data=request.data
    #         lead_protity_id=data["lead_protity_id"]
    #         obj=LeadPrority.objects.filter(id=lead_protity_id).first()
    #         if obj is not None:
    #             serializer=LeadProritySerializer(obj,data,partial=True)
    #             if serializer.is_valid():
    #                 serializer.save()
    #                 return Response(data=serializer.data,status=status.HTTP_200_OK)
    #             else:
    #                 return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    #         else:
    #             return Response({'message':'lead_protity_id not found'},status=status.HTTP_404_NOT_FOUND)
    #     except Exception as e:
    #         return Response({'message':'lead_protity_id is required'},status=status.HTTP_400_BAD_REQUEST)

    # def delete(self,request):
    #     data = request.data
    #     context = {}
    #     try:
    #         lead_protity_id = data["lead_protity_id"]
    #         leadprority =LeadPrority.objects.get(id=lead_protity_id)
    #         leadprority.delete()
    #         context["msg"]="Successfully deleted lead protity"
    #         context["lead_protity"]=LeadProritySerializer(leadprority,many=False).data
    #         return Response(context, status=status.HTTP_200_OK)
    #     except:
    #         return Response({'error': True, 'errors': "valid lead_protity_id is required"},
    #                     status=status.HTTP_400_BAD_REQUEST)

