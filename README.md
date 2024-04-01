# mountain-climber

# main.py

This is a GUI application built using the Arcade library in Python. It is a program for visualizing and managing mountain trails, allowing users to add, remove, edit, and view details of different mountains and their trails.

Here are the main components and functionalities:

GUI Setup: The MyWindow class sets up the graphical user interface (GUI) with various UI elements such as buttons, input fields, and layouts using the arcade.gui module.
Drawing and Rendering: The on_draw method handles the drawing and rendering of the mountain trails, action buttons, and other GUI elements on the screen.
Mouse Interactions: The on_mouse_press, on_mouse_release, and on_mouse_motion methods handle mouse events, enabling user interactions such as adding, removing, or editing trails based on the current draw mode.
Draw Modes: The application supports different draw modes, including adding mountains, adding trail branches, removing trails, and editing mountain details. These modes are toggled using the action buttons on the sidebar.
Mountain Management: The MountainManager class (not provided) seems to handle the management of mountains, allowing the addition, removal, and editing of mountains and their associated trails.
Trail Visualization: The TrailDraw class (not provided) appears to be responsible for rendering the trails on the screen.
Mountain Graph: The application includes a feature to display a graph representing the difficulty levels and positions of the mountains.
File Management: There is functionality to save and load mountain trail data to and from JSON files.

Overall, the main.py file serves as the main entry point and controller for the GUI application, handling user interactions, drawing mountain trails, and managing the associated data.

# mountain.py
implementation of a Mountain class using Python's dataclass. This class represents a mountain with the following attributes:

name (str): The name of the mountain.
difficulty_level (int): The difficulty level of the mountain, represented by an integer value.
length (int): The length or distance of the mountain trail, also represented as an integer value.
The @dataclass decorator is a way to automatically add special methods like __init__, __repr__, __eq__, etc., to the class. It helps to reduce boilerplate code and makes the class more concise and readable.

With this implementation, you can create instances of the Mountain class by providing values for the name, difficulty_level, and length attributes.

Example usage:
>>>mountain1 = Mountain("Mount Everest", 5, 20)
>>>mountain2 = Mountain("Mount Kilimanjaro", 3, 15)
In the above example, mountain1 represents a mountain named "Mount Everest" with a difficulty level of 5 and a length of 20 units, while mountain2 represents a mountain named "Mount Kilimanjaro" with a difficulty level of 3 and a length of 15 units.

This implementation is a basic data structure for representing a mountain and its properties. 
Overall, the mountain.py file provides a simple data structure for representing mountains, which can be used as a building block for the larger application.

# mountain_manager.py
The mountain_manager.py file provides an implementation of the MountainManager class, which is responsible for managing a collection of Mountain objects. It also includes a basic implementation of the Mountain class itself.

Here's a breakdown of the code:

Mountain Class:
The Mountain class has an __init__ method that takes two arguments: name (str) and difficulty (int).
These attributes represent the name and difficulty level of a mountain, respectively.
MountainManager Class:
The MountainManager class has an __init__ method that initializes an empty list self.mountains to store Mountain objects.
The add_mountain method takes a Mountain object as an argument and appends it to the self.mountains list.
The remove_mountain method takes a Mountain object as an argument and removes it from the self.mountains list if it exists.
The edit_mountain method takes two arguments: old_mountain (the existing Mountain object) and new_mountain (the updated Mountain object). It first removes the old_mountain from the list and then adds the new_mountain.
The mountains_with_difficulty method takes a diff argument (int) and returns a list of Mountain objects that have the specified difficulty level.
The group_by_difficulty method returns a list of lists, where each inner list contains Mountain objects with the same difficulty level. The outer list is ordered by difficulty level, with the first inner list containing mountains with difficulty 1, the second inner list containing mountains with difficulty 2, and so on.
The file also includes a sample usage section at the bottom, which creates three Mountain objects (mountain1, mountain2, and mountain3) with different difficulty levels. It then creates a MountainManager instance (manager) and adds the three mountains to it.

The sample usage demonstrates the following:

Retrieving mountains with a specific difficulty level (9) using manager.mountains_with_difficulty(9).
Grouping mountains by difficulty level using manager.group_by_difficulty().

This implementation of the MountainManager class allows you to manage a collection of Mountain objects, add new mountains, remove existing mountains, edit mountain details, and retrieve or group mountains based on their difficulty levels.

# trail.py
The trail.py file contains several classes related to representing and managing mountain trails. Let's break down the components:

