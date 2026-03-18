

import cv2
import numpy as np
from sklearn.cluster import KMeans

def get_color_name(hsv_pixel):
    h, s, v = int(hsv_pixel[0]), int(hsv_pixel[1]), int(hsv_pixel[2])

    # Achromatic colors first (low saturation)
    if s < 30:
        if v < 50:
            return "black"
        elif v > 200:
            return "white"
        else:
            return "grey"

    # Chromatic colors by hue
    if h < 10 or h >= 170:
        if v < 80:
            return "dark red"
        return "red"
    elif h < 20:
        if s < 150 and v < 120:
            return "brown"
        return "orange"
    elif h < 33:
        return "yellow"
    elif h < 85:
        if v < 80:
            return "dark green"
        return "green"
    elif h < 125:
        if v < 80:
            return "navy"
        elif s < 100:
            return "light blue"
        return "blue"
    elif h < 145:
        return "indigo"
    elif h < 160:
        if s < 100:
            return "lavender"
        return "purple"
    elif h < 170:
        if s < 80:
            return "blush"
        return "pink"
    return "unknown"


def detect_color_combination(image_path, k=5):
    img = cv2.imread(image_path)
    if img is None:
        return ["unknown"]

    # Resize for speed
    img = cv2.resize(img, (300, 300))

    # Remove very light background pixels (common in product photos)
    # Convert to LAB and filter out near-white pixels
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    mask = lab[:, :, 0] < 240  # exclude near-white
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    pixels_hsv = hsv.reshape((-1, 3))
    mask_flat = mask.reshape(-1)
    
    # Filter pixels
    filtered = pixels_hsv[mask_flat]
    
    if len(filtered) < 100:
        filtered = pixels_hsv  # fallback if too much is filtered

    # KMeans clustering
    k = min(k, len(filtered))
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
    kmeans.fit(filtered)

    counts = np.bincount(kmeans.labels_)
    centers = kmeans.cluster_centers_

    color_results = {}
    for center, count in zip(centers, counts):
        color_name = get_color_name(center)
        if color_name not in ("unknown", "white"):  # skip white (likely background)
            color_results[color_name] = color_results.get(color_name, 0) + count

    sorted_colors = sorted(color_results.items(), key=lambda x: x[1], reverse=True)
    dominant_colors = [c[0] for c in sorted_colors[:3]]  # top 3

    if not dominant_colors:
        dominant_colors = ["unknown"]

    return dominant_colors
