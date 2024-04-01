import math
from typing import List, Tuple

class DoubleKeyTable:
    def __init__(self, sizes=None, internal_sizes=None):
        # Initialize top-level and internal table sizes
        if sizes is not None:
            self.TABLE_SIZES = sizes
        if internal_sizes is not None:
            self.INTERNAL_SIZES = internal_sizes

        # Initialize top-level and internal hash tables
        self.top_level_table = [None] * self.TABLE_SIZES[-1]
        self.internal_tables = [None] * self.TABLE_SIZES[-1]

    def hash(self, key1, key2):
        # Implement your custom hash function for key1 and key2
        # Return a hash value
        pass

    def hash2(self, key2):
        # Implement your custom hash function for key2
        # Return a hash value
        pass

    def _linear_probe(self, key1, key2, is_insert):
        # Handle linear probing for collisions during insertion and retrieval
        # Return indices to access in the top-level and low-level tables
        pass

    def _resize(self, table):
        # Resize the hash tables when load factor exceeds 0.5
        pass

    def keys(self, key=None):
        # Retrieve top-level and low-level keys based on the provided key
        if key is None:
            top_level_keys = [k1 for k1 in self.top_level_table if k1 is not None]
            return top_level_keys
        else:
            top_index = self.hash(key, None) % self.TABLE_SIZES[-1]
            if self.top_level_table[top_index] == key:
                low_level_keys = [k2 for k2 in self.internal_tables[top_index] if k2 is not None]
                return low_level_keys
            else:
                return []

    def values(self, key=None):
        # Retrieve values from the hash table based on the provided key
        if key is None:
            all_values = []
            for i in range(self.TABLE_SIZES[-1]):
                if self.top_level_table[i] is not None:
                    all_values.extend(self.internal_tables[i])
            return [value for value in all_values if value is not None]
        else:
            top_index = self.hash(key, None) % self.TABLE_SIZES[-1]
            if self.top_level_table[top_index] == key:
                return [value for value in self.internal_tables[top_index] if value is not None]
            else:
                return []
// written this
    def table_size(self):
        # Return the current size of the table
        return len(self.top_level_table)

    def iter_keys(self, key=None):
        # Iterate through keys one by one
        if key is None:
            for k1 in self.top_level_table:
                if k1 is not None:
                    yield k1
        else:
            top_index = self.hash(key, None) % self.TABLE_SIZES[-1]
            if self.top_level_table[top_index] == key:
                for k2 in self.internal_tables[top_index]:
                    if k2 is not None:
                        yield k2

    def iter_values(self, key=None):
        # Iterate through values one by one
        if key is None:
            for i in range(self.TABLE_SIZES[-1]):
                if self.top_level_table[i] is not None:
                    for value in self.internal_tables[i]:
                        if value is not None:
                            yield value
        else:
            top_index = self.hash(key, None) % self.TABLE_SIZES[-1]
            if self.top_level_table[top_index] == key:
                for value in self.internal_tables[top_index]:
                    if value is not None:
                        yield value

    def __getitem__(self, keys):
        # Implement __getitem__ method for accessing values using subscript notation
        pass

    def __setitem__(self, keys, value):
        # Implement __setitem__ method for setting values using subscript notation
        pass

    def __delitem__(self, keys):
        # Implement __delitem__ method for deleting key-value pairs using subscript notation
        pass
