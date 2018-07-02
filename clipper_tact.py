# -*- coding: utf-8 -*-
"""
Created on 1/2/18

@author: olga
"""
import cProfile
import os
from collections import namedtuple
import cv2
import pandas as pd
import sys

FPS = 25
OUTPUT_DIMENSIONS = None
OUTPUT_DIMENSIONS = (960,540)

def read_intervals_data(file_path):
    df = pd.read_csv(file_path, dtype={
        'GameID': 'object',
        'Half': 'object',
        'TeamName': 'object',
        'PlayerName': 'object',
        'OutFileName': 'object',
        'StartFrame': 'int64',
        'Duration': 'int64',
    })
    return df


def add_intervals_info(intervals_data, options):
    intervals_data['StartFrame'] += options.start_offset
    intervals_data['last_frame'] = intervals_data.apply(
        lambda row: row.StartFrame + row.Duration, axis=1)
    intervals_data['output_directory'] = intervals_data.apply(
        lambda row: os.path.join(options.output_folder, row.GameID, row.Half, row.TeamName,
                                 row.PlayerName), axis=1)


def validate_argv(argv):
    if len(argv) == 5:
        return True


def validate_options(options):
    for file in [options.input_video, options.intervals_csv]:
        if not os.path.exists(file):
            raise FileNotFoundError("File {} does not exist".format(file))


def resize_frame(frame):
    if OUTPUT_DIMENSIONS:
        return cv2.resize(frame, OUTPUT_DIMENSIONS)
    return frame


def clip_one_player(intervals_data, options):
    max_frame = intervals_data['last_frame'].max()

    cap = cv2.VideoCapture(options.input_video)
    # fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    # fourcc = cv2.VideoWriter_fourcc(*'DIV4') // avi
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    frame_number = 0
    output_files = {}

    while True:
        _, frame = cap.read()
        # no more frames left
        if frame is None or frame_number > max_frame + 1:
            break

        for interval_row in intervals_data.itertuples():
            # output_directory = interval_row[8]
            output_directory = interval_row.output_directory
            output_file = os.path.join(output_directory, interval_row.OutFileName+'.mp4')
            # if interval starts from the current frame
            if interval_row.StartFrame == frame_number:
                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)
                output_dim = OUTPUT_DIMENSIONS or (frame.shape[1], frame.shape[0])
                output_files[output_file] = cv2.VideoWriter(
                    output_file, fourcc, FPS, output_dim)
            elif interval_row.last_frame == frame_number or \
                    (interval_row.last_frame < frame_number):
                to_close_output = output_files.pop(output_file, None)
                if to_close_output:
                    to_close_output.release()

        for output in output_files.values():
            output.write(resize_frame(frame))
        frame_number += 1
        #print("Frame {}".format(frame_number))

    for incomplete_output in output_files.keys():
        print("[Warning] File {}.mp4 is incomplete!".format(incomplete_output))
        output_files[incomplete_output].release()


def run(argv):
    if not validate_argv(argv):
        print("Usage: {} <input_video> <intervals.csv> <start_offset> <output_folder>".format(argv[0]))
        return
    Options = namedtuple('Options', ['input_video',
                                     'intervals_csv',
                                     'start_offset',
                                     'output_folder'])
    options = Options(argv[1], argv[2], int(argv[3]), argv[4])
    validate_options(options)

    intervals_data = read_intervals_data(options.intervals_csv)
    add_intervals_info(intervals_data, options)
    clip_one_player(intervals_data, options)


if __name__=='__main__':
    #cProfile.run('run(sys.argv)')
    run(sys.argv)
