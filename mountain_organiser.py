from sortedcontainers import SortedDict

class MountainOrganiser:
    def __init__(self):
        self.mountains = []
        self.rank = SortedDict()

    def add_mountains(self, mountains):
        self.mountains.extend(mountains)
        self.mountains.sort(key=lambda x: (x.difficulty, x.name))
        self.rank.clear()
        for i, mountain in enumerate(self.mountains, start=1):
            self.rank[mountain] = i

    def cur_position(self, mountain):
        if mountain not in self.rank:
            raise KeyError(f"Mountain '{mountain.name}' not found.")
        return self.rank[mountain]