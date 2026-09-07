import os
import subprocess
import tempfile
import fitz
import qrcode

# 1. Ensure QR Code for PDF is generated with high error correction
pdf_url = "https://looks-salon-patna.vercel.app/Looks%20Salon%20-%20Complete%20Service%20Menu.pdf"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=16,
    border=2
)
qr.add_data(pdf_url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="#000000", back_color="#FFFFFF").convert('RGB')
qr_img.save("qr_pdf_poster.png")
print("Generated qr_pdf_poster.png")

# 2. Read official SVG Logo
with open("Big_Logo.svg", "r", encoding="utf-8") as f:
    logo_svg = f.read()

# Inline SVG Icons
ICON_PIN = '''<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0; margin-top:1px;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>'''
ICON_PHONE = '''<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'''
ICON_CLOCK = '''<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>'''
ICON_SCAN = '''<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7V5a2 2 0 0 1 2-2h2"></path><path d="M17 3h2a2 2 0 0 1 2 2v2"></path><path d="M21 17v2a2 2 0 0 1-2 2h-2"></path><path d="M7 21H5a2 2 0 0 1-2-2v-2"></path><rect x="7" y="7" width="10" height="10" rx="1"></rect></svg>'''
ICON_DOWNLOAD = '''<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>'''
ICON_SPARKLE = '''<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>'''

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Looks Salon - PDF Service Menu QR Poster</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,600;0,6..96,700;1,6..96,400&family=Montserrat:wght@300;400;500;600;700&display=swap');

    @page {{
      size: A4 portrait;
      margin: 0;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Montserrat', sans-serif;
      background: #0d0c0a;
      color: #eae6df;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
    }}

    .poster-page {{
      width: 210mm;
      height: 297mm;
      position: relative;
      background: radial-gradient(circle at 50% 25%, #1c1a16 0%, #0c0c0a 80%);
      padding: 12mm 14mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
    }}

    /* Luxury Outer Borders */
    .border-outer {{
      position: absolute;
      top: 5mm;
      left: 5mm;
      right: 5mm;
      bottom: 5mm;
      border: 1.5px solid rgba(212, 175, 55, 0.45);
      pointer-events: none;
    }}

    .border-inner {{
      position: absolute;
      top: 7.5mm;
      left: 7.5mm;
      right: 7.5mm;
      bottom: 7.5mm;
      border: 0.8px solid rgba(212, 175, 55, 0.2);
      pointer-events: none;
    }}

    .corner-decor {{
      position: absolute;
      width: 14mm;
      height: 14mm;
      border-color: #d4af37;
      pointer-events: none;
    }}
    .c-tl {{ top: 6mm; left: 6mm; border-top: 2.5px solid #d4af37; border-left: 2.5px solid #d4af37; }}
    .c-tr {{ top: 6mm; right: 6mm; border-top: 2.5px solid #d4af37; border-right: 2.5px solid #d4af37; }}
    .c-bl {{ bottom: 6mm; left: 6mm; border-bottom: 2.5px solid #d4af37; border-left: 2.5px solid #d4af37; }}
    .c-br {{ bottom: 6mm; right: 6mm; border-bottom: 2.5px solid #d4af37; border-right: 2.5px solid #d4af37; }}

    /* Header */
    .poster-header {{
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 3mm;
      position: relative;
      z-index: 2;
      padding-top: 4mm;
    }}

    .logo-box {{
      width: 130px;
      height: 44px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .logo-box svg {{
      width: 100%;
      height: 100%;
    }}

    .branch-badge {{
      display: inline-block;
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 3.5px;
      text-transform: uppercase;
      color: #0d0c0a;
      background: linear-gradient(135deg, #d4af37 0%, #ecd07a 50%, #b8972e 100%);
      padding: 3px 16px;
      border-radius: 2px;
      margin-top: 1mm;
    }}

    .title-group {{
      margin-top: 2mm;
    }}

    .main-title {{
      font-family: 'Bodoni Moda', serif;
      font-size: 1.85rem;
      font-weight: 700;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: #fbf9f5;
      line-height: 1.15;
    }}

    .subtitle {{
      font-size: 0.78rem;
      font-weight: 500;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      color: #c5a059;
      margin-top: 1.5mm;
    }}

    /* Main Hero QR Section */
    .hero-qr-section {{
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      z-index: 2;
      margin: 3mm 0;
    }}

    .qr-card-container {{
      background: rgba(22, 20, 17, 0.85);
      border: 1.8px solid rgba(212, 175, 55, 0.45);
      border-radius: 8px;
      padding: 7mm 9mm 6mm 9mm;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.6), 0 0 20px rgba(212, 175, 55, 0.12);
      backdrop-filter: blur(8px);
      position: relative;
    }}

    .qr-card-badge {{
      position: absolute;
      top: -3.5mm;
      background: #d4af37;
      color: #0c0c0a;
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      padding: 2px 14px;
      border-radius: 20px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    }}

    .qr-frame {{
      background: #ffffff;
      padding: 4.5mm;
      border-radius: 6px;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-top: 2mm;
    }}

    .qr-frame img {{
      width: 60mm;
      height: 60mm;
      display: block;
    }}

    .scan-cta {{
      margin-top: 4.5mm;
      text-align: center;
    }}

    .scan-cta-title {{
      font-family: 'Bodoni Moda', serif;
      font-size: 1.15rem;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #d4af37;
    }}

    .scan-cta-desc {{
      font-size: 0.72rem;
      color: #d0ccc4;
      margin-top: 1.5mm;
      letter-spacing: 1px;
    }}

    /* Value Pillars */
    .features-row {{
      display: flex;
      justify-content: center;
      gap: 7mm;
      margin-top: 5mm;
      width: 100%;
    }}

    .feature-item {{
      display: flex;
      align-items: center;
      gap: 2.5mm;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(212, 175, 55, 0.2);
      padding: 2.5mm 4.5mm;
      border-radius: 4px;
    }}

    .feature-text {{
      font-size: 0.65rem;
      font-weight: 600;
      color: #ece8e1;
      letter-spacing: 1.2px;
      text-transform: uppercase;
    }}

    /* Menu Categories Highlights */
    .categories-preview {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 3mm;
      position: relative;
      z-index: 2;
      width: 100%;
    }}

    .cat-card {{
      background: rgba(25, 23, 20, 0.7);
      border: 1px solid rgba(212, 175, 55, 0.2);
      border-radius: 4px;
      padding: 3mm 2.5mm;
      text-align: center;
    }}

    .cat-title {{
      font-family: 'Bodoni Moda', serif;
      font-size: 0.78rem;
      font-weight: 700;
      color: #d4af37;
      text-transform: uppercase;
      letter-spacing: 1px;
    }}

    .cat-sub {{
      font-size: 0.58rem;
      color: #a8a49c;
      margin-top: 1mm;
      line-height: 1.3;
    }}

    /* Patna Exclusive Footer Info Card */
    .patna-footer-card {{
      background: rgba(22, 20, 17, 0.95);
      border: 1.2px solid rgba(212, 175, 55, 0.35);
      border-radius: 6px;
      padding: 4mm 6mm;
      display: grid;
      grid-template-columns: 1.15fr 1.3fr;
      gap: 6mm;
      align-items: center;
      position: relative;
      z-index: 2;
      box-shadow: 0 6px 18px rgba(0,0,0,0.4);
    }}

    .pfc-left {{
      display: flex;
      flex-direction: column;
      gap: 1.8mm;
    }}

    .pfc-brand {{
      display: flex;
      align-items: center;
      gap: 3mm;
    }}

    .pfc-brand-title {{
      font-family: 'Bodoni Moda', serif;
      font-size: 0.95rem;
      font-weight: 700;
      color: #d4af37;
      letter-spacing: 1.5px;
    }}

    .pfc-branch-pill {{
      font-size: 0.52rem;
      font-weight: 700;
      letter-spacing: 1.8px;
      background: #d4af37;
      color: #0c0c0a;
      padding: 1.5px 6px;
      border-radius: 2px;
      text-transform: uppercase;
    }}

    .pfc-address {{
      display: flex;
      align-items: flex-start;
      gap: 2mm;
      font-size: 0.62rem;
      color: #d8d4cb;
      line-height: 1.35;
    }}

    .pfc-right {{
      display: flex;
      flex-direction: column;
      gap: 1.6mm;
      border-left: 1px solid rgba(212, 175, 55, 0.2);
      padding-left: 5mm;
      font-size: 0.62rem;
      color: #d8d4cb;
    }}

    .contact-item {{
      display: flex;
      align-items: center;
      gap: 2mm;
    }}

    .contact-item strong {{
      color: #ffffff;
    }}

    /* Bottom Brand Bar */
    .bottom-bar {{
      text-align: center;
      font-size: 0.55rem;
      letter-spacing: 3.5px;
      text-transform: uppercase;
      color: #8f8b83;
      padding-top: 1mm;
      position: relative;
      z-index: 2;
    }}
  </style>
</head>
<body>

<div class="poster-page">
  <div class="border-outer"></div>
  <div class="border-inner"></div>
  <div class="corner-decor c-tl"></div>
  <div class="corner-decor c-tr"></div>
  <div class="corner-decor c-bl"></div>
  <div class="corner-decor c-br"></div>

  <!-- Header -->
  <header class="poster-header">
    <div class="logo-box">
      {logo_svg}
    </div>
    <div class="branch-badge">Kankarbagh, Patna</div>
    <div class="title-group">
      <h1 class="main-title">Complete Service Menu</h1>
      <p class="subtitle">Experience Luxury Hair, Skin & Body Rituals</p>
    </div>
  </header>

  <!-- Hero QR Card -->
  <section class="hero-qr-section">
    <div class="qr-card-container">
      <div class="qr-card-badge">Instant PDF Menu</div>
      
      <div class="qr-frame">
        <img src="qr_pdf_poster.png" alt="Looks Salon PDF Menu QR Code">
      </div>

      <div class="scan-cta">
        <div class="scan-cta-title">Scan With Any Smartphone</div>
        <div class="scan-cta-desc">Instant access to complete price list, services & rituals</div>
      </div>
    </div>

    <!-- 3 Core Pillars -->
    <div class="features-row">
      <div class="feature-item">
        {ICON_SCAN}
        <span class="feature-text">Open Phone Camera</span>
      </div>
      <div class="feature-item">
        {ICON_DOWNLOAD}
        <span class="feature-text">Instant PDF Download</span>
      </div>
      <div class="feature-item">
        {ICON_SPARKLE}
        <span class="feature-text">100% Verified Rates</span>
      </div>
    </div>
  </section>

  <!-- Service Categories Overview -->
  <section class="categories-preview">
    <div class="cat-card">
      <div class="cat-title">Hair & Styling</div>
      <div class="cat-sub">Cut, Styling, Shave & Beard Grooming</div>
    </div>
    <div class="cat-card">
      <div class="cat-title">Color & Texture</div>
      <div class="cat-sub">Global Color, Highlights, Straightening & Keratin</div>
    </div>
    <div class="cat-card">
      <div class="cat-title">Hair Spa & Scalp</div>
      <div class="cat-sub">Kérastase, L'Oréal Rituals & Treatments</div>
    </div>
    <div class="cat-card">
      <div class="cat-title">Skin & Body Care</div>
      <div class="cat-sub">Luxury Facials, Cleanup, Mani-Pedi & Waxing</div>
    </div>
  </section>

  <!-- Patna Location Card -->
  <footer class="patna-footer-card">
    <div class="pfc-left">
      <div class="pfc-brand">
        <span class="pfc-brand-title">LOOKS SALON</span>
        <span class="pfc-branch-pill">Patna Branch</span>
      </div>
      <div class="pfc-address">
        {ICON_PIN}
        <div>
          <strong>B-184, Vidya Enclave, P.C. Colony</strong><br>
          Next to Lohiya Park, Kankarbagh, Patna &ndash; 800020
        </div>
      </div>
    </div>

    <div class="pfc-right">
      <div class="contact-item">
        {ICON_PHONE}
        <span><strong>+91 77838 65018</strong> &nbsp;|&nbsp; <strong>+91 62877 61333</strong></span>
      </div>
      <div class="contact-item">
        {ICON_CLOCK}
        <span>Timings: <strong>9:00 AM &ndash; 9:00 PM</strong> (Open 7 Days)</span>
      </div>
    </div>
  </footer>

  <div class="bottom-bar">
    LOOKS SALON &nbsp;&bull;&nbsp; KANKARBAGH PATNA &nbsp;&bull;&nbsp; WWW.LOOKSSALON.IN
  </div>
</div>

</body>
</html>
'''

with open("poster_qr_pdf.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved poster_qr_pdf.html successfully!")

# 3. Render PDF Poster and PNG using Edge Headless
html_path = os.path.abspath('poster_qr_pdf.html')
pdf_poster_path = os.path.abspath('Looks Salon - PDF Menu QR Poster.pdf')
temp_dir = tempfile.mkdtemp()
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

cmd = [
    edge_path,
    '--headless',
    '--disable-gpu',
    '--no-margins',
    '--run-all-compositor-stages-before-draw',
    '--virtual-time-budget=5000',
    f'--user-data-dir={temp_dir}',
    f'--print-to-pdf={pdf_poster_path}',
    '--no-pdf-header-footer',
    f'file:///{html_path.replace(chr(92), "/")}'
]

print("Rendering PDF poster with Edge...")
res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

if os.path.exists(pdf_poster_path):
    print(f"Generated PDF Poster: {pdf_poster_path}")
    doc = fitz.open(pdf_poster_path)
    # Render at 300 DPI for ultra sharp print quality
    page = doc[0]
    pix = page.get_pixmap(dpi=300)
    png_poster_path = os.path.abspath('LOOKS_SALON_PDF_QR_POSTER.png')
    pix.save(png_poster_path)
    print(f"Rendered High-Res PNG Poster (300 DPI): {png_poster_path}")
else:
    print("Failed to generate PDF poster:", res.stderr)
