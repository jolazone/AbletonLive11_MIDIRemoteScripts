# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Roland_FA/navigation.py
# Compiled at: 2021-06-29 09:33:48
# Size of source mod 2**32: 591 bytes
from __future__ import absolute_import, print_function, unicode_literals
import ableton.v2.control_surface.components as SessionNavigationComponentBase
from .scroll import ScrollComponent

class SessionNavigationComponent(SessionNavigationComponentBase):

    def __init__(self, *a, **k):
        (super(SessionNavigationComponent, self).__init__)(*a, **k)
        self._horizontal_paginator = ScrollComponent((self.track_pager_type(self._session_ring)),
          parent=self)