import cv2
import numpy as np
import websockets
import asyncio
from pickle import dumps 

cap = cv2.VideoCapture(4) #REMEMBA TO CHECK YOUR VIDEO SOURCE!
width = 1920
height = 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, 0.5)
cap.set(cv2.CAP_PROP_EXPOSURE, 5000)

async def echo(websocket, path):
        async for message in websocket:
            for i in range(0,4):
                cap.read()
            _, frame = cap.read()
            frame = cv2.resize(frame, (1920, 1080))
            frame = frame[439:450, 0:1920] 

            frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_HLS = cv2.cvtColor(frame_RGB, cv2.COLOR_RGB2HLS)
            frame_L = frame_HLS[:, :, 1]
            # frame_flip = np.flip(frame_L)
            
            frame_to_send = dumps(frame_L)
            await websocket.send(frame_to_send)
            

start_server = websockets.serve(echo, "192.168.2.117", 9999)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

cv2.destroyAllWindows() 

