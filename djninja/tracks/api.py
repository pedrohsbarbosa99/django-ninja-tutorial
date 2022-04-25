from ninja import NinjaAPI
from djninja.tracks.models import Track
from djninja.tracks.schema import TrackSchema, NotFoundSchema
from typing import List


api = NinjaAPI()

@api.get("/tracks", response=List[TrackSchema])
def tracks(request):
    return Track.objects.all()