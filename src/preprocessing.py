from pathlib import Path
from PIL import Image, ImageOps, ImageFilter


def preprocess_image(image_path: str, height: int = 128) -> Image.Image:
    """Load, grayscale, denoise, binarize, and height-normalize a handwriting image."""
    img = Image.open(image_path).convert("L")
    img = img.filter(ImageFilter.MedianFilter(size=3))
    img = ImageOps.autocontrast(img)
    width = max(1, int(img.width * (height / img.height)))
    img = img.resize((width, height))
    img = img.point(lambda p: 255 if p > 160 else 0)
    return img


def save_processed(img: Image.Image, output_path: str) -> str:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path)
    return output_path
