import math

class PPMImage:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = bytearray(width * height * 3)
        
    def set_pixel(self, x, y, color):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        index = (y * self.width + x) * 3
        self.data[index] = color[0]
        self.data[index + 1] = color[1]
        self.data[index + 2] = color[2] 

    def save(self, filename):
        # Open the file for writing
        with open(filename, 'wb') as f:
        # Write the PPM header
            f.write(bytes('P6\n{} {}\n255\n'.format(self.width, self.height), 'utf-8'))
            # Write the pixel data
            for y in range(self.height):
                for x in range(self.width):
                    pixel = self.buffer[y][x]
                    f.write(bytes([pixel[0], pixel[1], pixel[2]]))

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
    

    def draw_circle(self, x, y, r, color):
        # Use the parametric equation of a circle to generate points
        # along the circumference and add them to the edge matrix.
        step = 10  # Step size in degrees
        num_steps = int(360 / step)
        for i in range(num_steps):
            theta = math.radians(i * step)
            x0 = x + r * math.cos(theta)
            y0 = y + r * math.sin(theta)
            x1 = x + r * math.cos(theta + math.radians(step))
            y1 = y + r * math.sin(theta + math.radians(step))
            self.add_edge(x0, y0, 0, x1, y1, 0)
        self.draw_edges(color)

        
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

# Create a 400x400 image
engine = GraphicsEngine(400, 400)

# Draw a red circle in the center of the image
engine.draw_circle(200, 200, 100, (255, 0, 0))

# Save the result to a PPM file
engine.save_image('circle.ppm')

