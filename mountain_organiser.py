from sortedcontainers import SortedDict

class Mountain:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

class MountainOrganiser:
    def __init__(self):
        self.mountains = []  # List to store all mountains
        self.rank = SortedDict()  # Sorted dictionary to store the ranking

    def add_mountains(self, mountains):
        # Add the new mountains to the list
        self.mountains.extend(mountains)
        # Sort the list by difficulty and then by name lexicographically
        self.mountains.sort(key=lambda x: (x.difficulty, x.name))
        # Rebuild the ranking dictionary
        self.rank.clear()
        for i, mountain in enumerate(self.mountains):
            self.rank[mountain] = i + 1

    def cur_position(self, mountain):
        if mountain not in self.rank:
            raise KeyError(f"Mountain '{mountain.name}' not found.")
        return self.rank[mountain]

# Example usage
if __name__ == "__main__":
    mountain1 = Mountain("Everest", 8848)
    mountain2 = Mountain("K2", 8611)
    mountain3 = Mountain("Makalu", 8485)

    organiser = MountainOrganiser()
    organiser.add_mountains([mountain1, mountain2])
    print(organiser.cur_position(mountain1))  # Output: 1
    print(organiser.cur_position(mountain2))  # Output: 2

    organiser.add_mountains([mountain3])
    print(organiser.cur_position(mountain3))  # Output: 3
