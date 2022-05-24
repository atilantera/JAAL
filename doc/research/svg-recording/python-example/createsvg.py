import svgwrite

vertices = {
    # 'label': (x, y)
    'A': (445, 338),
    'B': (312, 137),
    'C': (68, 238),
    'D': (63, 335),
    'E': (443, 49),
    'F': (185, 244),
    'G': (61, 143),
    'H': (187, 132),
    'I': (50, 46),
    'J': (306, 245),
    'K': (193, 339),
    'L': (437, 136),
    'M': (177, 40),
    'N': (310, 348),
    'O': (305, 41),
    'P': (443, 242)
}

edges = (
    ('IM', 6),
    ('MH', 8),
    ('OE', 4), ('OB', 9), ('OL', 15),
    ('GH', 4), ('GF', 10),
    ('HB', 11), ('HF', 6), ('HJ', 13),
    ('BL', 4), ('BP', 10), ('LP', 7),
    ('FJ', 12),
    ('JN', 10), ('PN', 7),
    ('KN', 3), ('NA', 6),
    ('CD', 2)
)


dwg = svgwrite.Drawing('example1.svg')
dwg.add(dwg.rect((0, 0), (500, 400), fill='#e2eedd'))
for edge in edges:
    v1 = vertices[edge[0][0]]
    v2 = vertices[edge[0][1]]
    w = edge[1]
    dwg.add(dwg.line(v1, v2).stroke('#d59f0d', width=10))
    mid_x = 0.5 * (v1[0] + v2[0])
    mid_y = 0.5 * (v1[1] + v2[1])
    dwg.add(dwg.text(w, (mid_x - 5, mid_y + 5), font_size="16", font_family="Arial",
                     style="text-shadow: 0 0 5px #fff;"))

for label, coord in vertices.items():
    x = coord[0]
    y = coord[1]
    dwg.add(dwg.circle(center=(x, y), r='24', stroke='#002f6c', fill='white'))
    txt = dwg.text(label, (x - 5, y + 5), font_size="14", font_family="Arial")
    dwg.add(txt)

dwg.save(pretty=True, indent=2)
