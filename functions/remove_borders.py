import pandas as pd
import matplotlib.pyplot as plt

def remove_borders() -> None:
    """
    Removes borders from an existing graph.
    """
    for spine in plt.gca().spines.values():
        spine.set_visible(False)