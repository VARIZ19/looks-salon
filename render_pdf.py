import os
import subprocess
import tempfile
import fitz

html_path = os.path.abspath('service_menu.html')
pdf_path = os.path.abspath('Looks Salon - Complete Service Menu - Redesigned.pdf')
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
    f'--print-to-pdf={pdf_path}',
    '--no-pdf-header-footer',
    f'file:///{html_path.replace(chr(92), "/")}'
]

print("Running Edge command...")
res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
print("Return code:", res.returncode)

if os.path.exists(pdf_path):
    print(f"Generated PDF: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
    doc = fitz.open(pdf_path)
    print(f"Page count: {len(doc)}")
    
    out_dir = os.path.abspath('new_pdf_preview')
    os.makedirs(out_dir, exist_ok=True)
    
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        img_path = os.path.join(out_dir, f'new_page_{i+1}.png')
        pix.save(img_path)
        print(f"Rendered page {i+1} to {img_path}")
else:
    print("PDF was not created!")
    print("Stdout:", res.stdout)
    print("Stderr:", res.stderr)
