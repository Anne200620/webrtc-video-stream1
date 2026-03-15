import asyncio
import cv2
from aiortc import RTCPeerConnection

async def main():

    pc = RTCPeerConnection()

    @pc.on("track")
    async def on_track(track):

        print("Flux vidéo reçu")

        while True:
            frame = await track.recv()

            img = frame.to_ndarray(format="bgr24")

            cv2.imshow("Video Stream", img)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break


asyncio.run(main())
