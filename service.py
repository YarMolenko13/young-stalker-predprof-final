from share import maze
from PIL import Image, ImageDraw


def draw_swans(coords):
    try:
        image = Image.open("app/map.png")
        draw = ImageDraw.Draw(image)

        for y in range(len(coords)):
            for x in range(len(coords[0])):
                fill = ""
                if coords[y][x] == 1:
                    fill = "blue"
                elif coords[y][x] == 2:
                    fill = "red"
                elif coords[y][x] == 3:
                    fill = "green"
                if coords[y][x] != 0:
                    draw.rectangle(
                        (5 + (50 * x),
                         5 + (50 * y),
                         45 + (50 * x),
                         45 + (50 * y)),
                        fill=fill)
        image.show()
        image.save("app/static/image.png")
    except FileNotFoundError:
        # TODO
        print("Файл не найден")


draw_swans(maze)
