#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2022-2032, Node Supply Chain Manager Corporation Limited.
@contact: leonhe0119@gmail.com
@file: patch_rest_court_point.py
@time: 2024/4/24 10:52
@desc:
"""
import glob
import json
import os.path
import sys
from typing import List


def _find_court_data(shape_data):
    if len(shape_data) < 10:
        return None

    append_data = []
    for shape in shape_data:
        print(shape)
        if shape["label"] == "court":
            append_data.append(shape)
        if shape["label"] == "pole":
            append_data.append(shape)

    if len(append_data) == 10:
        return append_data


def filter_court_point(shape_data) -> List:
    if len(shape_data) < 10:
        return shape_data

    return [shape for shape in shape_data if shape["label"] not in ("court", "pole")]


def save_append_file(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    print("save to", file)


def run(file_path):
    files = [f for f in glob.glob(os.path.join(file_path, "*.json"))]
    files.sort(key=lambda x: int(x.split("/")[-1].split(".")[0]))
    court_data = None
    append_cnt = 0
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if data["flags"].get("court_occluded", False):
            continue

        shape_data = data["shapes"]

        if court_data:
            shape_data_exclude_court = filter_court_point(shape_data)
            shape_data_exclude_court.extend(court_data)
            data["shapes"] = shape_data_exclude_court
            save_append_file(data, file)
            append_cnt += 1
        else:
            court_data = _find_court_data(shape_data)
            if court_data:
                print("find court data in", file)

    print("handle done", file_path, "append", append_cnt, "cnt")


if __name__ == '__main__':
    json_dir_path = sys.argv[1]
    assert os.path.exists(json_dir_path), f"{json_dir_path} not exists"
    run(json_dir_path)
