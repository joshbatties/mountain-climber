from __future__ import annotations
from abc import ABC, abstractmethod
from enum import auto
from base_enum import BaseEnum
from mountain import Mountain
from trail import Trail, TrailSeries

class PersonalityDecision(BaseEnum):
    TOP = auto()
    BOTTOM = auto()
    STOP = auto()

class WalkerPersonality(ABC):

    def __init__(self) -> None:
        self.mountains = []

    def add_mountain(self, mountain: Mountain) -> None:
        self.mountains.append(mountain)

    @abstractmethod
    def select_branch(self, top_branch: Trail, bottom_branch: Trail) -> PersonalityDecision:
        raise NotImplementedError()

class TopWalker(WalkerPersonality):
     def select_branch(self, top_branch: Trail, bottom_branch: Trail) -> PersonalityDecision:
        return PersonalityDecision.TOP
        

class BottomWalker(WalkerPersonality):
    def select_branch(self, top_branch: Trail, bottom_branch: Trail) -> PersonalityDecision:
        return PersonalityDecision.BOTTOM

class LazyWalker(WalkerPersonality):
    def select_branch(self, top_branch: Trail, bottom_branch: Trail) -> PersonalityDecision:
         def select_branch(self, top_branch: Trail, bottom_branch: Trail) -> PersonalityDecision:
            if isinstance(top_branch.store, TrailSeries) and isinstance(bottom_branch.store, TrailSeries):
                if top_branch.store.mountain.difficulty_level < bottom_branch.store.mountain.difficulty_level:
                    return PersonalityDecision.TOP
                elif top_branch.store.mountain.difficulty_level > bottom_branch.store.mountain.difficulty_level:
                    return PersonalityDecision.BOTTOM
            elif isinstance(top_branch.store, TrailSeries):
                return PersonalityDecision.BOTTOM
            else:
                return PersonalityDecision.TOP
            return PersonalityDecision.STOP
