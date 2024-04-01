# cli.py
from mountain_manager import MountainManager
from mountain import Mountain
from trail import Trail
from mountain_organiser import MountainOrganiser
from personality import TopWalker, BottomWalker, LazyWalker
from serialize import serialize, deserialize

def run_cli():
    mountain_manager = MountainManager()
    trail = Trail()
    mountain_organiser = MountainOrganiser()

    while True:
        print("\nMountain Trail Manager")
        print("1. Add Mountain")
        print("2. Remove Mountain")
        print("3. Query Mountains")
        print("4. Load Trail Data")
        print("5. Save Trail Data")
        print("6. Simulate Walker's Path")
        print("7. Organize Mountains")
        print("8. Display Mountain Positions")
        print("9. Quit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            name = input("Enter mountain name: ")
            difficulty = int(input("Enter difficulty level: "))
            length = int(input("Enter length: "))
            mountain = Mountain(name, difficulty, length)
            mountain_manager.add_mountain(mountain)
            print(f"Mountain '{name}' added successfully.")
        elif choice == "2":
            name = input("Enter mountain name to remove: ")
            mountain = next((m for m in mountain_manager.mountains if m.name == name), None)
            if mountain:
                mountain_manager.remove_mountain(mountain)
                print(f"Mountain '{name}' removed successfully.")
            else:
                print(f"Mountain '{name}' not found.")
        elif choice == "3":
            print("Mountains:")
            for mountain in mountain_manager.mountains:
                print(f"- {mountain.name} (Difficulty: {mountain.difficulty}, Length: {mountain.length})")
        elif choice == "4":
            filename = input("Enter the filename to load: ")
            try:
                with open(filename, 'r') as file:
                    data = file.read()
                    trail = deserialize(data)
                    print("Trail data loaded successfully.")
            except FileNotFoundError:
                print(f"File '{filename}' not found.")
        elif choice == "5":
            filename = input("Enter the filename to save: ")
            try:
                with open(filename, 'w') as file:
                    data = serialize(trail)
                    file.write(data)
                    print("Trail data saved successfully.")
            except IOError:
                print(f"Error occurred while saving the file '{filename}'.")
        elif choice == "6":
            print("Select a walker personality:")
            print("1. Top Walker")
            print("2. Bottom Walker")
            print("3. Lazy Walker")
            personality_choice = input("Enter your choice (1-3): ")
            if personality_choice == "1":
                personality = TopWalker()
            elif personality_choice == "2":
                personality = BottomWalker()
            elif personality_choice == "3":
                personality = LazyWalker()
            else:
                print("Invalid personality choice. Skipping simulation.")
                continue
            trail.follow_path(personality)
            if not personality.mountains:
                print("No mountains found in the path.")
            else:
                print("Walker's Path:")
                for mountain in personality.mountains:
                    print(f"- {mountain.name} (Difficulty: {mountain.difficulty}, Length: {mountain.length})")
        elif choice == "7":
                mountain_organiser.add_mountains(mountain_manager.mountains)
                print("Mountains organized successfully.")
        elif choice == "8":
            print("Mountain Positions:")
            for mountain in mountain_manager.mountains:
                position = mountain_organiser.cur_position(mountain)
                print(f"- {mountain.name} (Position: {position})")
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")