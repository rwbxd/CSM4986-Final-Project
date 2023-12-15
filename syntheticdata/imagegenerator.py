from PIL import Image
import os
from dataclasses import dataclass

if not os.path.exists("nums/generated/"): os.makedirs("nums/generated")

@dataclass
class Color:
    color: tuple
    name: str

ORANGE = Color((252, 111, 3), "orange")
WHITE = Color((255, 255, 255), "white")

nums = []
for i in range(10):
    nums.append(Image.open(f"nums/{i}.png"))
nums.append(Image.open("nums/decimal.png"))
s = 0
iw, ih = nums[0].size
decimal_offset = 110

from tqdm.auto import tqdm
def generate(start, end, color, decimal=False):
    if decimal: return _generate_decimal(start, end, color)
    for i in tqdm(range(start, end)):
        si = str(i)
        new_image = Image.new("RGB", (((len(si) * iw) + ((len(si)-1) * s)), ih), color.color)
        for j, ci in enumerate(si):
            new_image.paste(nums[int(ci)], (j * (iw + s), 0), nums[int(ci)])
        new_image.save(f"nums/generated/{si}-{color.name}.png", "PNG")

def _generate_decimal(start, end, color, n_points=2):
    for i in tqdm(range(start, end)):
        si = str(i)
        if len(si) == 2: si = "0" + si
        new_image = Image.new("RGB", (((len(si) * iw) + ((len(si)-1) * s)), ih), color.color)
        for j, ci in enumerate(si[:-2]):
            new_image.paste(nums[int(ci)], (j * (iw + s), 0), nums[int(ci)])
        new_image.paste(nums[-1], ((len(si) - 3) * (iw + s) + decimal_offset, 0), nums[-1])
        for j, ci in enumerate(si[-2:], len(si)-2):
            new_image.paste(nums[int(ci)], (j * (iw + s), 0), nums[int(ci)])
        new_image.save(f"nums/generated/{si[:-2]}.{si[-2:]}-{color.name}.png", "PNG")

generate(10, 10001, WHITE)
generate(10, 10001, ORANGE)
generate(10, 10001, WHITE, True)
generate(10, 10001, ORANGE, True)

from PIL import ImageEnhance

def generate_dark(start, end):
    for i in tqdm(range(start, end)):
            si = str(i)
            new_image = Image.new("RGB", (((len(si) * iw) + ((len(si)-1) * s)), ih), ORANGE.color)
            for j, ci in enumerate(si):
                new_image.paste(nums[int(ci)], (j * (iw + s), 0), nums[int(ci)])  
            enhancer = ImageEnhance.Contrast(new_image)
            enchancer2 = ImageEnhance.Brightness(enhancer.enhance(.5))
            enchancer2.enhance(.5).save(f"nums/generated/{si}-dark.png", "PNG")

def generate_dark_decimal(start, end):
    for i in tqdm(range(start, end)):
        si = str(i)
        if len(si) == 2: si = "0" + si
        new_image = Image.new("RGB", (((len(si) * iw) + ((len(si)-1) * s)), ih), ORANGE.color)
        for j, ci in enumerate(si[:-2]):
            new_image.paste(nums[int(ci)], (j * (iw + s), 0), nums[int(ci)])
        new_image.paste(nums[-1], ((len(si) - 3) * (iw + s) + decimal_offset, 0), nums[-1])
        for j, ci in enumerate(si[-2:], len(si)-2):
            new_image.paste(nums[int(ci)], (j * (iw + s), 0), nums[int(ci)])
        enhancer = ImageEnhance.Contrast(new_image)
        enchancer2 = ImageEnhance.Brightness(enhancer.enhance(.5))
        enchancer2.enhance(.5).save(f"nums/generated/{si[:-2]}.{si[-2:]}-dark.png", "PNG")

generate_dark(10, 10001)
generate_dark_decimal(10, 10001)