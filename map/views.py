from django.shortcuts import render
from .models import Landmark

# Create your views here.

def landmark_list(request):
    all_landmarks = Landmark.objects.all()
    return render(request, 'map/landmark_list.html', {'all_landmarks': all_landmarks})

def landmark_detail(request, landmark_id):
    landmark = Landmark.objects.get(id=landmark_id)
    google_maps_address = _generate_google_address(landmark.address)
    return render(request, 'map/landmark_detail.html', {'landmark': landmark, 'google_maps_address': google_maps_address})

# lead with _ to signal that this method is only used in this file.
def _generate_google_address(address):
    modified_address = address.replace(" ", '+')
    return modified_address