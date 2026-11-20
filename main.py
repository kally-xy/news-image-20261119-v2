#!/usr/bin/env python3
""":synopsis: news-image-20261119-v2: The World in One Day — Thursday 19 November 2026 (visual edition).
Deterministic PIL-rendered newspaper front page summarizing all 35 verified stories,
featuring realistic multi-point continent coastlines, detailed section icons, high-fidelity banner flags, and stat bar chart.
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

    # Illustrated Lead Banner (Shenzhen Summit scene with detailed flags ~44x30)
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

    # Three Flagpoles & Detailed Recognisable Flags (~44x30)
    # US Flagpole & Flag at x=450
    draw.rectangle([448, 110, 451, 190], fill="#94A3B8")
    draw.rectangle([452, 115, 496, 145], fill="#B91C1C") # Red field
    # US stripes (white horizontal lines)
    for sy_line in range(119, 145, 4):
        draw.line([(452, sy_line), (496, sy_line)], fill="#FFFFFF", width=2)
    # US Canton (blue)
    draw.rectangle([452, 115, 472, 131], fill="#1E3A8A")
    # US stars (white dots)
    for sx in [456, 462, 468]:
        for sy_dot in [119, 123, 127]:
            draw.point((sx, sy_dot), fill="#FFFFFF")

    # China Flagpole & Flag at x=510
    draw.rectangle([508, 110, 511, 190], fill="#94A3B8")
    draw.rectangle([512, 115, 556, 145], fill="#DE2910") # Red field
    # China big star (approx yellow polygon/ellipse)
    draw.ellipse([518, 119, 526, 127], fill="#FFDE00")
    # China small stars
    for cs_pt in [(530, 117), (534, 121), (534, 127), (530, 131)]:
        draw.ellipse([cs_pt[0]-1, cs_pt[1]-1, cs_pt[0]+1, cs_pt[1]+1], fill="#FFDE00")

    # Russia Flagpole & Flag at x=570
    draw.rectangle([568, 110, 571, 190], fill="#94A3B8")
    draw.rectangle([572, 115, 616, 125], fill="#FFFFFF") # White stripe
    draw.rectangle([572, 125, 616, 135], fill="#0039A6") # Blue stripe
    draw.rectangle([572, 135, 616, 145], fill="#D52B1E") # Red stripe

    # Leaders podium / table
    draw.rectangle([430, 190, 594, 205], fill="#334155")
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

    # Map & Stat Bars layout (y: 465 to 640)
    map_y = 465
    draw.rectangle([20, map_y, 600, map_y + 175], fill="#E0F2FE", outline="#0284C7")
    draw.text((35, map_y + 6), "GLOBAL HOTSPOTS MAP", fill="#0369A1", font=get_font("DejaVuSans-Bold.ttf", 10))
    draw.text((35, map_y + 18), "1:Hormuz 2:Kuwait 3:Bahrain 4:Kerch 5:Kyiv 6:Shenzhen 7:Beni 8:Gaza 9:Alaska", fill="#0369A1", font=get_font("DejaVuSans.ttf", 9))
    
    # Grid lines on map
    for gx in range(50, 580, 50):
        draw.line([(gx, map_y + 30), (gx, map_y + 170)], fill="#BAE6FD", width=1)
    for gy in range(map_y + 35, map_y + 175, 25):
        draw.line([(30, gy), (590, gy)], fill="#BAE6FD", width=1)

    def proj(lon, lat, x0=20, y0=map_y+25, w=580, h=145):
        x = x0 + (lon - (-170)) / 360.0 * w
        y = y0 + (80 - lat) / 140.0 * h
        return (int(x), int(y))

    # Detailed Continent Polygons with >= 12 points each
    # North America
    na_pts = [
        proj(-165, 60), proj(-150, 68), proj(-130, 70), proj(-100, 70), proj(-85, 68),
        proj(-60, 60), proj(-55, 52), proj(-70, 42), proj(-75, 35), proj(-81, 25),
        proj(-90, 20), proj(-97, 16), proj(-82, 9), proj(-78, 8), proj(-85, 12),
        proj(-105, 22), proj(-115, 30), proj(-125, 45), proj(-135, 54), proj(-155, 58)
    ]
    draw.polygon(na_pts, fill="#C7D2FE") # Sage/Blue-purple muted

    # South America
    sa_pts = [
        proj(-78, 9), proj(-75, 12), proj(-60, 11), proj(-50, 5), proj(-35, -5),
        proj(-38, -12), proj(-43, -23), proj(-50, -30), proj(-68, -52), proj(-67, -55),
        proj(-74, -40), proj(-75, -20), proj(-81, -5), proj(-80, -1), proj(-77, 8)
    ]
    draw.polygon(sa_pts, fill="#FEF08A") # Yellow/Tan muted

    # Africa
    af_pts = [
        proj(-6, 36), proj(10, 37), proj(32, 31), proj(35, 22), proj(51, 11),
        proj(40, -10), proj(35, -25), proj(18, -34), proj(15, -22), proj(12, -5),
        proj(5, 4), proj(-10, 6), proj(-17, 15), proj(-15, 28), proj(-10, 35)
    ]
    draw.polygon(af_pts, fill="#FDE047") # Ochre muted
    # Madagascar
    mg_pts = [proj(47, -12), proj(50, -15), proj(48, -25), proj(45, -22)]
    draw.polygon(mg_pts, fill="#FDE047")

    # Eurasia (Europe + Asia)
    eu_as_pts = [
        proj(-9, 43), proj(3, 51), proj(10, 55), proj(25, 70), proj(40, 68),
        proj(60, 65), proj(90, 72), proj(140, 70), proj(170, 65), proj(165, 55),
        proj(140, 36), proj(120, 30), proj(102, 10), proj(92, 15), proj(77, 8),
        proj(68, 25), proj(50, 30), proj(35, 36), proj(20, 38), proj(10, 36)
    ]
    draw.polygon(eu_as_pts, fill="#A7F3D0") # Teal/Sage muted

    # Australia
    au_pts = [
        proj(114, -22), proj(130, -12), proj(138, -11), proj(142, -11), proj(153, -27),
        proj(151, -34), proj(145, -38), proj(138, -35), proj(130, -32), proj(115, -32)
    ]
    draw.polygon(au_pts, fill="#FED7AA") # Terracotta muted

    # 9 Hotspot Pins
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
    draw.rectangle([stat_x, map_y, 1004, map_y + 175], fill="#FFFFFF", outline="#D1D5DB")
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
        sy_bar += 34

    # 6 Sections (3 columns x 2 rows) with explicit Icons for the 3 target stories
    sec_data = [
        ("EUROPE", [
            ("Russian strikes kill 4 in Odesa", "At least 4 dead and 13 hurt."),
            ("Kyiv: no peace without Ukraine", "Zelenskyy insists on terms."),
            ("Europe shut out of Shenzhen", "Leaders debate influence.", "flags"), # Icon 2: Three Mini Flags
            ("COP31 talks turn tense", "Draft deal splits nations."),
            ("Van Gogh sells for $190.4m", "Record price amid row.")
        ]),
        ("MIDDLE EAST", [
            ("Iran defends Gulf strikes", "Tehran calls attacks defence."),
            ("Three tankers burn in Hormuz", "Fires reported in strait."),
            ("Israel pushes into central Gaza", "Rare incursion near Nuseirat."),
            ("Arab League condemns raids", "Bloc denounces hospital threats."),
            ("Lebanon charges Hezbollah men", "Recruitment and weapons case.")
        ]),
        ("AFRICA", [
            ("Ebola global emergency", "11,300+ cases in DRC."),
            ("Ebola vaccines head to trials", "Phase two next week."),
            ("Ethiopia, Eritrea mass troops", "Forces build along border."),
            ("Sudan commander defects", "RSF officer joins army."),
            ("Migrant boat sinks off Senegal", "Dozens missing from vessel.")
        ]),
        ("ASIA-PACIFIC", [
            ("North Korea expands enrichment", "Yongbyon facility extended."),
            ("Lee seeks talks with Pyongyang", "South Korean president appeals."),
            ("Yunus home set ablaze", "Bangladesh tensions flare."),
            ("Indonesia passes asset law", "Parliament approves forfeiture."),
            ("Fiji declares disaster", "El Nino drought threat.")
        ]),
        ("AMERICAS", [
            ("Trump asks court to block TPS", "Admin seeks to end protections."),
            ("Russian charged in Palantir plot", "Targeting tech workers."),
            ("US, Venezuela restore ties", "Hegseth Caracas visit."),
            ("Pastor convicted over Haiti", "Miami court finds role."),
            ("Musk regrets midterm spending", "Billionaire rues outlay.")
        ]),
        ("SCIENCE, CULTURE & SPORT", [
            ("Anthropic record market debut", "AI firm raises record sum.", "barchart"), # Icon 1: Rising Bar Chart
            ("GTA VI arrives after 13 years", "Fans fly to NZ early.", "sunset"), # Icon 3: Sunset
            ("NASA cargo launch cover", "Northrop Grumman CRS-25."),
            ("Red crabs march Christmas Island", "Millions begin migration."),
            ("NZ court backs pay equity", "Ruling on women's rights.")
        ])
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
        for story_tuple in items:
            headline = story_tuple[0]
            deck = story_tuple[1]
            icon_type = story_tuple[2] if len(story_tuple) > 2 else None

            # If icon_type is present, draw small icon (24-32px) immediately LEFT of headline
            text_x_offset = cx + 6
            if icon_type:
                icon_x = cx + 6
                icon_y = iy + 2
                text_x_offset = cx + 32 # leave room for 24-26px icon
                
                if icon_type == "barchart":
                    # Rising Bar Chart (3 bars ascending)
                    draw.rectangle([icon_x, icon_y + 12, icon_x + 5, icon_y + 20], fill="#E11D48")
                    draw.rectangle([icon_x + 7, icon_y + 7, icon_x + 12, icon_y + 20], fill="#E11D48")
                    draw.rectangle([icon_x + 14, icon_y + 2, icon_x + 19, icon_y + 20], fill="#3B82F6")
                elif icon_type == "flags":
                    # Three mini flags
                    for fx_offset in [0, 8, 16]:
                        draw.line([(icon_x + fx_offset, icon_y + 4), (icon_x + fx_offset, icon_y + 20)], fill="#64748B", width=1)
                        draw.rectangle([icon_x + fx_offset, icon_y + 4, icon_x + fx_offset + 6, icon_y + 12], fill="#EF4444")
                elif icon_type == "sunset":
                    # Sunset: purple sky + orange disc half-hidden behind dark skyline
                    draw.rectangle([icon_x, icon_y, icon_x + 22, icon_y + 14], fill="#581C87") # Purple sky
                    draw.ellipse([icon_x + 4, icon_y + 4, icon_x + 16, icon_y + 16], fill="#F97316") # Orange sun
                    draw.rectangle([icon_x, icon_y + 12, icon_x + 22, icon_y + 22], fill="#0F172A") # Dark skyline

            draw.text((text_x_offset, iy), f"• {headline}", fill="#111827", font=get_font("DejaVuSans-Bold.ttf", 9))
            iy += 12
            draw.text((text_x_offset + 8, iy), deck, fill="#4B5563", font=get_font("DejaVuSans.ttf", 9))
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
