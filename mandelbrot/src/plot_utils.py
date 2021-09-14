from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def watermark_text(input_image_path, output_image_path, text, pos):
    photo = Image.open(input_image_path)

    # make the image editable
    drawing = ImageDraw.Draw(photo)

    black = (3, 8, 12)
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(output_image_path)


def watermark_with_transparency(
    input_image_path, output_image_path, watermark_image_path, position
):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size

    transparent = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    # transparent.show()
    transparent.save(output_image_path)
