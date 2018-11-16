from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import gc
import logging
import six
import time

from functools import wraps
from tensorboardX.writer import SummaryWriter
from atalaya.grapher.visdom_writer import VisdomWriter


# Supports both TensorBoard and Visdom (no embedding or graph visualization with Visdom)
vis_formats = {'tensorboard': SummaryWriter, 'visdom': VisdomWriter}


class Grapher:
    def __init__(self, *args, **kwargs):
        self.subscribers = {}
        self.register(*args, **kwargs)

    def register(self, *args, **kwargs):
        # Sets tensorboard as the default visualization format if not specified
        formats = ['tensorboard'] if not args else args
        for format in formats:
            if self.subscribers.get(format) is None and format in vis_formats.keys():
                self.subscribers[format] = vis_formats[format](**kwargs)

    def unregister(self, *args):
        for format in args:
            self.subscribers[format].close()
            del self.subscribers[format]
            gc.collect()

    def __getattr__(self, attr):
        for _, subscriber in six.iteritems(self.subscribers):
            def wrapper(*args, **kwargs):
                for _, subscriber in six.iteritems(self.subscribers):
                    if hasattr(subscriber, attr):
                        getattr(subscriber, attr)(*args, **kwargs)
            return wrapper
        raise AttributeError

    # Handle writer management (open/close) for the user
    def __del__(self):
        for _, subscriber in six.iteritems(self.subscribers):
            subscriber.close()