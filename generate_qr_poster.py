import qrcode
from PIL import Image, ImageDraw, ImageFont

# Live PDF Menu URL
pdf_url = "https://looks-salon-patna.vercel.app/Looks%20Salon%20-%20Complete%20Service%20Menu.pdf"

print(f"Target PDF URL: {pdf_url}")

# 1. Generate standalone high-res QR code for PDF
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=16, border=2)
qr.add_data(pdf_url)
qr.make(fit=True)
img_pdf_qr = qr.make_image(fill_color="#000000", back_color="#FFFFFF").convert('RGB')
img_pdf_qr.save("standalone_qr_pdf.png")

# 2. Create clean, centered luxury display card
canvas_width = 1000
canvas_height = 900
background_color = (13, 12, 10)  # Deep Charcoal Obsidian
gold_color = (212, 175, 55)      # Metallic Gold
gold_light = (235, 205, 120)
white_color = (250, 248, 245)
gray_color = (175, 170, 160)
card_bg = (22, 20, 17)

canvas = Image.new("RGB", (canvas_width, canvas_height), background_color)
draw = ImageDraw.Draw(canvas)

# Elegant double gold border with margin
draw.rectangle([18, 18, canvas_width - 18, canvas_height - 18], outline=gold_color, width=2)
draw.rectangle([25, 25, canvas_width - 25, canvas_height - 25], outline=(150, 120, 40), width=1)

# Corner accents
acc_len = 30
# TL
draw.line([(25, 25), (25 + acc_len, 25)], fill=gold_light, width=3)
draw.line([(25, 25), (25, 25 + acc_len)], fill=gold_light, width=3)
# TR
draw.line([(canvas_width - 25, 25), (canvas_width - 25 - acc_len, 25)], fill=gold_light, width=3)
draw.line([(canvas_width - 25, 25), (canvas_width - 25, 25 + acc_len)], fill=gold_light, width=3)
# BL
draw.line([(25, canvas_height - 25), (25 + acc_len, canvas_height - 25)], fill=gold_light, width=3)
draw.line([(25, canvas_height - 25), (25, canvas_height - 25 - acc_len)], fill=gold_light, width=3)
# BR
draw.line([(canvas_width - 25, canvas_height - 25), (canvas_width - 25 - acc_len, canvas_height - 25)], fill=gold_light, width=3)
draw.line([(canvas_width - 25, canvas_height - 25), (canvas_width - 25, canvas_height - 25 - acc_len)], fill=gold_light, width=3)

# Fonts
try:
    title_font = ImageFont.truetype("arialbd.ttf", 40)
    subtitle_font = ImageFont.truetype("arialbd.ttf", 18)
    card_title_font = ImageFont.truetype("arialbd.ttf", 26)
    card_sub_font = ImageFont.truetype("arial.ttf", 19)
    footer_font = ImageFont.truetype("arial.ttf", 15)
except:
    title_font = subtitle_font = card_title_font = card_sub_font = footer_font = ImageFont.load_default()

# Header text
draw.text((canvas_width // 2, 70), "LOOKS SALON", fill=gold_color, font=title_font, anchor="mm")
draw.text((canvas_width // 2, 115), "KANKARBAGH, PATNA • DIGITAL SERVICE MENU", fill=white_color, font=subtitle_font, anchor="mm")

# Center Card
cx = canvas_width // 2
card_w = 580
card_h = 600
card_top = 160

# Card background & border
draw.rectangle([cx - card_w//2, card_top, cx + card_w//2, card_top + card_h], fill=card_bg, outline=gold_color, width=2)
draw.rectangle([cx - card_w//2 + 5, card_top + 5, cx + card_w//2 - 5, card_top + card_h - 5], outline=(80, 65, 25), width=1)

# QR Code inside Card
qr_size = 360
pdf_qr_resized = img_pdf_qr.resize((qr_size, qr_size))
canvas.paste(pdf_qr_resized, (cx - qr_size//2, card_top + 45))

# Scan instruction text below QR
draw.text((cx, card_top + 450), "COMPLETE SERVICE MENU", fill=gold_color, font=card_title_font, anchor="mm")
draw.text((cx, card_top + 490), "Scan with any smartphone camera", fill=white_color, font=card_sub_font, anchor="mm")
draw.text((cx, card_top + 525), "Instant access to all hair, skin & spa prices", fill=gray_color, font=card_sub_font, anchor="mm")

# Service highlights row
services_text = "HAIR CUT  •  COLOR & KERATIN  •  LUXURY FACIALS  •  SPA RITUALS  •  PEDICURE & WAX"
draw.text((cx, card_top + 565), services_text, fill=gold_light, font=footer_font, anchor="mm")

# Bottom Location details
draw.line([(60, canvas_height - 95), (canvas_width - 60, canvas_height - 95)], fill=(60, 50, 25), width=1)
draw.text((cx, canvas_height - 65), "B-184, Vidya Enclave, P.C. Colony, Next to Lohiya Park, Kankarbagh, Patna", fill=white_color, font=footer_font, anchor="mm")
draw.text((cx, canvas_height - 40), "Call: +91 77838 65018 | +91 62877 61333   •   Open 7 Days: 9:00 AM – 9:00 PM", fill=gold_color, font=footer_font, anchor="mm")

canvas.save("LOOKS_SALON_QR_CODES.png")
print("Saved clean, single-QR LOOKS_SALON_QR_CODES.png successfully!")
