import os
import re
import qrcode
from PIL import Image, ImageDraw

# 1. Generate QR Code 1 for PDF redirect
qr1 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=8,
    border=2,
)
# PDF URL / Redirect
qr1.add_data('https://lookssalon.in/kankarbagh-patna-menu.pdf')
qr1.make(fit=True)
img_qr1 = qr1.make_image(fill_color='#0b0b0d', back_color='#f6e6b8').convert('RGBA')
img_qr1.save('qr_pdf.png')

# 2. Generate QR Code 2 for HTML web menu redirect
qr2 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=8,
    border=2,
)
# HTML URL / Redirect
qr2.add_data('https://lookssalon.in/kankarbagh-patna-menu.html')
qr2.make(fit=True)
img_qr2 = qr2.make_image(fill_color='#0b0b0d', back_color='#f6e6b8').convert('RGBA')
img_qr2.save('qr_html.png')

print("Generated qr_pdf.png and qr_html.png successfully!")

# Load the SVG logo
with open('Big_Logo.svg', 'r', encoding='utf-8') as f:
    svg_raw = f.read()

# Make the SVG responsive by removing hardcoded width/height and adding style
svg_clean = re.sub(r'width="\d+px"', 'width="100%"', svg_raw)
svg_clean = re.sub(r'height="\d+px"', 'height="100%"', svg_clean)
svg_clean = svg_clean.replace('<?xml version="1.0" encoding="utf-8"?>', '')
svg_clean = svg_clean.replace('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">', '')

