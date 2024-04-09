import asyncio
import websockets
from pickle import loads    
import matplotlib.pyplot as plt
import numpy as np
import csv
async def image():
    uri = "ws://192.168.2.117:9999"
    async with websockets.connect(uri) as websocket:
        inp = input("PRESSS 't' TO GET DATA...: ")
        if(inp == 't'):
            message = "DATA"
            await websocket.send(message)
            response = await websocket.recv()
            data = loads(response)[0]
            print(data.shape)
            x = np.arange(start=0, stop=len(data), step=1)
            print(x.shape)
            A, B, C, D = [359.983773, 0.26482365, 2.445666e-5, -8.5555e-9]
            wavelen = A + B*x + C*x**2 + D*x**3
            print(wavelen.shape)
            Points = np.vstack([wavelen, data])
            np.savetxt("spactrum.csv", Points.T, delimiter=",", fmt="%.8f")
           

asyncio.get_event_loop().run_until_complete(image())
