import os
import math
from PIL import Image, ImageDraw, ImageFilter

OUTPUT_DIR = "LiquidGlass_Windows_ICO"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_liquid_glass_base(size=256):
    base = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(base)
    margin = int(size * 0.05)
    radius = int(size * 0.24)
    rect = [margin, margin, size - margin, size - margin]
    draw.rounded_rectangle(rect, radius=radius, fill=(36, 39, 46, 225), outline=(255, 255, 255, 70), width=3)
    highlight = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    h_draw = ImageDraw.Draw(highlight)
    h_draw.rounded_rectangle([margin+3, margin+3, size-margin-3, size-margin-3], radius=radius-3, outline=(255, 255, 255, 35), width=2)
    return Image.alpha_composite(base, highlight)

def draw_letter_badge(draw, text, cx=128, cy=128):
    w = (255, 255, 255, 255)
    bg = (36, 39, 46, 255)
    draw.rounded_rectangle([cx-48, cy-48, cx+48, cy+48], radius=16, outline=w, width=9)
    # Vẽ ký tự hình học sắc nét cho từng app
    if text == "W": # Word
        draw.line([(cx-26, cy-22), (cx-14, cy+22), (cx, cy-6), (cx+14, cy+22), (cx+26, cy-22)], fill=w, width=8)
    elif text == "X": # Excel
        draw.line([(cx-20, cy-22), (cx+20, cy+22)], fill=w, width=9)
        draw.line([(cx+20, cy-22), (cx-20, cy+22)], fill=w, width=9)
    elif text == "P": # PowerPoint
        draw.line([(cx-16, cy-22), (cx-16, cy+24)], fill=w, width=9)
        draw.arc([cx-16, cy-22, cx+22, cy+4], start=270, end=90, fill=w, width=9)
    elif text == "A": # Access
        draw.line([(cx-22, cy+22), (cx, cy-22), (cx+22, cy+22)], fill=w, width=9)
        draw.line([(cx-12, cy+6), (cx+12, cy+6)], fill=w, width=8)
    elif text == "Pub": # Publisher
        draw.rounded_rectangle([cx-22, cy-22, cx+22, cy+22], radius=6, outline=w, width=8)
    elif text == "O": # Outlook
        draw.ellipse([cx-22, cy-22, cx+22, cy+22], outline=w, width=9)
    elif text == "PDF": # Foxit PDF
        draw.polygon([(cx-18, cy+20), (cx, cy-24), (cx+18, cy+20)], outline=w, width=8)
    elif text == "U": # UniKey / UltraViewer
        draw.arc([cx-20, cy-22, cx+20, cy+22], start=0, end=180, fill=w, width=9)
        draw.line([(cx-20, cy-22), (cx-20, cy)], fill=w, width=9)
        draw.line([(cx+20, cy-22), (cx+20, cy)], fill=w, width=9)
    elif text == "C": # Canva / CocCoc
        draw.arc([cx-22, cy-22, cx+22, cy+22], start=45, end=315, fill=w, width=9)