TrailSplit:
Represents a split in the trail, where the trail can branch into two paths (top and bottom) and then continue with a following trail.
It has a remove_branch method that removes the branch and returns the remaining following trail.
TrailSeries:
Represents a series of trails, where a mountain is followed by a following trail.
It has methods to remove the mountain (remove_mountain), add a mountain before (add_mountain_before), add an empty branch before (add_empty_branch_before), add a mountain after (add_mountain_after), and add an empty branch after (add_empty_branch_after).
Trail:
Represents a trail, which can be a TrailSplit, TrailSeries, or None.
It has methods to add a mountain before (add_mountain_before) and add an empty branch before (add_empty_branch_before).
The follow_path method allows traversing the trail based on a WalkerPersonality instance (not provided), which determines how to navigate through splits (choosing the top, bottom, or stopping).
The collect_all_mountains method is intended to return a list of all mountains contained within the trail, but its implementation is not provided.
The difficulty_maximum_paths and difficulty_difference_paths methods are not implemented and raise NotImplementedError.
Type Aliases:
TrailStore is a type alias for Union[TrailSplit, TrailSeries, None], representing the different types of trail stores.

# mountain_organiser.py
The mountain_organiser.py file implements the MountainOrganiser class, which is used to organize and rank a collection of Mountain objects based on their difficulty and name.

Here's a breakdown of the code:

Mountain Class:
This is a simple implementation of the Mountain class.
Each Mountain object has a name (str) and a difficulty (int) attribute.
MountainOrganiser Class:
The __init__ method initializes two data structures:
self.mountains: A list to store all Mountain objects.
self.rank: A SortedDict (from the sortedcontainers library) to store the ranking of the mountains.
The add_mountains method takes a list of Mountain objects and performs the following tasks:
Extends the self.mountains list with the new mountains.
Sorts the self.mountains list based on the difficulty (ascending) and then on the name (lexicographically ascending).
Rebuilds the self.rank dictionary by assigning ranks to the mountains based on their sorted order in the self.mountains list.
The cur_position method takes a Mountain object as input and returns its current rank (position) in the self.rank dictionary. If the Mountain object is not found, it raises a KeyError.
The file also includes an example usage section at the bottom, which demonstrates the following:

Creating three Mountain objects: mountain1, mountain2, and mountain3.
Initializing a MountainOrganiser instance organiser.
Adding mountain1 and mountain2 to the organizer and printing their positions (ranks).
Adding mountain3 to the organizer and printing its position.
The MountainOrganiser class is designed to manage a collection of Mountain objects and maintain their ranking based on difficulty and name. It uses the SortedDict data structure from the sortedcontainers library to efficiently store and retrieve the ranks of the mountains.

Note that this implementation assumes the sortedcontainers library is installed and available in your Python environment. If not, you can install it using pip install sortedcontainers.

# double_key_table.py
The double_key_table.py file provides an implementation of the DoubleKeyTable class, which is a hash table data structure that allows storing and retrieving values using two keys (key1 and key2). This data structure is useful when you need to associate a value with a combination of two keys.

Here's a breakdown of the code:

Initialization:

The __init__ method takes two optional arguments: sizes and internal_sizes.

sizes is a list of sizes for the top-level table, and internal_sizes is a list of sizes for the internal tables.

The top_level_table and internal_tables are initialized as lists of None values, with sizes based on the provided TABLE_SIZES and INTERNAL_SIZES.

Hash Functions:

The hash and hash2 methods are placeholders for implementing custom hash functions for key1 and key2, respectively.

These methods should return a hash value for the respective keys.

Linear Probing:

The _linear_probe method is a placeholder for handling linear probing in case of collisions during insertion and retrieval.

It should return indices to access the top-level and low-level tables.

Resizing:

The _resize method is a placeholder for resizing the hash tables when the load factor exceeds 0.5.

Key and Value Retrieval:

The keys method retrieves the top-level and low-level keys based on the provided key.

The values method retrieves the values from the hash table based on the provided key.

The iter_keys and iter_values methods are generators that iterate through keys and values, respectively, with an optional key filter.

Table Size:

The table_size method returns the current size of the top-level table.

Subscript Notation:

The __getitem__, __setitem__, and __delitem__ methods are placeholders for implementing subscript notation for accessing, setting, and deleting key-value pairs, respectively.

The provided implementation is a skeleton that outlines the structure and expected functionality of the DoubleKeyTable class.

