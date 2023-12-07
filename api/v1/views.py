from flask import jsonify
from .config import *
from .Github.tags import *

async def MarseyHello():
    return jsonify(message=message, version=latest)


async def MarseyVersion():
    return jsonify(latest=await GetLatestMarseyTag(), minimum=await GetLatestMarseyMTag(), releases=release)
