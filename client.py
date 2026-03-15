import asyncio
import cv2
from aiortc import VideoStreamTrack
from av import VideoFrame

class CameraTrack(VideoStreamTrack):

    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(0)

    async def recv(self):
        pts, time_base = await self.next_timestamp()

        ret, frame = self.cap.read()
        if not ret:
            return

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        video_frame = VideoFrame.from_ndarray(frame, format="rgb24")
        video_frame.pts = pts
        video_frame.time_base = time_base

        return video_frame


async def main():
    print("Serveur WebRTC démarré")
    print("Capture de la webcam en cours...")

    camera = CameraTrack()

    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
