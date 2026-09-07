import qrcode
from PIL import Image, ImageDraw, ImageFont

# Live Vercel Production URLs
html_url = "https://looks-salon-patna.vercel.app/service_menu.html"
pdf_url = "https://looks-salon-patna.vercel.app/Looks%20Salon%20-%20Complete%20Service%20Menu.pdf"

print(f"Vercel Live Web URL: {html_url}")
print(f"Vercel Live PDF URL: {pdf_url}")

# 1. Generate standalone QR codes targeting Vercel
qr_pdf = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=12, border=2)
qr_pdf.add_data(pdf_url)
qr_pdf.make(fit=True)
img_pdf_qr = qr_pdf.make_image(fill_color="#000000", back_color="#FFFFFF").convert('RGB')
img_pdf_qr.save("standalone_qr_pdf.png")

qr_html = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=12, border=2)
qr_html.add_data(html_url)
qr_html.make(fit=True)
img_html_qr = qr_html.make_image(fill_color="#000000", back_color="#FFFFFF").convert('RGB')
img_html_qr.save("standalone_qr_html.png")

# 2. Create combined luxury display poster image
canvas_width = 1200
canvas_height = 800
background_color = (15, 15, 15)  # Dark sleek charcoal
gold_color = (212, 175, 55)      # Metallic Gold
white_color = (255, 255, 255)
gray_color = (180, 180, 180)

canvas = Image.new("RGB", (canvas_width, canvas_height), background_color)
draw = ImageDraw.Draw(canvas)

# Double gold border
draw.rectangle([20, 20, canvas_width - 20, canvas_height - 20], outline=gold_color, width=3)
draw.rectangle([28, 28, canvas_width - 28, canvas_height - 28], outline=gold_color, width=1)

# Fonts
try:
    title_font = ImageFont.truetype("arialbd.ttf", 42)
    subtitle_font = ImageFont.truetype("arial.ttf", 22)
    card_title_font = ImageFont.truetype("arialbd.ttf", 26)
    card_sub_font = ImageFont.truetype("arial.ttf", 18)
except:
    title_font = subtitle_font = card_title_font = card_sub_font = ImageFont.load_default()

# Header text
draw.text((canvas_width // 2, 70), "LOOKS SALON", fill=gold_color, font=title_font, anchor="mm")
draw.text((canvas_width // 2, 115), "KANKARBAGH, PATNA • DIGITAL SERVICE MENU", fill=white_color, font=subtitle_font, anchor="mm")

# Prepare QR cards
qr_size = 320
pdf_qr_resized = img_pdf_qr.resize((qr_size, qr_size))
html_qr_resized = img_html_qr.resize((qr_size, qr_size))

# Left Card (PDF QR)
left_cx = 330
card_top = 170
card_w = 440
card_h = 540

draw.rectangle([left_cx - card_w//2, card_top, left_cx + card_w//2, card_top + card_h], fill=(25, 25, 25), outline=gold_color, width=2)
canvas.paste(pdf_qr_resized, (left_cx - qr_size//2, card_top + 40))

draw.text((left_cx, card_top + 400), "📄 PDF MENU", fill=gold_color, font=card_title_font, anchor="mm")
draw.text((left_cx, card_top + 440), "Scan to Download / Print PDF Menu", fill=white_color, font=card_sub_font, anchor="mm")
draw.text((left_cx, card_top + 475), "Direct Vercel Host", fill=gray_color, font=card_sub_font, anchor="mm")

# Right Card (Web HTML QR)
right_cx = 870
draw.rectangle([right_cx - card_w//2, card_top, right_cx + card_w//2, card_top + card_h], fill=(25, 25, 25), outline=gold_color, width=2)
canvas.paste(html_qr_resized, (right_cx - qr_size//2, card_top + 40))

draw.text((right_cx, card_top + 400), "🌐 INTERACTIVE WEB MENU", fill=gold_color, font=card_title_font, anchor="mm")
draw.text((right_cx, card_top + 440), "Scan to Open Live Mobile Web Menu", fill=white_color, font=card_sub_font, anchor="mm")
draw.text((right_cx, card_top + 475), "Optimized for Smartphones", fill=gray_color, font=card_sub_font, anchor="mm")

canvas.save("LOOKS_SALON_QR_CODES.png")
print("Saved Vercel-linked LOOKS_SALON_QR_CODES.png successfully!")
