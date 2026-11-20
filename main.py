#!/usr/bin/env python3
""":synopsis: news-image-20261119-v2: The World in One Day — Thursday 19 November 2026 (visual edition).
Deterministic PIL-rendered newspaper front page summarizing all 35 verified stories,
featuring an illustrated Shenzhen summit banner, icon accents, coloured map, and stat bar chart.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

def get_font(name, size):
    paths = [
        f"/usr/share/fonts/truetype/dejavu/{name}",
        f"/usr/share/fonts/truetype/deja-vu/{name}"
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def wrap_text(text, font, max_width, draw):
    words = text.split()
    if not words:
        return [""]
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
                current_line = [word]
            else:
                lines.append(word)
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")

    img = Image.new("RGB", (1024, 1024), color="#F7F2E8")
    draw = ImageDraw.Draw(img)

    serif_bold = get_font("DejaVuSerif-Bold.ttf", 14)
    serif_reg = get_font("DejaVuSerif.ttf", 12)
    sans_bold = get_font("DejaVuSans-Bold.ttf", 12)
    sans_reg = get_font("DejaVuSans.ttf", 10)

    # Masthead
    draw.rectangle([20, 15, 1004, 85], fill="#1A1A1A")
    title_font = get_font("DejaVuSerif-Bold.ttf", 32)
    draw.text((35, 22), "THE WORLD IN ONE DAY", fill="#F7F2E8", font=title_font)
    sub_font = get_font("DejaVuSans-Bold.ttf", 12)
    draw.text((35, 60), "THURSDAY, 19 NOVEMBER 2026  ·  GLOBAL EDITION", fill="#D4AF37", font=sub_font)

    # Illustrated Lead Banner (Shenzhen Summit scene)
    banner_box = [20, 90, 1004, 210]
    draw.rectangle(banner_box, fill="#121824")
    # Skyline silhouettes
    draw.rectangle([50, 130, 90, 210], fill="#1E293B")
    draw.rectangle([100, 110, 160, 210], fill="#0F172A")
    draw.rectangle([170, 140, 230, 210], fill="#1E293B")
    draw.rectangle([780, 120, 840, 210], fill="#1E293B")
    draw.rectangle([850, 100, 930, 210], fill="#0F172A")
    draw.rectangle([940, 135, 980, 210], fill="#1E293B")
    # Red sun disc
    draw.ellipse([460, 105, 540, 185], fill="#E11D48")
    # Three flags in center
    draw.rectangle([485, 120, 488, 190], fill="#94A3B8") # US flagpole
    draw.rectangle([490, 120, 510, 135], fill="#3B82F6") # US flag
    draw.rectangle([514, 120, 517, 190], fill="#94A3B8") # China flagpole
    draw.rectangle([519, 120, 539, 135], fill="#EF4444") # China flag
    draw.rectangle([543, 120, 546, 190], fill="#94A3B8") # Russia flagpole
    draw.rectangle([548, 120, 568, 135], fill="#FFFFFF") # Russia flag
    # Leaders podium / table
    draw.rectangle([440, 190, 584, 205], fill="#334155")
    banner_text = get_font("DejaVuSans-Bold.ttf", 14)
    draw.text((35, 98), "HISTORIC SHENZHEN SUMMIT: US, CHINA & RUSSIA", fill="#38BDF8", font=banner_text)

    # Lead Section
    lead_y = 220
    draw.rectangle([20, lead_y, 1004, lead_y + 115], fill="#FFFFFF", outline="#D1D5DB")
    lead_h_font = get_font("DejaVuSerif-Bold.ttf", 20)
    draw.text((35, lead_y + 10), "TRUMP, XI AND PUTIN MEET IN SHENZHEN", fill="#111827", font=lead_h_font)
    deck_font = get_font("DejaVuSerif.ttf", 13)
    deck_text = "The leaders of the United States, China and Russia hold their first three-way summit in Shenzhen — a 90-minute meeting ending in a joint peace declaration on nuclear risks and stable energy flows through the Strait of Hormuz."
    lines = wrap_text(deck_text, deck_font, 950, draw)
    cy = lead_y + 42
    for l in lines[:3]:
        draw.text((35, cy), l, fill="#374151", font=deck_font)
        cy += 18

    # Second Lead & Also Today
    sec_y = 345
    draw.rectangle([20, sec_y, 500, sec_y + 110], fill="#FFFFFF", outline="#D1D5DB")
    draw.text((32, sec_y + 8), "WORLD COURT: MYANMAR GUILTY OF GENOCIDE", fill="#991B1B", font=get_font("DejaVuSerif-Bold.ttf", 14))
    s_deck = "The ICJ rules Myanmar committed state-sponsored genocide against the Rohingya — the first ruling of its kind — in the case brought by The Gambia."
    slines = wrap_text(s_deck, sans_reg, 450, draw)
    sy = sec_y + 30
    for sl in slines[:3]:
        draw.text((32, sy), sl, fill="#374151", font=sans_reg)
        sy += 15

    draw.rectangle([520, sec_y, 1004, sec_y + 110], fill="#FEF2F2", outline="#EF4444")
    draw.text((532, sec_y + 8), "ALSO TODAY", fill="#991B1B", font=get_font("DejaVuSans-Bold.ttf", 13))
    at_items = [
        "· Kerch Bridge hit for a third time this week.",
        "· Houthi missile damages a Riyadh tower.",
        "· Cyclone Akvan nears India; 72,000 evacuated."
    ]
    aty = sec_y + 28
    for item in at_items:
        draw.text((532, aty), item, fill="#1F2937", font=sans_reg)
        aty += 18

    # Map & Stat Bars layout (y: 465 to 660)
    map_y = 465
    draw.rectangle([20, map_y, 600, map_y + 180], fill="#E0F2FE", outline="#0284C7")
    draw.text((35, map_y + 6), "GLOBAL HOTSPOTS MAP", fill="#0369A1", font=get_font("DejaVuSans-Bold.ttf", 10))
    draw.text((35, map_y + 18), "1:Hormuz 2:Kuwait 3:Bahrain 4:Kerch 5:Kyiv 6:Shenzhen 7:Beni 8:Gaza 9:Alaska", fill="#0369A1", font=get_font("DejaVuSans.ttf", 9))
    
    # Subtle latitude/longitude grid lines on map
    for gx in range(50, 580, 50):
        draw.line([(gx, map_y + 30), (gx, map_y + 175)], fill="#BAE6FD", width=1)
    for gy in range(map_y + 35, map_y + 180, 30):
        draw.line([(30, gy), (590, gy)], fill="#BAE6FD", width=1)

    # Simple abstract continent polygons/shapes on map
    draw.polygon([(80, map_y+40), (180, map_y+35), (220, map_y+90), (100, map_y+120)], fill="#FEF3C7") # N/S America
    draw.polygon([(300, map_y+35), (420, map_y+40), (400, map_y+130), (280, map_y+110)], fill="#E2E8F0") # Europe/Africa
    draw.polygon([(450, map_y+30), (570, map_y+40), (580, map_y+140), (430, map_y+120)], fill="#DCFCE7") # Asia/Australia
    # 9 Pins with clear spacing
    pins = [
        (370, map_y+95, "1"), (388, map_y+92, "2"), (404, map_y+90, "3"),
        (355, map_y+55, "4"), (330, map_y+52, "5"), (490, map_y+75, "6"),
        (360, map_y+135, "7"), (345, map_y+92, "8"), (80, map_y+45, "9")
    ]
    for px, py, pnum in pins:
        draw.ellipse([px-7, py-7, px+7, py+7], fill="#EF4444", outline="#FFFFFF")
        draw.text((px-3, py-6), pnum, fill="#FFFFFF", font=get_font("DejaVuSans-Bold.ttf", 9))

    # Stat Bar Chart Strip (Right of map)
    stat_x = 615
    draw.rectangle([stat_x, map_y, 1004, map_y + 180], fill="#FFFFFF", outline="#D1D5DB")
    draw.text((stat_x + 15, map_y + 8), "BY THE NUMBERS (VERIFIED KEY METRICS)", fill="#111827", font=get_font("DejaVuSans-Bold.ttf", 11))
    stats = [
        ("Ebola Cases (DRC)", "11,300+", 220),
        ("Ebola Deaths", "5,500", 140),
        ("Evacuated (Akvan)", "72,000", 320),
        ("Summit Duration", "90 min", 180)
    ]
    sy_bar = map_y + 32
    for label, val, bar_w in stats:
        draw.text((stat_x + 15, sy_bar), f"{label}: {val}", fill="#374151", font=sans_reg)
        draw.rectangle([stat_x + 15, sy_bar + 14, stat_x + 15 + int(bar_w * 0.8), sy_bar + 24], fill="#E11D48")
        sy_bar += 35

    # 6 Sections (3 columns x 2 rows)
    sec_data = [
        ("EUROPE", [("Russian strikes kill 4 in Odesa", "At least 4 dead and 13 hurt."), ("Kyiv: no peace without Ukraine", "Zelenskyy insists on terms."), ("Europe shut out of Shenzhen", "Leaders debate influence."), ("COP31 talks turn tense", "Draft deal splits nations."), ("Van Gogh sells for $190.4m", "Record price amid row.")]),
        ("MIDDLE EAST", [("Iran defends Gulf strikes", "Tehran calls attacks defence."), ("Three tankers burn in Hormuz", "Fires reported in strait."), ("Israel pushes into central Gaza", "Rare incursion near Nuseirat."), ("Arab League condemns raids", "Bloc denounces hospital threats."), ("Lebanon charges Hezbollah men", "Recruitment and weapons case.")]),
        ("AFRICA", [("Ebola global emergency", "11,300+ cases in DRC."), ("Ebola vaccines head to trials", "Phase two next week."), ("Ethiopia, Eritrea mass troops", "Forces build along border."), ("Sudan commander defects", "RSF officer joins army."), ("Migrant boat sinks off Senegal", "Dozens missing from vessel.")]),
        ("ASIA-PACIFIC", [("North Korea expands enrichment", "Yongbyon facility extended."), ("Lee seeks talks with Pyongyang", "South Korean president appeals."), ("Yunus home set ablaze", "Bangladesh tensions flare."), ("Indonesia passes asset law", "Parliament approves forfeiture."), ("Fiji declares disaster", "El Nino drought threat.")]),
        ("AMERICAS", [("Trump asks court to block TPS", "Admin seeks to end protections."), ("Russian charged in Palantir plot", "Targeting tech workers."), ("US, Venezuela restore ties", "Hegseth Caracas visit."), ("Pastor convicted over Haiti", "Miami court finds role."), ("Musk regrets midterm spending", "Billionaire rues outlay.")]),
        ("SCIENCE, CULTURE & SPORT", [("Anthropic record market debut", "AI firm raises record sum."), ("GTA VI arrives after 13 years", "Fans fly to NZ early."), ("NASA cargo launch cover", "Northrop Grumman CRS-25."), ("Red crabs march Christmas Island", "Millions begin migration."), ("NZ court backs pay equity", "Ruling on women's rights.")])
    ]

    col_w = 318
    col_xs = [20, 353, 686]
    row_ys = [645, 810]

    for idx, (sec_title, items) in enumerate(sec_data):
        c_idx = idx % 3
        r_idx = idx // 3
        cx = col_xs[c_idx]
        cy = row_ys[r_idx]
        
        # Section background box
        draw.rectangle([cx, cy, cx + col_w, cy + 158], fill="#FFFFFF", outline="#D1D5DB")
        # Red Header Bar
        draw.rectangle([cx, cy, cx + col_w, cy + 16], fill="#991B1B")
        draw.text((cx + 8, cy + 2), sec_title, fill="#FFFFFF", font=get_font("DejaVuSans-Bold.ttf", 9))
        
        iy = cy + 19
        for headline, deck in items: # All 5 stories per section
            draw.text((cx + 6, iy), f"• {headline}", fill="#111827", font=get_font("DejaVuSans-Bold.ttf", 9))
            iy += 12
            draw.text((cx + 14, iy), deck, fill="#4B5563", font=get_font("DejaVuSans.ttf", 9))
            iy += 14

    # Date Check & Footer
    footer_y = 975
    draw.rectangle([20, footer_y, 1004, footer_y + 42], fill="#FEF2F2", outline="#EF4444")
    draw.text((35, footer_y + 4), "DATE CHECK — Every story on this page is verified for Thursday, 19 November 2026.", fill="#991B1B", font=get_font("DejaVuSans-Bold.ttf", 10))
    draw.text((35, footer_y + 24), "THE WORLD IN ONE DAY  ·  PRODUCED DETERMINISTICALLY VIA PIL  ·  MAKE.FUN NEWS-IMAGE-20261119 V2", fill="#6B7280", font=sans_reg)

    img.save(out_path, "PNG")
    print(f"Successfully generated {out_path}")

if __name__ == "__main__":
    main()
