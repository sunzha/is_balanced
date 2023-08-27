""" Queue ADT and an array implementation.

Defines a generic abstract queue with the usual methods, and implements 
a circular queue using arrays. Also defines UnitTests for the class.
"""

from abc import ABC, abstractmethod 
from typing import TypeVar, Generic
T = TypeVar('T')


class Queue(ABC, Generic[T]):
    """ Abstract class for a generic Queue. """
   
    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def append(self,item:T) -> None:
        """ Adds an element to the rear of the queue."""
        pass

    @abstractmethod
    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front."""
        pass

    def __len__(self) -> int:
        """ Returns the number of elements in the queue."""
        return self.length

    def is_empty(self) -> bool:
        """ True if the queue is empty. """
        return len(self) == 0
