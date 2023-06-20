from django.shortcuts import render

from .serializers import serviceSerializer,testimonialSerializer,teamSerializer,projectSerializer
from .models import Services,Testimonials,Team,Project
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.


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