def draw_symbol(draw, app_type, cx=128, cy=128):
    w = (255, 255, 255, 255)
    bg = (36, 39, 46, 255)
    if app_type == "Chrome":
        draw.ellipse([cx-52, cy-52, cx+52, cy+52], outline=w, width=10)
        draw.ellipse([cx-20, cy-20, cx+20, cy+20], fill=w)
        draw.line([cx, cy-20, cx+46, cy-20], fill=w, width=8)
        draw.line([cx-17, cy+10, cx-40, cy+46], fill=w, width=8)
        draw.line([cx+17, cy+10, cx+40, cy+46], fill=w, width=8)
    elif app_type == "Edge":
        draw.ellipse([cx-50, cy-50, cx+50, cy+50], outline=w, width=10)
        draw.arc([cx-30, cy-30, cx+30, cy+30], start=30, end=260, fill=w, width=9)
    elif app_type == "CocCoc":
        draw.ellipse([cx-50, cy-50, cx+50, cy+50], outline=w, width=10)
        draw.arc([cx-28, cy-28, cx+28, cy+28], start=50, end=310, fill=w, width=10)
    elif app_type == "Zalo":
        draw.rounded_rectangle([cx-52, cy-46, cx+52, cy+42], radius=22, fill=w)
        draw.polygon([(cx-28, cy+38), (cx-42, cy+54), (cx-10, cy+42)], fill=w)
        draw.line([(cx-22, cy-18), (cx+22, cy-18), (cx-22, cy+16), (cx+22, cy+16)], fill=bg, width=8)
    elif app_type == "Facebook":
        draw.rounded_rectangle([cx-48, cy-48, cx+48, cy+48], radius=18, outline=w, width=9)
        draw.line([(cx+6, cy+44), (cx+6, cy-12)], fill=w, width=10)
        draw.arc([cx+6, cy-24, cx+32, cy], start=180, end=270, fill=w, width=10)
        draw.line([(cx-10, cy+6), (cx+24, cy+6)], fill=w, width=9)
    elif app_type == "Gemini":
        draw.polygon([(cx, cy-54), (cx+14, cy-14), (cx+54, cy), (cx+14, cy+14), (cx, cy+54), (cx-14, cy+14), (cx-54, cy), (cx-14, cy-14)], fill=w)
    elif app_type == "VS_Code":
        draw.line([(cx-38, cy-22), (cx+32, cy+42), (cx+32, cy-42), (cx-38, cy+22)], fill=w, width=11)
        draw.line([(cx+32, cy-42), (cx+32, cy+42)], fill=w, width=13)
    elif app_type == "Visual_Studio":
        draw.polygon([(cx-44, cy-26), (cx-44, cy+26), (cx+36, cy-44), (cx+36, cy+44)], outline=w, width=10)
    elif app_type == "SQL_Server":
        draw.ellipse([cx-44, cy-48, cx+44, cy-24], outline=w, width=8)
        draw.arc([cx-44, cy-14, cx+44, cy+12], start=0, end=180, fill=w, width=8)
        draw.arc([cx-44, cy+14, cx+44, cy+42], start=0, end=180, fill=w, width=8)
        draw.line([(cx-44, cy-36), (cx-44, cy+28)], fill=w, width=8)
        draw.line([(cx+44, cy-36), (cx+44, cy+28)], fill=w, width=8)
    elif app_type == "Power_BI":
        draw.rounded_rectangle([cx-38, cy+4, cx-18, cy+44], radius=4, fill=w)
        draw.rounded_rectangle([cx-10, cy-18, cx+10, cy+44], radius=4, fill=w)
        draw.rounded_rectangle([cx+18, cy-42, cx+38, cy+44], radius=4, fill=w)
    elif app_type == "Folder":
        draw.rounded_rectangle([cx-54, cy-34, cx+54, cy+42], radius=12, outline=w, width=9)
        draw.polygon([(cx-54, cy-26), (cx-54, cy-44), (cx-12, cy-44), (cx, cy-30)], fill=w)
    elif app_type == "This_PC":
        draw.rounded_rectangle([cx-52, cy-40, cx+52, cy+26], radius=10, outline=w, width=9)
        draw.line([(cx-24, cy+42), (cx+24, cy+42)], fill=w, width=9)
        draw.line([(cx, cy+26), (cx, cy+42)], fill=w, width=9)
    elif app_type == "Recycle_Bin":
        draw.polygon([(cx-36, cy-26), (cx+36, cy-26), (cx+26, cy+44), (cx-26, cy+44)], outline=w, width=8)
        draw.line([(cx-44, cy-36), (cx+44, cy-36)], fill=w, width=9)
    elif app_type == "Network":
        draw.ellipse([cx-48, cy-48, cx+48, cy+48], outline=w, width=8)
        draw.ellipse([cx-22, cy-48, cx+22, cy+48], outline=w, width=7)
        draw.line([(cx-48, cy), (cx+48, cy)], fill=w, width=7)
    elif app_type == "Control_Panel":
        draw.ellipse([cx-32, cy-32, cx+32, cy+32], outline=w, width=11)
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            draw.line([(cx+int(32*math.cos(rad)), cy+int(32*math.sin(rad))), (cx+int(46*math.cos(rad)), cy+int(46*math.sin(rad)))], fill=w, width=10)
    else:
        badge_map = {"Word":"W", "Excel":"X", "PowerPoint":"P", "Access":"A", "Publisher":"Pub", "Outlook":"O", "Foxit":"PDF", "UniKey":"U", "UltraViewer":"U", "Canva":"C"}
        draw_letter_badge(draw, badge_map.get(app_type, "C"), cx, cy)

ALL_APPS = [
    "Chrome", "Edge", "CocCoc", "Zalo", "Facebook", "Gemini", "Canva",
    "VS_Code", "Visual_Studio", "SQL_Server", "Power_BI",
    "Word", "Excel", "PowerPoint", "Access", "Publisher", "Outlook",
    "Foxit", "UniKey", "UltraViewer",
    "Folder", "This_PC", "Recycle_Bin", "Network", "Control_Panel"
]

if __name__ == "__main__":
    for app in ALL_APPS:
        fg = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
        draw = ImageDraw.Draw(fg)
        draw_symbol(draw, app)
        glow = fg.filter(ImageFilter.GaussianBlur(radius=7))
        canvas = create_liquid_glass_base(256)
        canvas = Image.alpha_composite(canvas, glow)
        canvas = Image.alpha_composite(canvas, fg)
        canvas.save(os.path.join(OUTPUT_DIR, f"{app}.ico"), format="ICO", sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])
