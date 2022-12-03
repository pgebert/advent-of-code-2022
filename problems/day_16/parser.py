from typing import List

from .package import Package, PackageType
from .utils import hex2binary, binary2decimal


class Parser:

    def __init__(self, hex: str):
        self.binary = hex2binary(hex)
        self.root_package = None

    def parse(self):

        stack = self.binary
        package_pointer = None

        while stack != "" and binary2decimal(stack) != 0:

            version = binary2decimal(stack[0:3])
            type = PackageType(binary2decimal(stack[3:6]))

            package = Package(version=version, type=type)

            if package.is_operator():

                # Get length type
                length_type = int(stack[6])
                if length_type == 1:
                    package.number_of_contained_bits = 18
                    package.number_of_expected_children = binary2decimal(stack[7:18])
                    stack = stack[18:]

                else:
                    package.number_of_contained_bits = 22
                    package.number_of_expected_bits = binary2decimal(stack[7:22])
                    stack = stack[22:]
            else:
                stack = stack[6:]
                package.number_of_contained_bits = 6
                contained_bits = ""

                while True:
                    package.number_of_contained_bits += 5

                    control_bit = stack[0]
                    contained_bits += stack[1:5]
                    stack = stack[5:]

                    if int(control_bit) == 0:
                        break

                package.value = binary2decimal(contained_bits)

            while (package_pointer is not None
                   and package_pointer.number_of_expected_children <= package_pointer.get_number_of_contained_children()
                   and package_pointer.number_of_expected_bits <= package_pointer.get_number_of_contained_bits_in_children()):
                package_pointer = package_pointer.parent

            if package_pointer is None:
                self.root_package = package
                package_pointer = package
            else:
                package_pointer.children.append(package)
                package.parent = package_pointer
                package_pointer = package

    def get_versions(self) -> List[int]:

        versions = []

        if self.root_package is not None:
            versions.extend(self._get_versions_recursively(self.root_package))

        return versions

    def _get_versions_recursively(self, package: Package) -> List[int]:

        versions = [package.version]
        for child in package.children:
            versions.extend(self._get_versions_recursively(child))
        return versions
