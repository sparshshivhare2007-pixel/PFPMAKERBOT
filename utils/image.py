from PIL import Image, ImageEnhance

def cinematic_bw(img):
    img = img.convert("L").convert("RGB")

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.8)

    return img


def resize_square(img, size=1024):
    return img.resize((size,size))