# SVG Icons for Footer
ICON_PIN = '''<svg width="12" height="12" viewBox="0 0 24 24" fill="#d4af37" style="flex-shrink:0; margin-top: 1px;"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>'''
ICON_PHONE = '''<svg width="11" height="11" viewBox="0 0 24 24" fill="#d4af37" style="flex-shrink:0;"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>'''
ICON_MAIL = '''<svg width="11" height="11" viewBox="0 0 24 24" fill="#d4af37" style="flex-shrink:0;"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>'''
ICON_CLOCK = '''<svg width="11" height="11" viewBox="0 0 24 24" fill="#d4af37" style="flex-shrink:0;"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>'''
ICON_INSTA = '''<svg width="11" height="11" viewBox="0 0 24 24" fill="#d4af37" style="flex-shrink:0;"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>'''

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Looks Salon - Complete Service Menu | Kankarbagh Patna</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..800;1,6..96,400..800&family=Manrope:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  @page {{
    size: A4 portrait;
    margin: 0;
  }}

  body {{
    background-color: #0b0b0d;
    color: #e6e2dd;
    font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  .page {{
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    page-break-after: always;
    page-break-inside: avoid;
    position: relative;
    overflow: hidden;
    background: radial-gradient(circle at 50% 20%, #171513 0%, #0c0c0e 65%, #070708 100%);
    padding: 13mm 14mm 11mm 14mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  /* Double Golden Luxury Border */
  .page-border {{
    position: absolute;
    top: 5mm;
    left: 5mm;
    right: 5mm;
    bottom: 5mm;
    border: 1px solid rgba(212, 175, 55, 0.32);
    pointer-events: none;
  }}
  .page-border::after {{
    content: '';
    position: absolute;
    top: 1.8mm;
    left: 1.8mm;
    right: 1.8mm;
    bottom: 1.8mm;
    border: 1px solid rgba(212, 175, 55, 0.14);
    pointer-events: none;
  }}

  /* Header Bar */
  .page-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(212, 175, 55, 0.22);
    padding-bottom: 2.8mm;
    margin-bottom: 3.2mm;
    position: relative;
    z-index: 2;
  }}

  .header-left {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}

  .header-badge {{
    font-family: 'Bodoni Moda', serif;
    font-size: 1.05rem;
    font-weight: 600;
    color: #d4af37;
    border: 1px solid rgba(212, 175, 55, 0.45);
    padding: 1px 9px;
    letter-spacing: 1px;
    background: rgba(212, 175, 55, 0.08);
  }}

  .header-title-group h2 {{
    font-family: 'Bodoni Moda', serif;
    font-size: 1.25rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #fdfcfb;
    line-height: 1.1;
  }}
  .header-title-group p {{
    font-size: 0.62rem;
    letter-spacing: 2.2px;
    text-transform: uppercase;
    color: #c5a059;
    margin-top: 1.5px;
    font-weight: 500;
  }}

  .header-right {{
    text-align: right;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 2px;
  }}
  .header-logo-container {{
    width: 90px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
  }}
  .header-tag {{
    font-size: 0.55rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #9e9a93;
    font-weight: 500;
  }}

  /* Page Footer */
  .page-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(212, 175, 55, 0.2);
    padding-top: 2.5mm;
    margin-top: 2.5mm;
    font-size: 0.6rem;
    color: #8c8880;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    position: relative;
    z-index: 2;
  }}
  .footer-center {{
    color: #c5a059;
    font-weight: 600;
    letter-spacing: 3px;
  }}

  /* Content Grid */
  .content-body {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    gap: 3mm;
    position: relative;
    z-index: 2;
  }}

  .grid-2col {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4mm;
    align-items: stretch;
  }}

  /* Menu Cards */
  .menu-card {{
    background: rgba(20, 18, 16, 0.72);
    border: 1px solid rgba(212, 175, 55, 0.18);
    border-radius: 4px;
    padding: 3.2mm 4mm;
    display: flex;
    flex-direction: column;
    gap: 1.8mm;
    backdrop-filter: blur(4px);
    box-shadow: 0 4px 14px rgba(0,0,0,0.3);
  }}

  .card-header {{
    border-bottom: 1px solid rgba(212, 175, 55, 0.16);
    padding-bottom: 1.8mm;
    margin-bottom: 0.8mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
  }}
  .card-title {{
    font-family: 'Bodoni Moda', serif;
    font-size: 0.95rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #d4af37;
    white-space: nowrap;
  }}
  .card-subtitle-badge {{
    font-size: 0.52rem;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #a8a49d;
    background: rgba(212, 175, 55, 0.06);
    border: 1px solid rgba(212, 175, 55, 0.2);
    padding: 2px 7px;
    border-radius: 2px;
    white-space: nowrap;
    font-weight: 600;
  }}

  .section-label {{
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    color: #e5c07b;
    margin-top: 1.4mm;
    margin-bottom: 0.6mm;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .section-label::after {{
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(212, 175, 55, 0.15);
  }}

  /* Service Rows */
  .service-list {{
    display: flex;
    flex-direction: column;
    gap: 1.35mm;
  }}

  .service-item {{
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    font-size: 0.69rem;
    line-height: 1.25;
  }}
  .service-name {{
    color: #e8e4df;
    font-weight: 400;
    white-space: nowrap;
  }}
  .service-dots {{
    flex: 1;
    border-bottom: 1px dotted rgba(212, 175, 55, 0.22);
    margin: 0 5px;
    transform: translateY(-2px);
  }}
  .service-price {{
    color: #f1dfa8;
    font-weight: 600;
    font-variant-numeric: tabular-nums;
    white-space: nowrap;
    letter-spacing: 0.5px;
  }}

  /* Dual price table for Kerastase */
  .table-header-row {{
    display: flex;
    align-items: baseline;
    font-size: 0.58rem;
    font-weight: 700;
    color: #c5a059;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding-bottom: 0.8mm;
    border-bottom: 1px dashed rgba(212, 175, 55, 0.2);
    margin-bottom: 0.8mm;
  }}
  .table-item-row {{
    display: flex;
    align-items: baseline;
    font-size: 0.67rem;
    line-height: 1.35;
  }}
  .col-name {{
    flex: 1;
    color: #e8e4df;
  }}
  .col-price {{
    width: 14mm;
    text-align: right;
    color: #f1dfa8;
    font-weight: 600;
  }}

  /* COVER PAGE STYLES */
  .cover-container {{
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    text-align: center;
    padding: 16mm 10mm 12mm 10mm;
    position: relative;
    z-index: 2;
  }}

  .cover-top-tag {{
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 6px;
    text-transform: uppercase;
    color: #d4af37;
    display: inline-block;
    padding: 3px 22px;
    border-top: 1px solid rgba(212, 175, 55, 0.4);
    border-bottom: 1px solid rgba(212, 175, 55, 0.4);
  }}

  .cover-center-content {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 3mm;
    width: 100%;
  }}

  .cover-logo-box {{
    width: 240px;
    height: 95px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 3mm auto;
    filter: drop-shadow(0 4px 20px rgba(0,0,0,0.9));
  }}

  .cover-title-group {{
    margin-top: 2mm;
  }}
  .cover-subtitle {{
    font-size: 0.82rem;
    letter-spacing: 5px;
    text-transform: uppercase;
    color: #c5a059;
    font-weight: 600;
    margin-bottom: 3.5mm;
  }}
  .cover-main-title {{
    font-family: 'Bodoni Moda', serif;
    font-size: 3rem;
    font-weight: 500;
    letter-spacing: 0.5px;
    line-height: 1.15;
    color: #ffffff;
    text-shadow: 0 4px 24px rgba(0,0,0,0.8);
    margin-bottom: 4mm;
  }}
  .cover-divider {{
    width: 90px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #d4af37, transparent);
    margin: 5mm auto 4mm auto;
  }}
  .cover-services-list {{
    font-size: 0.82rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #dfdcd7;
    font-weight: 500;
  }}

  .cover-location-badge {{
    background: rgba(212, 175, 55, 0.07);
    border: 1px solid rgba(212, 175, 55, 0.38);
    padding: 5mm 10mm;
    border-radius: 4px;
    width: 140mm;
    margin: 5mm auto 0 auto;
    box-shadow: 0 4px 16px rgba(0,0,0,0.35);
  }}
  .cover-branch-name {{
    font-family: 'Bodoni Moda', serif;
    font-size: 1.15rem;
    letter-spacing: 3px;
    color: #f6e6b8;
    text-transform: uppercase;
    margin-bottom: 1.5mm;
  }}
  .cover-branch-sub {{
    font-size: 0.68rem;
    letter-spacing: 1.4px;
    color: #b8b3ab;
  }}

  .cover-footer-note {{
    font-size: 0.62rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #8c8880;
  }}

  /* CUSTOM PATNA FOOTER CARD (Page 5) */
  .patna-footer-card {{
    background: linear-gradient(135deg, rgba(28, 25, 22, 0.92) 0%, rgba(16, 14, 13, 0.97) 100%);
    border: 1px solid rgba(212, 175, 55, 0.45);
    border-radius: 4px;
    padding: 3mm 4.5mm;
    margin-top: 1.5mm;
    box-shadow: 0 6px 20px rgba(0,0,0,0.45);
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 4mm;
  }}

  .pfc-left {{
    flex: 1.1;
    border-right: 1px solid rgba(212, 175, 55, 0.2);
    padding-right: 3.5mm;
  }}
  .pfc-brand {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 1.5mm;
  }}
  .pfc-brand-title {{
    font-family: 'Bodoni Moda', serif;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #f1dfa8;
    text-transform: uppercase;
  }}
  .pfc-branch-pill {{
    font-size: 0.52rem;
    font-weight: 700;
    letter-spacing: 1px;
    background: #d4af37;
    color: #0b0a08;
    padding: 1px 5px;
    border-radius: 2px;
    text-transform: uppercase;
  }}
  .pfc-address {{
    font-size: 0.62rem;
    line-height: 1.35;
    color: #d1ceca;
    display: flex;
    align-items: flex-start;
    gap: 5px;
  }}
  .pfc-address-text strong {{
    color: #f8f6f4;
  }}

  .pfc-middle {{
    flex: 1.1;
    border-right: 1px solid rgba(212, 175, 55, 0.2);
    padding-right: 3.5mm;
  }}
  .pfc-contact-line {{
    font-size: 0.62rem;
    line-height: 1.4;
    color: #e0dcd6;
    display: flex;
    align-items: center;
    gap: 5px;
  }}
  .pfc-hours {{
    margin-top: 1.5mm;
    font-size: 0.58rem;
    color: #b5b0a6;
    display: flex;
    align-items: center;
    gap: 5px;
  }}
  .pfc-hours strong {{
    color: #e5c07b;
  }}

  .pfc-right-qr {{
    flex: 1.1;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 3.5mm;
  }}

  .qr-box {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    background: rgba(212, 175, 55, 0.04);
    border: 1px solid rgba(212, 175, 55, 0.3);
    border-radius: 3px;
    padding: 1.8mm 2.2mm 1.5mm 2.2mm;
  }}
  .qr-img {{
    width: 48px;
    height: 48px;
    border-radius: 2px;
    margin-bottom: 1.2mm;
    box-shadow: 0 2px 6px rgba(0,0,0,0.5);
  }}
  .qr-label {{
    font-size: 0.5rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    color: #f1dfa8;
  }}
  .qr-sub {{
    font-size: 0.44rem;
    letter-spacing: 0.5px;
    color: #b8b3ab;
    margin-top: 0.5px;
  }}
