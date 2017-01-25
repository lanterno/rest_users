from rest_framework import response, status
from rest_framework.views import APIView


class SuspendAccountView(APIView):

    def post(self, request, *args, **kwargs):
        self.request.user.is_active = False
        self.request.user.save()
        return response.Response({'message': 'success'}, status=status.HTTP_200_OK)
