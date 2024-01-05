import math
from typing import Dict, Tuple, Iterable, Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.patches import Rectangle
from scipy.spatial import ConvexHull

FONTSIZE_NORMAL = 10
FONTSIZE_BIGGER = 12

SIZE_NORMAL = 10
SIZE_BIGGER = 12

DBSCAN_COLOR_DICT = {

    -1: "red",
    0: "lightblue",
    1: "lightcoral",
    2: "yellow",
    3: "grey",
    4: "pink",
    5: "navy",
    6: "orange",
    7: "purple",
    8: "salmon",
    9: "olive",
    10: "brown",
    11: "tan",
    12: "lime",
}

def dist1(x: np.ndarray, y: np.ndarray) -> float:
    """Original euclidean distance."""
    return np.sqrt(np.sum((x - y) ** 2))


def dist2(data: dict, x, y) -> float:
    """Euclidean distance which takes keys of a dictionary (X_dict) as inputs."""
    return np.sqrt(np.sum((data[x] - data[y]) ** 2))

def annotate_points(annotations: Iterable, points: np.ndarray, ax) -> None:
    """
    Annotate the points of the axis with their name (number).

    :param annotations: names of the points (their numbers).
    :param points: array of their positions.
    :param ax: axis of the plot.
    """
    for i, txt in enumerate(annotations):
        ax.annotate(
            txt,
            (points[i, 0], points[i, 1]),
            fontsize=FONTSIZE_NORMAL,
            #size=SIZE_NORMAL,
            ha="center",
            va="center",
        )
