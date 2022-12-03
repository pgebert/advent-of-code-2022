class Octopus:

    def __init__(self, energy: str):
        self.energy = int(energy)
        self.flashed_in_step = False

    def increase_energy(self) -> bool:

        if self.energy >= 9:
            self.energy = 0
            self.flashed_in_step = True
            return True

        elif not self.flashed_in_step:
            self.energy += 1

        return False

    def __repr__(self):
        return str(self.energy)