# serialize.py
The serialize.py file contains two functions, serialize and deserialize, which are used to convert Python objects to JSON and vice versa, respectively. These functions are specifically designed to work with the Trail, TrailSplit, TrailSeries, and Mountain classes from the trail and mountain modules.

EnhancedJSONEncoder:
This class is a custom JSON encoder that extends the json.JSONEncoder class.
It is used to handle the serialization of dataclasses (such as Mountain, TrailSplit, and TrailSeries) by converting them to dictionaries using dataclasses.asdict.
The remove_box method is a helper method that removes keys ending with "_box" from the dictionaries. This is likely a custom requirement specific to your project.
serialize:
This function takes a Trail object as input and returns a JSON string representation of that object.
It uses the EnhancedJSONEncoder to handle the serialization of dataclasses.
deserialize:
This function takes a Python dictionary (or a JSON object) as input and returns a Trail object.
It recursively deserializes the nested TrailSplit and TrailSeries objects.
It uses the Mountain class to create instances of Mountain objects from the dictionary representations.
Here's an example of how these functions might be used:

Create a trail object
mountain1 = Mountain("Mount Everest", 5, 20)
trail1 = TrailSeries(mountain1, Trail(None))

Serialize the trail object to JSON
json_data = serialize(trail1)
print(json_data)

Deserialize the JSON data back to a Trail object
new_trail = deserialize(json.loads(json_data))
The serialize and deserialize functions provide a way to convert the complex Trail object structure, along with its nested TrailSplit, TrailSeries, and Mountain objects, to and from JSON format. This can be useful for storing or transmitting the trail data in a serialized format, or for persisting it to disk or a database.

# draw_trails.py\
The draw_trails.py file contains the TrailDraw class, which is responsible for determining the location and size of trail objects in the GUI application. It is used to draw and visualize the mountain trails based on the data structures defined in the trail module.

Here's a breakdown of the key components in this file:

Box Dataclass:
The Box dataclass represents a rectangular area with x, y, w (width), and h (height) attributes.
It implements the __contains__ method to check if a given point (x, y) is within the box.
TrailSplitBox, TrailSeriesBox, TrailBox:
These dataclasses extend the TrailSplit, TrailSeries, and Trail classes from the trail module, respectively.
They add additional attributes related to bounding boxes for different components of the trail (e.g., branch_start_box, mountain_box, trail_box).
TrailDraw Class:
The TrailDraw class is responsible for drawing and visualizing the trails.
It has several constants for controlling the visual aspects of the trails, such as separations, heights, and widths.
The __init__ method takes a TrailBox object as input.
The required_height and required_width methods calculate the required height and width, respectively, for drawing the given trail.
The draw_in_box method recursively draws the trail components (mountains, branches, and lines) within a specified box (x, y, width, height).
The draw_line, draw_mountain, and draw_branch methods are helper methods for drawing specific components of the trail.
The box_and_action method is a crucial method that determines the appropriate bounding box and action (e.g., adding a mountain, adding a branch, removing a trail) based on the mouse position and the current draw mode.
The draw_trails.py file relies on the arcade library for drawing graphics and text on the screen. It also imports the Mountain class from mountain.py, the Trail, TrailSeries, and TrailSplit classes from trail.py, and the DrawMode constants from constants.py.

# base_enum.py:
Defines a BaseEnum class that extends the built-in Enum class.
Overrides the __eq__ method to compare enum values based on their string representation, which is useful when classes are imported from different locations.
constants.py:
Imports the BaseEnum class from base_enum.py.
Defines the DrawMode enum, which inherits from BaseEnum.
The DrawMode enum represents the different modes for drawing and interacting with the mountain trails, such as editing, adding mountains, adding branches, and removing trails.

# infinite_hash_table.py:
Defines an InfiniteHashTable class, which is a generic hash table implementation.
The class provides methods for getting, setting, and deleting key-value pairs, as well as retrieving the location of a key and sorting the keys in lexicographical order.
However, most of the methods in this class are marked as NotImplementedError, indicating that the actual implementation is not provided.
# utils.py:
Contains two utility functions: av and bezier.
The av function calculates the average of a sequence of numbers.
The bezier function is a helper function for drawing Bézier curves, which is used in the draw_trails module.

# personality.py:
Defines the PersonalityDecision enum, which inherits from BaseEnum.
Introduces the WalkerPersonality abstract base class, which represents different personalities for navigating mountain trails.
Provides three concrete implementations of WalkerPersonality: TopWalker, BottomWalker, and LazyWalker.
These classes define different strategies for selecting branches at trail splits based on the specified personality.

