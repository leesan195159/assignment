import json
from django.http import JsonResponse
from .models import *
from django.views import View

class OwnerView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name  = data['name']
            email = data['email']
            age   = data['age']

            Owner.objects.create(
                name=name, 
                email=email,
                age=age
                )

            return JsonResponse({'Result': 'created'}, status = 201)
        except KeyError:
            return JsonResponse({'Error : KeyError'}, status=400)
    
    def get(self, request):
 
            owners = Owner.objects.all()
            results = [{
                'name'  : owner.name, 
                'email' : owner.email,
                'age'   : owner.age,
                'dog_list' : [{
                    'name' : dog.name,
                    'age'  : dog.age,
                } for dog in owner.dog_set.all()]
                } for owner in owners]

            return JsonResponse({'Result': results}, status = 201)

class DogView(View):
        def post(self, request):
            try:
                data     = json.loads(request.body)
                name     = data['name']
                age      = data['age']
                owner_id = data['owner']

                owner = Owner.objects.get(id=owner_id)

                Dog.objects.create(
                    name  = name,
                    age   = age,
                    owner = owner
                )
                return JsonResponse({'Result': 'created'}, status = 201) 

            except KeyError:
                return JsonResponse({'Error : KeyError'}, status=400) 
            except Owner.DoesNotExist:
                return JsonResponse({'Error : Specified owner does not exist.'}, status=404) 
            except Owner.MultipleObjectsReturned:
                return JsonResponse({'Error : Multiple objects returned.'}, status=400)  

        def get(self, request):

            dogs = Dog.objects.all()
            results = [{
                'name'       : dog.name,
                'age'        : dog.age,
                'owner_list' : {
                    'name' : dog.owner.name,
                    'age'  : dog.owner.age,
                }
            }for dog in dogs]

            return JsonResponse({'Result': results}, status = 201) 
            
