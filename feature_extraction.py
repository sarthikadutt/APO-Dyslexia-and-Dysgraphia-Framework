import numpy as np
from PIL import Image


def extract_demo_features(img: Image.Image) -> dict:
    """Extract lightweight proxy features for demo execution.

    These are not clinical features. They approximate APO fields so that the
    pipeline can run without restricted data or trained checkpoints.
    """
    arr = np.array(img.convert("L"))
    ink = arr < 128
    cols = ink.sum(axis=0)
    rows = ink.sum(axis=1)
    density = float(ink.mean())
    crowding = float(np.clip(cols.std() / (cols.mean() + 1e-6) / 5, 0, 1))
    tilt_variance = float(np.clip(rows.std() / (rows.mean() + 1e-6) / 10, 0, 1))
    stas = float(np.clip((density * 2 + crowding) / 3, 0, 1))
    gri = int(crowding > 0.45)
    return {"STAS": stas, "LTVC": tilt_variance, "SCI": crowding, "GRI": gri}
