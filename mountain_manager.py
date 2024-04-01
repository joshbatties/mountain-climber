class Mountain:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty


class MountainManager:
    def __init__(self):
        self.mountains = []

    def add_mountain(self, mountain):
        self.mountains.append(mountain)

    def remove_mountain(self, mountain):
        if mountain in self.mountains:
            self.mountains.remove(mountain)

    def edit_mountain(self, old_mountain, new_mountain):
        self.remove_mountain(old_mountain)
        self.add_mountain(new_mountain)

    def mountains_with_difficulty(self, diff):
        return [mountain for mountain in self.mountains if mountain.difficulty == diff]

    def group_by_difficulty(self):
        grouped_mountains = [[] for _ in range(11)]  # Assuming difficulties range from 1 to 10
        for mountain in self.mountains:
            grouped_mountains[mountain.difficulty].append(mountain)
        return [mountains for mountains in grouped_mountains if mountains]


# Sample usage
if __name__ == "__main__":
    mountain1 = Mountain("Mount Everest", 10)
    mountain2 = Mountain("K2", 9)
    mountain3 = Mountain("Mount Kilimanjaro", 7)

    manager = MountainManager()
    manager.add_mountain(mountain1)
    manager.add_mountain(mountain2)
    manager.add_mountain(mountain3)

    diff_9_mountains = manager.mountains_with_difficulty(9)
    print("Mountains with difficulty 9:")
    for mountain in diff_9_mountains:
        print(mountain.name)

    grouped_mountains = manager.group_by_difficulty()
    print("\nMountains grouped by difficulty:")
    for i, mountains in enumerate(grouped_mountains):
        for mountain in mountains:
            print(f"Difficulty {i}: {mountain.name}")
