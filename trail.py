from __future__ import annotations
from dataclasses import dataclass

from mountain import Mountain

from typing import TYPE_CHECKING, Union
from personality import PersonalityDecision


# Avoid circular imports for typing.
if TYPE_CHECKING:
    from personality import WalkerPersonality

@dataclass
class TrailSplit:
    """
    A split in the trail.
       _____top______
      /              \
    -<                >-following-
      \____bottom____/
    """

    top: Trail
    bottom: Trail
    following: Trail

    def remove_branch(self) -> TrailStore:
        """Removes the branch, should just leave the remaining following trail."""
        return self.following.store

@dataclass
class TrailSeries:
    """
    A mountain, followed by the rest of the trail

    --mountain--following--

    """

    mountain: Mountain
    following: Trail

    def remove_mountain(self) -> TrailStore:
        """
        Returns a *new* trail which would be the result of:
        Removing the mountain at the beginning of this series.
        """
        return self.following.store

    def add_mountain_before(self, mountain: Mountain) -> TrailStore:
        """
        Returns a *new* trail which would be the result of:
        Adding a mountain in series before the current one.
        """
        return TrailSeries(mountain, Trail(self))

    def add_empty_branch_before(self) -> TrailStore:
        """Returns a *new* trail which would be the result of:
        Adding an empty branch, where the current trailstore is now the following path.
        """
        return TrailSplit(Trail(None), Trail(None), Trail(self))

    def add_mountain_after(self, mountain: Mountain) -> TrailStore:
        """
        Returns a *new* trail which would be the result of:
        Adding a mountain after the current mountain, but before the following trail.
        """
        return TrailSeries(self.mountain, Trail(TrailSeries(mountain, self.following)))

    def add_empty_branch_after(self) -> TrailStore:
        """
        Returns a *new* trail which would be the result of:
        Adding an empty branch after the current mountain, but before the following trail.
        """
        return TrailSeries(self.mountain, Trail(TrailSplit(Trail(None), Trail(None), self.following)))

TrailStore = Union[TrailSplit, TrailSeries, None]

@dataclass
class Trail:

    store: TrailStore = None
    def collect_all_mountains(self) -> list[Mountain]:
        mountains = []
        stack = [self]
        while stack:
            trail = stack.pop()
            if isinstance(trail.store, TrailSeries):
                mountains.append(trail.store.mountain)
                stack.append(trail.store.following)
            elif isinstance(trail.store, TrailSplit):
                stack.append(trail.store.following)
                stack.append(trail.store.top)
                stack.append(trail.store.bottom)
        return mountains
    
    def add_mountain_before(self, mountain: Mountain) -> Trail:
        """
        Returns a *new* trail which would be the result of:
        Adding a mountain before everything currently in the trail.
        """
        return Trail(TrailSeries(mountain, self))

    def add_empty_branch_before(self) -> Trail:
        """
        Returns a *new* trail which would be the result of:
        Adding an empty branch before everything currently in the trail.
        """
        return Trail(TrailSplit(Trail(None), Trail(None), self))

    def follow_path(self, personality: WalkerPersonality) -> None:
        stack = [self]
        while stack:
            trail = stack.pop()
            if trail.store is None:
                continue
            if isinstance(trail.store, TrailSeries):
                personality.add_mountain(trail.store.mountain)
                stack.append(trail.store.following)
            elif isinstance(trail.store, TrailSplit):
                stack.append(trail.store.following)
                decision = personality.select_branch(trail.store.top, trail.store.bottom)
                if decision == PersonalityDecision.TOP:
                    stack.append(trail.store.top)
                elif decision == PersonalityDecision.BOTTOM:
                    stack.append(trail.store.bottom)



    def collect_all_mountains(self) -> list[Mountain]:
        """Returns a list of all mountains contained within the Trail.

  Returns:
    A list of all mountains contained within the Trail.
  """

        mountains = []
        
        
    def explore(mountain: Mountain):
        """Recursively explores the trail, starting from the given mountain.

    Args:
      mountain: The mountain to start exploring from.
    """

        mountains.append(mountain)

        for branch in mountain.branches:
            explore(branch)

        explore(self.root)
        return mountains        


    def difficulty_maximum_paths(self, max_difficulty: int) -> list[list[Mountain]]: # Input to this should not exceed k > 50, at most 5 branches.
        # 1008/2085 ONLY!
        raise NotImplementedError()

    def difficulty_difference_paths(self, max_difference: int) -> list[list[Mountain]]: # Input to this should not exceed k > 50, at most 5 branches.
        # 1054 ONLY!
        raise NotImplementedError()
