from PIL import Image
import sys

img_path = sys.argv[1]
out_path = sys.argv[2]

img = Image.open(img_path).convert("RGB")

# Target dimensions
t_w, t_h = 1200, 630

# Calculate new size maintaining aspect ratio for height 630
new_w = int(img.width * (t_h / img.height))
img_resized = img.resize((new_w, t_h), Image.Resampling.LANCZOS)

# Create new image
new_img = Image.new("RGB", (t_w, t_h))

# Paste resized image into center
offset_x = (t_w - new_w) // 2
new_img.paste(img_resized, (offset_x, 0))

# Extend left edge
left_edge = img_resized.crop((0, 0, 1, t_h))
for x in range(offset_x):
    new_img.paste(left_edge, (x, 0))

# Extend right edge
right_edge = img_resized.crop((new_w - 1, 0, new_w, t_h))
for x in range(offset_x + new_w, t_w):
    new_img.paste(right_edge, (x, 0))

new_img.save(out_path)
print("Image successfully resized and padded.")
