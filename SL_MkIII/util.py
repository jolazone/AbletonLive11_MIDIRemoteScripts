# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/SL_MkIII/util.py
# Compiled at: 2022-01-27 16:28:16
# Size of source mod 2**32: 1118 bytes
from __future__ import absolute_import, print_function, unicode_literals
from past.utils import old_div
from ableton.v2.base import clamp, liveobj_valid
from ableton.v2.control_surface.components import find_nearest_color
from ableton.v2.control_surface.elements import Color
from novation.colors import CLIP_COLOR_TABLE, RGB_COLOR_TABLE

def normalized_parameter_value(param):
    value = 0.0
    if liveobj_valid(param):
        param_range = param.max - param.min
        value = old_div(float(param.value - param.min), param_range)
    return clamp(value, 0.0, 1.0)


def convert_parameter_value_to_midi_value(param):
    return int(normalized_parameter_value(param) * 127)


def is_song_recording(song):
    return song.session_record or song.record_mode


def color_for_track(track):
    color_value = 0
    if liveobj_valid(track):
        try:
            color_value = CLIP_COLOR_TABLE[track.color]
        except (KeyError, IndexError):
            color_value = find_nearest_color(RGB_COLOR_TABLE, track.color)

        return Color(color_value)