#!/usr/bin/env python3
"""
sticker-cutout.py — 把 YC IP 贴纸的纯白底抠成透明 PNG。

用途：yc-ip 的 Sticker / Minimal 模式生成的贴纸是「纯白 #FFFFFF 底」，
要贴到 yc-design 的奶白页面（#fefcf6）上当装饰，需要先把白底抠透明，
让角色「浮」在页面里，而不是带一个白方块。

做法：从图片四边的白色像素做洪水填充（flood fill），只抠掉「与边缘相连」
的白背景，保留角色内部的白衬衫 / 白鞋 / 白气泡等，避免punch洞。

依赖：Pillow（pip install --user --break-system-packages Pillow）

用法：
  # 单张
  python3 sticker-cutout.py 输入.png 输出.png
  # 整个文件夹（输出到 <文件夹>/cutout/）
  python3 sticker-cutout.py /path/to/raw-stickers/
"""
import sys, os
from collections import deque
from PIL import Image

# 白底判定阈值：接近纯白且低饱和（灰白）才算背景
WHITE_MIN = 234      # min(r,g,b) 高于此值
SAT_MAX = 16         # max-min 低于此值（避免误抠彩色）

def is_bg(px):
    r, g, b = px[0], px[1], px[2]
    return min(r, g, b) > WHITE_MIN and (max(r, g, b) - min(r, g, b)) < SAT_MAX

def cutout(in_path, out_path):
    im = Image.open(in_path).convert("RGBA")
    w, h = im.size
    px = im.load()
    visited = [[False] * w for _ in range(h)]
    q = deque()
    # 从四条边的背景像素入队
    for x in range(w):
        for y in (0, h - 1):
            if is_bg(px[x, y]) and not visited[y][x]:
                visited[y][x] = True; q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if is_bg(px[x, y]) and not visited[y][x]:
                visited[y][x] = True; q.append((x, y))
    # 洪水填充
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and is_bg(px[nx, ny]):
                visited[ny][nx] = True; q.append((nx, ny))
    # 抠掉标记的背景
    for y in range(h):
        for x in range(w):
            if visited[y][x]:
                r, g, b, _ = px[x, y]
                px[x, y] = (r, g, b, 0)
    # 裁到内容边界
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    im.save(out_path)
    print(f"✓ {os.path.basename(out_path)}  {im.size}")

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    src = sys.argv[1]
    if os.path.isdir(src):
        out_dir = os.path.join(src, "cutout")
        for f in sorted(os.listdir(src)):
            if f.lower().endswith((".png", ".jpg", ".jpeg")):
                cutout(os.path.join(src, f), os.path.join(out_dir, os.path.splitext(f)[0] + ".png"))
    else:
        out = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + "-cutout.png"
        cutout(src, out)

if __name__ == "__main__":
    main()
