from __future__ import annotations
import dataclasses, json

from trail import Trail, TrailSplit, TrailSeries
from mountain import Mountain

def serialize(trail):
    return json.dumps(trail, default=lambda o: o.__dict__)

def deserialize(data):
    return json.loads(data, object_hook=lambda d: Trail(**d))
