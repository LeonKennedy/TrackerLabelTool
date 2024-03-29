#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2022-2032, Node Supply Chain Manager Corporation Limited.
@contact: leonhe0119@gmail.com
@file: split_video.py
@time: 2024/3/29 10:59
@desc:
"""
import os.path
import time
import glob

import cv2
import tqdm


def _get_image_path(video_path: str) -> str:
    b = os.path.basename(video_path)
    name = b[:-4]
    video_image_path = os.path.join(image_path, name)
    return video_image_path


def run():
    for v in glob.glob(video_path + "/*.mp4"):
        _handle(v)


def _handle(filename: str):
    video_image_path = _get_image_path(filename)
    if os.path.exists(video_image_path):
        print(filename, "is exists.")
        return

    cv = cv2.VideoCapture(filename)
    if cv.isOpened():
        print("open file:", filename)
        print("fps", cv.get(cv2.CAP_PROP_FPS), "frame count", cv.get(cv2.CAP_PROP_FRAME_COUNT),
              "width", cv.get(cv2.CAP_PROP_FRAME_WIDTH), "height", cv.get(cv2.CAP_PROP_FRAME_HEIGHT))
        os.makedirs(video_image_path, exist_ok=True)
        n = 0
        pbar = tqdm.tqdm(desc="Processing", total=cv.get(cv2.CAP_PROP_FRAME_COUNT))
        while True:
            rval, frame = cv.read()
            if rval:
                cv2.imwrite(os.path.join(video_image_path, f"{n}.jpg"), frame)
                cv2.waitKey(1)
                n += 1
                pbar.update(1)
            else:
                break
    else:
        print(filename, "open error")


if __name__ == '__main__':
    video_path = "videos"
    image_path = "images"
    start_tm = time.time()
    run()
    print("Done! tm:", round(time.time() - start_tm, 2))