</style>
</head>
<body>

<!-- ========================================== -->
<!-- PAGE 1: COVER PAGE                         -->
<!-- ========================================== -->
<section class="page" id="page-1">
  <div class="page-border"></div>

  <div class="cover-container">
    <div class="cover-top-tag">L O O K S &nbsp;&bull;&nbsp; S A L O N</div>

    <div class="cover-center-content">
      <div class="cover-logo-box">
        {svg_clean}
      </div>

      <div class="cover-title-group">
        <div class="cover-subtitle">COMPLETE SERVICE MENU</div>
        <h1 class="cover-main-title">The Full Experience</h1>
        <div class="cover-divider"></div>
        <div class="cover-services-list">HAIR &nbsp;&bull;&nbsp; SKIN &nbsp;&bull;&nbsp; SPA &nbsp;&bull;&nbsp; GROOMING</div>
      </div>

      <div class="cover-location-badge">
        <div class="cover-branch-name">KANKARBAGH, PATNA</div>
        <div class="cover-branch-sub">B-184, Vidya Enclave, P.C. Colony, Next to Lohiya Park</div>
        <div class="cover-branch-sub" style="margin-top: 2mm; color: #d4af37; font-weight: 600; letter-spacing: 1.8px;">
          Direct Bookings: +91 77838 65018 &nbsp;|&nbsp; +91 62877 61333
        </div>
      </div>
    </div>

    <div class="cover-footer-note">PRICES IN INDIAN RUPEES (&#8377;) &nbsp;&bull;&nbsp; TAXES APPLICABLE &nbsp;&bull;&nbsp; SUBJECT TO CHANGE</div>
  </div>
</section>

<!-- ========================================== -->
<!-- PAGE 2: HAIR & GROOMING (HIM & HER)        -->
<!-- ========================================== -->
<section class="page" id="page-2">
  <div class="page-border"></div>

  <header class="page-header">
    <div class="header-left">
      <span class="header-badge">01</span>
      <div class="header-title-group">
        <h2>Hair & Grooming</h2>
        <p>GENTLEMEN'S GROOMING & LADIES' STYLING</p>
      </div>
    </div>
    <div class="header-right">
      <div class="header-logo-container">
        {svg_clean}
      </div>
      <span class="header-tag">KANKARBAGH, PATNA</span>
    </div>
  </header>

  <div class="content-body">
    <div class="grid-2col">
      <!-- COLUMN 1: FOR HIM -->
      <div class="menu-card">
        <div class="card-header">
          <span class="card-title">For Him</span>
          <span class="card-subtitle-badge">Gentlemen</span>
        </div>

        <div class="section-label">Cut & Care</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Hair Cut</span><span class="service-dots"></span><span class="service-price">₹500</span></div>
          <div class="service-item"><span class="service-name">Child Hair Cut (0–5)</span><span class="service-dots"></span><span class="service-price">₹400</span></div>
          <div class="service-item"><span class="service-name">Creative Hair Cut</span><span class="service-dots"></span><span class="service-price">₹550</span></div>
        </div>

        <div class="section-label">Beard Care</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Shave</span><span class="service-dots"></span><span class="service-price">₹300</span></div>
          <div class="service-item"><span class="service-name">Beard Trim</span><span class="service-dots"></span><span class="service-price">₹400</span></div>
          <div class="service-item"><span class="service-name">Beard Styling</span><span class="service-dots"></span><span class="service-price">₹500</span></div>
          <div class="service-item"><span class="service-name">Beard Colour</span><span class="service-dots"></span><span class="service-price">₹700</span></div>
        </div>

        <div class="section-label">Hair Care</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Hair Wash</span><span class="service-dots"></span><span class="service-price">₹150</span></div>
          <div class="service-item"><span class="service-name">Conditioner</span><span class="service-dots"></span><span class="service-price">₹150</span></div>
          <div class="service-item"><span class="service-name">Wash & Conditioner</span><span class="service-dots"></span><span class="service-price">₹300</span></div>
          <div class="service-item"><span class="service-name">Hair Wash (K)</span><span class="service-dots"></span><span class="service-price">₹250</span></div>
          <div class="service-item"><span class="service-name">Hair Wash & Condition (K)</span><span class="service-dots"></span><span class="service-price">₹700</span></div>
          <div class="service-item"><span class="service-name">Head Massage (30 mins)</span><span class="service-dots"></span><span class="service-price">₹600</span></div>
        </div>

        <div class="section-label">Hair Colour</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Hair Colour</span><span class="service-dots"></span><span class="service-price">₹1,300</span></div>
          <div class="service-item"><span class="service-name">Hair Colour – Ammonia Free</span><span class="service-dots"></span><span class="service-price">₹1,400</span></div>
          <div class="service-item"><span class="service-name">Hi-Lites</span><span class="service-dots"></span><span class="service-price">₹2,500</span></div>
        </div>

        <div class="section-label">Hair Texture</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Straightening</span><span class="service-dots"></span><span class="service-price">₹4,000</span></div>
          <div class="service-item"><span class="service-name">Smoothening</span><span class="service-dots"></span><span class="service-price">₹4,000</span></div>
          <div class="service-item"><span class="service-name">Rebonding</span><span class="service-dots"></span><span class="service-price">₹4,000</span></div>
          <div class="service-item"><span class="service-name">Keratine</span><span class="service-dots"></span><span class="service-price">₹4,000</span></div>
        </div>
      </div>

      <!-- COLUMN 2: FOR HER -->
      <div class="menu-card">
        <div class="card-header">
          <span class="card-title">For Her</span>
          <span class="card-subtitle-badge">Ladies</span>
        </div>

        <div class="section-label">Cut & Style</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Hair Cut</span><span class="service-dots"></span><span class="service-price">₹900</span></div>
          <div class="service-item"><span class="service-name">Hair Cut – Child (0–5)</span><span class="service-dots"></span><span class="service-price">₹600</span></div>
          <div class="service-item"><span class="service-name">Creative Hair Cut</span><span class="service-dots"></span><span class="service-price">₹1,200</span></div>
        </div>

        <div class="section-label">Hair Care</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Hair Wash</span><span class="service-dots"></span><span class="service-price">₹200</span></div>
          <div class="service-item"><span class="service-name">Conditioner</span><span class="service-dots"></span><span class="service-price">₹200</span></div>
          <div class="service-item"><span class="service-name">Hair Wash & Conditioner</span><span class="service-dots"></span><span class="service-price">₹400</span></div>
          <div class="service-item"><span class="service-name">Hair Wash (K)</span><span class="service-dots"></span><span class="service-price">₹350</span></div>
          <div class="service-item"><span class="service-name">Conditioner (K)</span><span class="service-dots"></span><span class="service-price">₹350</span></div>
          <div class="service-item"><span class="service-name">Hair Wash & Conditioner (K)</span><span class="service-dots"></span><span class="service-price">₹700</span></div>
          <div class="service-item"><span class="service-name">Head Massage (30 mins)</span><span class="service-dots"></span><span class="service-price">₹600</span></div>
        </div>

        <div class="section-label">Hair Styling</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Blow Dry Straight</span><span class="service-dots"></span><span class="service-price">₹500</span></div>
          <div class="service-item"><span class="service-name">Ironing</span><span class="service-dots"></span><span class="service-price">₹800</span></div>
          <div class="service-item"><span class="service-name">Tong Curls</span><span class="service-dots"></span><span class="service-price">₹1,000</span></div>
          <div class="service-item"><span class="service-name">Hair Set & Upstyle</span><span class="service-dots"></span><span class="service-price">₹1,500</span></div>
        </div>

        <div class="section-label">Hair Colour</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Root Touch Up</span><span class="service-dots"></span><span class="service-price">₹1,400</span></div>
          <div class="service-item"><span class="service-name">Root Touch Up – Ammonia Free</span><span class="service-dots"></span><span class="service-price">₹1,500</span></div>
          <div class="service-item"><span class="service-name">Global Hair Colour</span><span class="service-dots"></span><span class="service-price">₹5,000</span></div>
          <div class="service-item"><span class="service-name">Global Colour w/ Bond Prot.</span><span class="service-dots"></span><span class="service-price">₹6,000</span></div>
          <div class="service-item"><span class="service-name">Hi-Lites</span><span class="service-dots"></span><span class="service-price">₹6,500</span></div>
          <div class="service-item"><span class="service-name">Balayage</span><span class="service-dots"></span><span class="service-price">₹6,500</span></div>
          <div class="service-item"><span class="service-name">French Balayage</span><span class="service-dots"></span><span class="service-price">₹7,500</span></div>
        </div>

        <div class="section-label">Hair Texture</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Smoothening</span><span class="service-dots"></span><span class="service-price">₹7,000</span></div>
          <div class="service-item"><span class="service-name">Keratin Treatment</span><span class="service-dots"></span><span class="service-price">₹7,000</span></div>
          <div class="service-item"><span class="service-name">Botox</span><span class="service-dots"></span><span class="service-price">₹7,000</span></div>
        </div>
      </div>
    </div>
  </div>

  <footer class="page-footer">
    <span>LOOKS SALON &nbsp;&bull;&nbsp; COMPLETE SERVICE MENU</span>
    <span class="footer-center">L O O K S &nbsp;&bull;&nbsp; S A L O N</span>
    <span>PAGE 02</span>
  </footer>
</section>

<!-- ========================================== -->
<!-- PAGE 3: HAIR RITUALS & KÉRASTASE PARIS     -->
<!-- ========================================== -->
<section class="page" id="page-3">
  <div class="page-border"></div>

  <header class="page-header">
    <div class="header-left">
      <span class="header-badge">02</span>
      <div class="header-title-group">
        <h2>Hair Rituals & Kérastase</h2>
        <p>RESTORATIVE SPA & SIGNATURE DIAGNOSTIC CARE</p>
      </div>
    </div>
    <div class="header-right">
      <div class="header-logo-container">
        {svg_clean}
      </div>
      <span class="header-tag">KANKARBAGH, PATNA</span>
    </div>
  </header>

  <div class="content-body">
    <div class="grid-2col">
      <!-- COLUMN 1: RESTORATIVE RITUALS (GENTS & LADIES) -->
      <div class="menu-card">
        <div class="card-header">
          <span class="card-title">Hair & Scalp</span>
          <span class="card-subtitle-badge">Restorative</span>
        </div>

        <div class="section-label">Gents Rituals</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Hair Spa</span><span class="service-dots"></span><span class="service-price">₹1,200</span></div>
          <div class="service-item"><span class="service-name">Dry Damaged Hair</span><span class="service-dots"></span><span class="service-price">₹1,200</span></div>
          <div class="service-item"><span class="service-name">Frizzy & Unruly Hair</span><span class="service-dots"></span><span class="service-price">₹1,200</span></div>
          <div class="service-item"><span class="service-name">Chemically Treated Hair</span><span class="service-dots"></span><span class="service-price">₹1,200</span></div>
          <div class="service-item"><span class="service-name">Clear Dose</span><span class="service-dots"></span><span class="service-price">₹600</span></div>
          <div class="service-item"><span class="service-name">Inner Spa</span><span class="service-dots"></span><span class="service-price">₹600</span></div>
          <div class="service-item"><span class="service-name">Scalp Soothing</span><span class="service-dots"></span><span class="service-price">₹1,200</span></div>
          <div class="service-item"><span class="service-name">Advanced Hair Moisture</span><span class="service-dots"></span><span class="service-price">₹1,200</span></div>
          <div class="service-item"><span class="service-name">Moroccan Quickie</span><span class="service-dots"></span><span class="service-price">₹1,500</span></div>
          <div class="service-item"><span class="service-name">Moroccan Super Charge</span><span class="service-dots"></span><span class="service-price">₹1,800</span></div>
          <div class="service-item"><span class="service-name">Biotop Express</span><span class="service-dots"></span><span class="service-price">₹2,500</span></div>
          <div class="service-item"><span class="service-name">Biotop</span><span class="service-dots"></span><span class="service-price">₹3,500</span></div>
        </div>

        <div class="section-label">Ladies Rituals</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Hair Spa</span><span class="service-dots"></span><span class="service-price">₹1,500</span></div>
          <div class="service-item"><span class="service-name">Dry Damaged Hair</span><span class="service-dots"></span><span class="service-price">₹1,500</span></div>
          <div class="service-item"><span class="service-name">Frizzy & Unruly Hair</span><span class="service-dots"></span><span class="service-price">₹2,000</span></div>
          <div class="service-item"><span class="service-name">Chemically Treated Hair</span><span class="service-dots"></span><span class="service-price">₹2,000</span></div>
          <div class="service-item"><span class="service-name">Clear Dose</span><span class="service-dots"></span><span class="service-price">₹600</span></div>
          <div class="service-item"><span class="service-name">Inner Spa</span><span class="service-dots"></span><span class="service-price">₹600</span></div>
          <div class="service-item"><span class="service-name">Scalp Soothing</span><span class="service-dots"></span><span class="service-price">₹1,500</span></div>
          <div class="service-item"><span class="service-name">Advanced Hair Moisture</span><span class="service-dots"></span><span class="service-price">₹1,500</span></div>
          <div class="service-item"><span class="service-name">Moroccan Quickie</span><span class="service-dots"></span><span class="service-price">₹3,000</span></div>
          <div class="service-item"><span class="service-name">Moroccan Super Charge</span><span class="service-dots"></span><span class="service-price">₹3,000</span></div>
          <div class="service-item"><span class="service-name">Biotop Express</span><span class="service-dots"></span><span class="service-price">₹2,500</span></div>
          <div class="service-item"><span class="service-name">Biotop</span><span class="service-dots"></span><span class="service-price">₹3,500</span></div>
        </div>
      </div>

      <!-- COLUMN 2: KÉRASTASE SIGNATURE RITUALS -->
      <div class="menu-card">
        <div class="card-header">
          <span class="card-title">Kérastase Paris</span>
          <span class="card-subtitle-badge">Diagnostic</span>
        </div>

        <div class="section-label">Recruiter Ritual — 15 Mins</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Fusio Scrub Instant Detox</span><span class="service-dots"></span><span class="service-price">₹2,200</span></div>
          <div class="service-item"><span class="service-name">Instant Conditioning Ritual (Fusio Dose)</span><span class="service-dots"></span><span class="service-price">₹2,200</span></div>
        </div>

        <div class="section-label" style="justify-content: space-between;">
          <span>Experience Rituals</span>
          <span style="font-size: 0.52rem; color: #f1dfa8;">30 MIN &nbsp;/&nbsp; 60 MIN</span>
        </div>
        
        <div class="table-header-row">
          <span class="col-name">Specialized Diagnostic Focus</span>
          <span class="col-price">30M</span>
          <span class="col-price">60M</span>
        </div>

        <div class="service-list">
          <div class="table-item-row"><span class="col-name">Discipline</span><span class="col-price">₹3,500</span><span class="col-price">₹4,500</span></div>
          <div class="table-item-row"><span class="col-name">Curl Manifesto</span><span class="col-price">₹3,500</span><span class="col-price">₹4,500</span></div>
          <div class="table-item-row"><span class="col-name">Volume Control & Smoothening</span><span class="col-price">₹3,500</span><span class="col-price">₹4,500</span></div>
          <div class="table-item-row"><span class="col-name">Colour Protection & Radiance</span><span class="col-price">₹3,500</span><span class="col-price">₹4,500</span></div>
          <div class="table-item-row"><span class="col-name">Intensive Nourishing</span><span class="col-price">₹3,500</span><span class="col-price">₹4,500</span></div>
          <div class="table-item-row"><span class="col-name">Bond & Fiber Strengthening</span><span class="col-price">₹3,500</span><span class="col-price">₹4,500</span></div>
          <div class="table-item-row"><span class="col-name">Densifying</span><span class="col-price">₹3,500</span><span class="col-price">₹4,500</span></div>
          <div class="table-item-row"><span class="col-name">Anti Hair Loss</span><span class="col-price">₹3,500</span><span class="col-price">₹4,500</span></div>
          <div class="table-item-row"><span class="col-name">Anti Dandruff</span><span class="col-price">₹3,500</span><span class="col-price">₹4,500</span></div>
          <div class="table-item-row"><span class="col-name">Soothing Scalp</span><span class="col-price">₹3,500</span><span class="col-price">₹4,500</span></div>
          <div class="table-item-row"><span class="col-name">Anti Oiliness</span><span class="col-price">₹3,500</span><span class="col-price">₹4,500</span></div>
        </div>

        <div class="section-label">Signature VIP Ritual — 90 Mins</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Chronologist Youth Revitalizing</span><span class="service-dots"></span><span class="service-price">₹6,000</span></div>
          <div class="service-item"><span class="service-name">Ultimate Bespoke Hair & Scalp</span><span class="service-dots"></span><span class="service-price">₹6,000</span></div>
          <div class="service-item"><span class="service-name">Genesis Dual Action Hair Fall</span><span class="service-dots"></span><span class="service-price">₹6,000</span></div>
        </div>
      </div>
    </div>
  </div>

  <footer class="page-footer">
    <span>LOOKS SALON &nbsp;&bull;&nbsp; COMPLETE SERVICE MENU</span>
    <span class="footer-center">L O O K S &nbsp;&bull;&nbsp; S A L O N</span>
    <span>PAGE 03</span>
  </footer>
</section>

<!-- ========================================== -->
<!-- PAGE 4: SKINCARE & CLINICAL AESTHETICS     -->
<!-- ========================================== -->
<section class="page" id="page-4">
  <div class="page-border"></div>

  <header class="page-header">
    <div class="header-left">
      <span class="header-badge">03</span>
      <div class="header-title-group">
        <h2>Skincare & Facials</h2>
        <p>NATURALIV, LAAMIS ORGANICS & DERMALOGICA</p>
      </div>
    </div>
    <div class="header-right">
      <div class="header-logo-container">
        {svg_clean}
      </div>
      <span class="header-tag">KANKARBAGH, PATNA</span>
    </div>
  </header>

  <div class="content-body">
    <div class="grid-2col">
      <!-- COLUMN 1: NATURALIV & LAAMIS FACIALS + BLEACH -->
      <div class="menu-card">
        <div class="card-header">
          <span class="card-title">Facials & Clean-Ups</span>
          <span class="card-subtitle-badge">Naturaliv & Laamis</span>
        </div>

        <div class="section-label">Naturaliv Clean Ups — 30 Mins</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Detox Clean Up</span><span class="service-dots"></span><span class="service-price">₹1,500</span></div>
          <div class="service-item"><span class="service-name">De-Tan Clean Up</span><span class="service-dots"></span><span class="service-price">₹1,500</span></div>
        </div>

        <div class="section-label">Naturaliv Facial (w/o Sea Algae) — 45 Mins</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Aquaderm</span><span class="service-dots"></span><span class="service-price">₹2,500</span></div>
          <div class="service-item"><span class="service-name">Vitaderm</span><span class="service-dots"></span><span class="service-price">₹2,500</span></div>
          <div class="service-item"><span class="service-name">Sensitive</span><span class="service-dots"></span><span class="service-price">₹2,500</span></div>
        </div>

        <div class="section-label">Naturaliv Facial (w/ Sea Algae Mask) — 60 Mins</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Aquaderm</span><span class="service-dots"></span><span class="service-price">₹3,500</span></div>
          <div class="service-item"><span class="service-name">Vitaderm</span><span class="service-dots"></span><span class="service-price">₹3,500</span></div>
          <div class="service-item"><span class="service-name">Sensitive</span><span class="service-dots"></span><span class="service-price">₹3,500</span></div>
        </div>

        <div class="section-label">Laamis Organic Facial — 60 Mins</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Pure White Facial w/ Sea Algae Mask</span><span class="service-dots"></span><span class="service-price">₹4,500</span></div>
          <div class="service-item"><span class="service-name">Pure Youth Facial w/ Sea Algae Mask</span><span class="service-dots"></span><span class="service-price">₹4,500</span></div>
        </div>

        <div class="section-label">Laamis Clean Ups — 30 Mins</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Pure White Clean Up</span><span class="service-dots"></span><span class="service-price">₹2,200</span></div>
          <div class="service-item"><span class="service-name">Pure Youth Clean Up</span><span class="service-dots"></span><span class="service-price">₹2,200</span></div>
        </div>

        <div class="section-label">Bleach & De-Tan Rituals</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Face Bleach</span><span class="service-dots"></span><span class="service-price">₹600</span></div>
          <div class="service-item"><span class="service-name">D-Tan</span><span class="service-dots"></span><span class="service-price">₹700</span></div>
          <div class="service-item"><span class="service-name">Face & Neck</span><span class="service-dots"></span><span class="service-price">₹700</span></div>
          <div class="service-item"><span class="service-name">Full Arms</span><span class="service-dots"></span><span class="service-price">₹750</span></div>
          <div class="service-item"><span class="service-name">Full Legs</span><span class="service-dots"></span><span class="service-price">₹850</span></div>
          <div class="service-item"><span class="service-name">Full Body</span><span class="service-dots"></span><span class="service-price">₹3,000</span></div>
        </div>
      </div>

      <!-- COLUMN 2: DERMALOGICA & TARGETED MASKS -->
      <div class="menu-card">
        <div class="card-header">
          <span class="card-title">Dermalogica</span>
          <span class="card-subtitle-badge">Clinical Care</span>
        </div>

        <div class="section-label">Clinical Treatments — 60 Mins</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Power Brightening Treatment</span><span class="service-dots"></span><span class="service-price">₹5,000</span></div>
          <div class="service-item"><span class="service-name">Age Smart Treatment</span><span class="service-dots"></span><span class="service-price">₹5,000</span></div>
          <div class="service-item"><span class="service-name">Mrdibac Clearing Treatment</span><span class="service-dots"></span><span class="service-price">₹5,000</span></div>
          <div class="service-item"><span class="service-name">Ultracalming Treatment</span><span class="service-dots"></span><span class="service-price">₹5,000</span></div>
          <div class="service-item"><span class="service-name">Treatment w/ Cooling Contour Mask</span><span class="service-dots"></span><span class="service-price">₹5,500</span></div>
          <div class="service-item"><span class="service-name">Contour Mask</span><span class="service-dots"></span><span class="service-price">₹1,500</span></div>
          <div class="service-item"><span class="service-name">Dermalogica Clean Up (30 mins)</span><span class="service-dots"></span><span class="service-price">₹2,500</span></div>
        </div>

        <div class="section-label">Laamis Specialized Masks</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Achi Tan Out Mask</span><span class="service-dots"></span><span class="service-price">₹1,000</span></div>
          <div class="service-item"><span class="service-name">Peel Off Skin Acai Mask</span><span class="service-dots"></span><span class="service-price">₹1,000</span></div>
        </div>

        <div class="section-label">Mintree Targeted Masks</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Lip Mask</span><span class="service-dots"></span><span class="service-price">₹200</span></div>
          <div class="service-item"><span class="service-name">Eye Mask</span><span class="service-dots"></span><span class="service-price">₹250</span></div>
          <div class="service-item"><span class="service-name">Bikini Mask</span><span class="service-dots"></span><span class="service-price">₹500</span></div>
        </div>

        <div style="margin-top: 5mm; padding: 3.5mm; background: rgba(212, 175, 55, 0.05); border: 1px solid rgba(212, 175, 55, 0.22); border-radius: 4px; text-align: center;">
          <div style="font-family: 'Bodoni Moda', serif; font-size: 0.8rem; color: #f1dfa8; letter-spacing: 1.5px; margin-bottom: 1mm;">SKIN EXPERT CONSULTATION</div>
          <div style="font-size: 0.62rem; color: #a8a49d; line-height: 1.4;">Our certified Dermalogica skin therapists evaluate your face mapping zones before every ritual for tailored radiance.</div>
        </div>
      </div>
    </div>
  </div>

  <footer class="page-footer">
    <span>LOOKS SALON &nbsp;&bull;&nbsp; COMPLETE SERVICE MENU</span>
    <span class="footer-center">L O O K S &nbsp;&bull;&nbsp; S A L O N</span>
    <span>PAGE 04</span>
  </footer>
</section>

<!-- ========================================== -->
<!-- PAGE 5: BODY, HANDS & PATNA LOCATION FOOTER-->
<!-- ========================================== -->
<section class="page" id="page-5">
  <div class="page-border"></div>

  <header class="page-header">
    <div class="header-left">
      <span class="header-badge">04</span>
      <div class="header-title-group">
        <h2>Body, Hands & Finishing</h2>
        <p>MANICURE, PEDICURE, WAXING & PRECISION FINISHING</p>
      </div>
    </div>
    <div class="header-right">
      <div class="header-logo-container">
        {svg_clean}
      </div>
      <span class="header-tag">KANKARBAGH, PATNA</span>
    </div>
  </header>

  <div class="content-body" style="gap: 2mm;">
    <div class="grid-2col" style="gap: 3.5mm;">
      <!-- COLUMN 1: HAND & FEET + THREADING -->
      <div class="menu-card" style="padding: 2.8mm 3.5mm;">
        <div class="card-header">
          <span class="card-title">Hand & Feet</span>
          <span class="card-subtitle-badge">Nail & Spa</span>
        </div>

        <div class="section-label">Pedicure</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Basic Pedicure</span><span class="service-dots"></span><span class="service-price">₹1,000</span></div>
          <div class="service-item"><span class="service-name">Spa Ice Cream Pedicure</span><span class="service-dots"></span><span class="service-price">₹1,500</span></div>
          <div class="service-item"><span class="service-name">Pedi Labs Plus</span><span class="service-dots"></span><span class="service-price">₹2,000</span></div>
        </div>

        <div class="section-label">Manicure</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Basic Manicure</span><span class="service-dots"></span><span class="service-price">₹1,000</span></div>
          <div class="service-item"><span class="service-name">Spa Ice Cream Manicure</span><span class="service-dots"></span><span class="service-price">₹1,500</span></div>
          <div class="service-item"><span class="service-name">Pedi Labs Plus Manicure</span><span class="service-dots"></span><span class="service-price">₹2,000</span></div>
        </div>

        <div class="section-label">Nail</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Nail Paint</span><span class="service-dots"></span><span class="service-price">₹200</span></div>
          <div class="service-item"><span class="service-name">Nail Filing</span><span class="service-dots"></span><span class="service-price">₹200</span></div>
          <div class="service-item"><span class="service-name">Nail Art</span><span class="service-dots"></span><span class="service-price">₹2,000</span></div>
        </div>

        <div class="section-label" style="margin-top: 1.8mm;">Threading (Precision)</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Eyebrows</span><span class="service-dots"></span><span class="service-price">₹100</span></div>
          <div class="service-item"><span class="service-name">Upper Lip / Forehead / Chin (each)</span><span class="service-dots"></span><span class="service-price">₹70</span></div>
          <div class="service-item"><span class="service-name">Full Face</span><span class="service-dots"></span><span class="service-price">₹500</span></div>
        </div>
      </div>

      <!-- COLUMN 2: BODY WAXING, REJUVENATION & FACE WAX -->
      <div class="menu-card" style="padding: 2.8mm 3.5mm;">
        <div class="card-header">
          <span class="card-title">Waxing & Body</span>
          <span class="card-subtitle-badge">Rejuvenation</span>
        </div>

        <div class="section-label">Body Waxing</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Under Arms</span><span class="service-dots"></span><span class="service-price">₹250</span></div>
          <div class="service-item"><span class="service-name">Half Arms</span><span class="service-dots"></span><span class="service-price">₹600</span></div>
          <div class="service-item"><span class="service-name">Full Arms & Underarms</span><span class="service-dots"></span><span class="service-price">₹850</span></div>
          <div class="service-item"><span class="service-name">Half Legs</span><span class="service-dots"></span><span class="service-price">₹600</span></div>
          <div class="service-item"><span class="service-name">Full Legs</span><span class="service-dots"></span><span class="service-price">₹950</span></div>
          <div class="service-item"><span class="service-name">Full Wax</span><span class="service-dots"></span><span class="service-price">₹1,500</span></div>
          <div class="service-item"><span class="service-name">Full Body</span><span class="service-dots"></span><span class="service-price">₹3,500</span></div>
          <div class="service-item"><span class="service-name">Midriff / Full Front / Back (each)</span><span class="service-dots"></span><span class="service-price">₹1,000</span></div>
          <div class="service-item"><span class="service-name">B-Line</span><span class="service-dots"></span><span class="service-price">₹1,200</span></div>
          <div class="service-item"><span class="service-name">Pinkini Brazilian Wax</span><span class="service-dots"></span><span class="service-price">₹2,000</span></div>
          <div class="service-item"><span class="service-name">Eyebrows Wax (peel off)</span><span class="service-dots"></span><span class="service-price">₹200</span></div>
          <div class="service-item"><span class="service-name">Under Arms (peel off)</span><span class="service-dots"></span><span class="service-price">₹350</span></div>
        </div>

        <div class="section-label">Face Wax</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Nose Wax</span><span class="service-dots"></span><span class="service-price">₹100</span></div>
          <div class="service-item"><span class="service-name">Upperlip / Lower Lip (each)</span><span class="service-dots"></span><span class="service-price">₹120</span></div>
          <div class="service-item"><span class="service-name">Eyebrow / Forehead / Chin (each)</span><span class="service-dots"></span><span class="service-price">₹200</span></div>
          <div class="service-item"><span class="service-name">Side Lock</span><span class="service-dots"></span><span class="service-price">₹300</span></div>
          <div class="service-item"><span class="service-name">Neck Wax</span><span class="service-dots"></span><span class="service-price">₹500</span></div>
        </div>

        <div class="section-label">Body Rejuvenation</div>
        <div class="service-list">
          <div class="service-item"><span class="service-name">Arms Polishing</span><span class="service-dots"></span><span class="service-price">₹1,000</span></div>
          <div class="service-item"><span class="service-name">Full Back Polishing</span><span class="service-dots"></span><span class="service-price">₹1,000</span></div>
          <div class="service-item"><span class="service-name">Full Body Polishing</span><span class="service-dots"></span><span class="service-price">₹3,500</span></div>
        </div>
      </div>
    </div>

    <!-- GRAND CUSTOM PATNA FOOTER CARD WITH 2 QR CODES -->
    <div class="patna-footer-card">
      <div class="pfc-left">
        <div class="pfc-brand">
          <span class="pfc-brand-title">LOOKS SALON</span>
          <span class="pfc-branch-pill">PATNA EXCLUSIVE</span>
        </div>
        <div class="pfc-address">
          {ICON_PIN}
          <div class="pfc-address-text">
            <strong>B-184, Vidya Enclave, P.C. Colony</strong><br>
            Next to Lohiya Park, Kankarbagh, Patna, Bihar – 800020
          </div>
        </div>
      </div>

      <div class="pfc-middle">
        <div class="pfc-contact-line">
          {ICON_PHONE}
          <span><strong>+91 77838 65018</strong> &nbsp;|&nbsp; <strong>+91 62877 61333</strong></span>
        </div>
        <div class="pfc-contact-line" style="margin-top: 1.2mm;">
          {ICON_MAIL}
          <span>info@lookssalon.in &nbsp;·&nbsp; customercare@lookssalon.in</span>
        </div>
        <div class="pfc-hours">
          {ICON_CLOCK}
          <span>Timings: <strong>9:00 AM – 9:00 PM</strong> (Open 7 Days a Week)</span>
        </div>
      </div>

    </div>
  </div>

  <footer class="page-footer">
    <span>LOOKS SALON &nbsp;&bull;&nbsp; COMPLETE SERVICE MENU</span>
    <span class="footer-center">L O O K S &nbsp;&bull;&nbsp; S A L O N</span>
    <span>PAGE 05</span>
  </footer>
</section>

</body>
</html>
'''

with open('service_menu.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated service_menu.html with QR codes for PDF and HTML!")
