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
engine.draw_line(50, 50, 150, 150, (255, 0, 0))
engine.draw_line(50, 150, 150, 50, (0, 255, 0))
engine.save_image('lines.ppm')

