from PIL import ImageDraw, ImageFilter

def draw_neon_text(image, position, text, font, color=(255,0,255)):
    draw = ImageDraw.Draw(image)

    # base text
    draw.text(position, text, fill=color, font=font)

    # glow layers
    glow = image.filter(ImageFilter.GaussianBlur(12))
    glow2 = image.filter(ImageFilter.GaussianBlur(6))

    image = Image.blend(glow, image, 0.6)
    image = Image.blend(glow2, image, 0.8)

    return image
