import cv2
import av
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer,WebRtcMode,RTCConfiguration,VideoProcessorBase

RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

class OpenCVVideoProcessor(VideoProcessorBase):

        

        def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
            img = frame.to_ndarray(format="bgr24")
            img = cv2.putText(img, 'OpenCV', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 2, cv2.LINE_AA)            
            return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_ctx = webrtc_streamer(key="sample",desired_playing_state = True,mode=WebRtcMode.SENDRECV,rtc_configuration=RTC_CONFIGURATION,video_processor_factory=OpenCVVideoProcessor,async_processing=True,)
