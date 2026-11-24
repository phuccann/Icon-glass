import os
import io
import requests
from PIL import Image, ImageDraw, ImageFilter

OUTPUT_DIR = "LiquidGlass_Windows_ICO"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Danh sách phần mềm Windows & Dev phổ biến (ánh xạ sang slug chuẩn của SimpleIcons)
WINDOWS_APPS = {
    "Google_Chrome": "googlechrome",
    "Microsoft_Edge": "microsoftedge",
    "Zalo": "zalo",
    "Messenger": "messenger",
    "Spotify": "spotify",
    "YouTube": "youtube",
    "Visual_Studio_Code": "visualstudiocode",
    "Visual_Studio": "visualstudio",
    "GitHub": "github",
    "Python": "python",
    "SQL_Server": "microsoftsqlserver",
    "Discord": "discord",
    "Telegram": "telegram",
    "Canva": "canva",
    "Minecraft": "minecraft",
    "Steam": "steam",
    "Windows_Terminal": "windowsterminal",
    "Google_Drive": "googledrive",
    "Notion": "notion",
    "Garena": "garena"
}

def create_liquid_glass_base(size=256):
    """Tạo nền kính mờ bo góc (Squircle) + viền sáng mỏng kiểu Ultra Liquid Glass PRO"""
    base = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(base)
    
    margin = int(size * 0.05)
    radius = int(size * 0.24)
    rect = [margin, margin, size - margin, size - margin]
    
    # Nền kính tối bán trong suốt (#24272E) + viền mảnh phản quang
    draw.rounded_rectangle(
        rect,
        radius=radius,
        fill=(36, 39, 46, 220),
        outline=(255, 255, 255, 65),
        width=3
    )
    
    # Lớp highlight ánh sáng viền trong
    highlight = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    h_draw = ImageDraw.Draw(highlight)
    h_draw.rounded_rectangle(
        [margin + 3, margin + 3, size - margin - 3, size - margin - 3],
        radius=radius - 3,
        outline=(255, 255, 255, 30),
        width=2
    )
    return Image.alpha_composite(base, highlight)

def generate_app_icon(app_name, slug):
    png_url = f"https://api.iconify.design/simple-icons/{slug}.png?color=%23ffffff&height=124"
    try:
        resp = requests.get(png_url, timeout=15)
        if resp.status_code != 200 or len(resp.content) < 100:
            print(f"[Bỏ qua] Không tìm thấy vector cho {app_name} ({slug})")
            return
            
        fg_icon = Image.open(io.BytesIO(resp.content)).convert("RGBA")
        
        # Tạo hiệu ứng phát sáng trắng nhẹ (Glow) đặc trưng của Ultra Liquid Glass
        glow = fg_icon.filter(ImageFilter.GaussianBlur(radius=7))
        
        canvas = create_liquid_glass_base(256)
        pos_x = (256 - fg_icon.width) // 2
        pos_y = (256 - fg_icon.height) // 2
        
        canvas.paste(glow, (pos_x, pos_y), glow)
        canvas.paste(fg_icon, (pos_x, pos_y), fg_icon)
        
        ico_path = os.path.join(OUTPUT_DIR, f"{app_name}.ico")
        canvas.save(
            ico_path,
            format="ICO",
            sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
        )
        print(f"[OK] Đã tạo: {ico_path}")
        
    except Exception as e:
        print(f"[Lỗi] {app_name}: {e}")

if __name__ == "__main__":
    print("Bắt đầu khởi tạo bộ icon Ultra Liquid Glass cho Windows 11...")
    for name, slug in WINDOWS_APPS.items():
        generate_app_icon(name, slug)
    print(f"Hoàn tất! File lưu tại: {os.path.abspath(OUTPUT_DIR)}")
