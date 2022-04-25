from ninja import NinjaAPI
from djninja.tracks.models import Track
from djninja.tracks.schema import TrackSchema, NotFoundSchema
from typing import List


api = NinjaAPI()

@api.get("/tracks", response=List[TrackSchema])
def tracks(request):
    return Track.objects.all()

@api.get("/track/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def track(request, track_id: int):
    try:
        track = Track.objects.get(pk=track_id)
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}
