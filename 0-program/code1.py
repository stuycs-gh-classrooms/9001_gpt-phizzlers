class PPMImage:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = bytearray(width * height * 3)
        
    def set_pixel(self, x, y, color):
        index = (y * self.width + x) * 3
        self.data[index] = color[0]
        self.data[index + 1] = color[1]
        self.data[index + 2] = color[2]
        
    def save(self, filename):
        with open(filename, 'wb') as f:
            f.write(b'P6\n{} {}\n255\n'.format(self.width, self.height).encode())
            f.write(self.data)

class GraphicsEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = PPMImage(width, height)
        self.edge_matrix = []
        
    def add_point(self, x, y, z=0):
        self.edge_matrix.append([x, y, z, 1])
        
    def add_edge(self, x0, y0, z0, x1, y1, z1):
        self.add_point(x0, y0, z0)
        self.add_point(x1, y1, z1)
        
    def draw_edges(self, color):
        for i in range(0, len(self.edge_matrix), 2):
            x0, y0, z0, w0 = self.edge_matrix[i]
            x1, y1, z1, w1 = self.edge_matrix[i + 1]
            if w0 != 0 and w1 != 0:
                sx0 = int((x0 + 1) * self.width / 2)
                sy0 = int((y0 + 1) * self.height / 2)
                sx1 = int((x1 + 1) * self.width / 2)
                sy1 = int((y1 + 1) * self.height / 2)
                self.draw_line(sx0, sy0, sx1, sy1, color)
                
    def draw_line(self, x0, y0, x1, y1, color):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        while x0 != x1 or y0 != y1:
            self.image.set_pixel(x0, y0, color)
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
                
    def save_image(self, filename):
        self.image.save(filename)

engine = GraphicsEngine(200, 200)
engine.add_edge(-1, 0, 0, 1, 0, 0)
engine.add_edge(0, -1, 0, 0, 1, 0)
engine.add_edge(-1, -1, 0, 1, 1, 0)
engine.draw_edges((255, 0, 0))
engine.save_image('edges.ppm')

