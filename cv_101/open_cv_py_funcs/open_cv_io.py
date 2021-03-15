import cv2
import os
from typing import Optional, Union


def read_img_input(file_path, imread_option):
    if not os.path.exists(file_path):
        raise ValueError(f"Please provide a valid path. You gave - {file_path}")

    if imread_option not in {-1, 0, 1}:
        raise ValueError(f"Cannot understand image_read_option provided."
                         f"Expected a value from [-1, 0, 1]. You gave - {imread_option}")

    img = cv2.imread(file_path, imread_option)

    return img


def read_video_input(video_type:Union[int, str], file_path: Optional[str] = None):
    """
    If the input to the video is a device_index, video type should be the value of the device_index.
    It will be interpreted and read as such. Else, the value of video_type is "file"

    if the input is a file - we read the file path

    """
    device_id = None
    if isinstance(video_type, int):
        device_id = video_type

    else:
        if not file_path or not os.path.exists(file_path):
            raise ValueError("Please provide either a valid device index or a valid video file_path")

    if device_id:
        cap = cv2.VideoCapture(device_id)
        if not cap.isOpened():
            cap.open(device_id)
    else:
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            cap.open(file_path)
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()



