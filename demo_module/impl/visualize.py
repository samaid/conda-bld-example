from demo_module.impl.arg_parse import parse_args

GUI = parse_args().gui

if GUI == "pygame".casefold():
    import pygame as pg
elif GUI == "matplotlib".casefold():
    import matplotlib.pyplot as plt
elif GUI == "plotly".casefold():
    import plotly
elif GUI == "opencv".casefold():
    import cv2

MAX_FRAMES = parse_args().max_frames


def visual_init(w, h):
    surface = (w, h)
    return surface


def visual_draw(surface, frames):
    pass


def visual_prepare_next_frame(surface, frames):
    return frames < MAX_FRAMES


def visual_user_cancelled():
    return False


def visual_finalize():
    pass
