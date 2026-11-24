import os
import math
from PIL import Image, ImageDraw, ImageFilter

OUTPUT_DIR = "LiquidGlass_Windows_ICO"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_liquid_glass_base(size=256):
    """Tạo nền kính mờ bo góc (Squircle) + viền sáng mỏng kiểu Ultra Liquid Glass PRO"""
    base = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(base)
    
    margin = int(size * 0.05)
    radius = int(size * 0.24)
    rect = [margin, margin, size - margin, size - margin]
    
    # Nền kính tối bán trong suốt + viền mảnh phản quang
    draw.rounded_rectangle(
        rect,
        radius=radius,
        fill=(36, 39, 46, 225),
        outline=(255, 255, 255, 70),
        width=3
    )
    
    # Lớp highlight ánh sáng viền trong
    highlight = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    h_draw = ImageDraw.Draw(highlight)
    h_draw.rounded_rectangle(
        [margin + 3, margin + 3, size - margin - 3, size - margin - 3],
        radius=radius - 3,
        outline=(255, 255, 255, 35),
        width=2
    )
    return Image.alpha_composite(base, highlight)

def draw_symbol(draw, app_type, cx=128, cy=128):
    """Tự vẽ biểu tượng trắng tối giản chuẩn vector sắc nét không cần tải mạng"""
    w = (255, 255, 255, 255)
    
    if app_type == "Chrome":
        draw.ellipse([cx-54, cy-54, cx+54, cy+54], outline=w, width=10)
        draw.ellipse([cx-22, cy-22, cx+22, cy+22], fill=w)
        draw.line([cx, cy-22, cx+48, cy-22], fill=w, width=9)
        draw.line([cx-19, cy+11, cx-43, cy+50], fill=w, width=9)
        draw.line([cx+19, cy+11, cx+43, cy+50], fill=w, width=9)
        
    elif app_type == "YouTube":
        draw.rounded_rectangle([cx-58, cy-40, cx+58, cy+40], radius=18, fill=w)
        draw.polygon([(cx-14, cy-18), (cx-14, cy+18), (cx+22, cy)], fill=(36, 39, 46, 255))
        
    elif app_type == "Spotify":
        draw.ellipse([cx-54, cy-54, cx+54, cy+54], fill=w)
        bg = (36, 39, 46, 255)
        draw.arc([cx-36, cy-24, cx+36, cy+16], start=200, end=340, fill=bg, width=8)
        draw.arc([cx-28, cy-6, cx+28, cy+28], start=200, end=340, fill=bg, width=7)
        draw.arc([cx-20, cy+10, cx+20, cy+38], start=200, end=340, fill=bg, width=6)
        
    elif app_type == "Messenger":
        draw.ellipse([cx-52, cy-52, cx+52, cy+46], fill=w)
        draw.polygon([(cx-32, cy+36), (cx-42, cy+56), (cx-14, cy+44)], fill=w)
        draw.line([(cx-28, cy+6), (cx-6, cy-14), (cx+8, cy+2), (cx+28, cy-16)], fill=(36, 39, 46, 255), width=8)
        
    elif app_type == "Telegram":
        draw.polygon([(cx-52, cy), (cx+48, cy-42), (cx+28, cy+46), (cx-4, cy+18), (cx-18, cy+36), (cx-18, cy+12)], fill=w)
        
    elif app_type == "Zalo":
        draw.rounded_rectangle([cx-52, cy-48, cx+52, cy+44], radius=24, fill=w)
        draw.polygon([(cx-30, cy+40), (cx-44, cy+56), (cx-12, cy+44)], fill=w)
        # Chữ Z cách điệu
        draw.line([(cx-24, cy-20), (cx+24, cy-20), (cx-24, cy+18), (cx+24, cy+18)], fill=(36, 39, 46, 255), width=9)
        
    elif app_type == "VS_Code":
        draw.line([(cx-38, cy-22), (cx+32, cy+42), (cx+32, cy-42), (cx-38, cy+22)], fill=w, width=12)
        draw.line([(cx+32, cy-42), (cx+32, cy+42)], fill=w, width=14)
        
    elif app_type == "Terminal":
        draw.rounded_rectangle([cx-54, cy-44, cx+54, cy+44], radius=14, outline=w, width=9)
        draw.line([(cx-28, cy-14), (cx-8, cy+2), (cx-28, cy+18)], fill=w, width=8)
        draw.line([(cx+2, cy+18), (cx+28, cy+18)], fill=w, width=8)
        
    elif app_type == "Folder":
        draw.rounded_rectangle([cx-56, cy-36, cx+56, cy+44], radius=12, outline=w, width=9)
        draw.polygon([(cx-56, cy-28), (cx-56, cy-46), (cx-12, cy-46), (cx, cy-32)], fill=w)
        
    elif app_type == "Settings":
        draw.ellipse([cx-34, cy-34, cx+34, cy+34], outline=w, width=12)
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x1, y1 = cx + int(34 * math.cos(rad)), cy + int(34 * math.sin(rad))
            x2, y2 = cx + int(48 * math.cos(rad)), cy + int(48 * math.sin(rad))
            draw.line([(x1, y1), (x2, y2)], fill=w, width=11)
            
    elif app_type == "Music":
        draw.ellipse([cx-36, cy+16, cx-10, cy+40], fill=w)
        draw.ellipse([cx+12, cy+8, cx+38, cy+32], fill=w)
        draw.line([(cx-12, cy+26), (cx-12, cy-34), (cx+36, cy-44), (cx+36, cy+20)], fill=w, width=9)
        
    elif app_type == "Browser_Edge":
        draw.ellipse([cx-50, cy-50, cx+50, cy+50], outline=w, width=11)
        draw.arc([cx-32, cy-32, cx+32, cy+32], start=30, end=260, fill=w, width=10)

APPS = [
    "Chrome", "YouTube", "Spotify", "Messenger",
    "Telegram", "Zalo", "VS_Code", "Terminal",
    "Folder", "Settings", "Music", "Browser_Edge"
]

if __name__ == "__main__":
    for app in APPS:
        fg = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
        draw = ImageDraw.Draw(fg)
        draw_symbol(draw, app)
        
        # Hiệu ứng phát sáng (Glow) đặc trưng của Ultra Liquid Glass PRO
        glow = fg.filter(ImageFilter.GaussianBlur(radius=7))
        
        canvas = create_liquid_glass_base(256)
        canvas = Image.alpha_composite(canvas, glow)
        canvas = Image.alpha_composite(canvas, fg)
        
        ico_path = os.path.join(OUTPUT_DIR, f"{app}.ico")
        canvas.save(
            ico_path,
            format="ICO",
            sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
        )
        print(f"[OK] Đã xuất: {ico_path}")
