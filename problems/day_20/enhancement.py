from typing import List


def binary2decimal(binary: str) -> int:
    return int(binary, 2)


class Enhancement:
    KERNEL_SIZE = 3

    def __init__(self, image: List[str], algorithm: str):

        self.image = image
        self.algorithm = algorithm

    def execute(self, steps):

        for step in range(steps):

            padding = "."
            if self.algorithm[0] == "#":
                padding = "." if step % 2 == 0 else "#"

            self.pad_image(self.KERNEL_SIZE - 1, padding)
            new_image = [["."] * len(row) for row in self.image]

            for y in range(self.KERNEL_SIZE // 2, len(self.image) - self.KERNEL_SIZE // 2):
                for x in range(self.KERNEL_SIZE // 2, len(self.image[y]) - self.KERNEL_SIZE // 2):

                    binary = ""
                    for i in range(self.KERNEL_SIZE):
                        for j in range(self.KERNEL_SIZE):
                            pixel = self.image[y - self.KERNEL_SIZE // 2 + i][x - self.KERNEL_SIZE // 2 + j]
                            binary += "1" if pixel == "#" else "0"

                    index = binary2decimal(binary)

                    new_image[y][x] = self.algorithm[index]

            self.image = new_image
            self.cut_image(self.KERNEL_SIZE // 2)

    def pad_image(self, width: int = 2, value: str = "."):

        assert len(self.image) > 0

        padded_image = []

        for _ in range(width):
            padded_image.append([value] * (2 * width + len(self.image[0])))

        for i, row in enumerate(self.image):
            padded_image.append([value] * width + row + [value] * width)

        for _ in range(width):
            padded_image.append([value] * (2 * width + len(self.image[0])))

        self.image = padded_image

    def cut_image(self, width: int = 2):

        self.image = [row[width: - width] for row in self.image]
        self.image = self.image[width: - width]

    def count_white_pixels(self) -> int:

        return sum([1 if pixel == "#" else 0 for row in self.image for pixel in row])
