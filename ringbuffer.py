#!/usr/bin/env python3

class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''
        # TO-DO: implement this
        self.MAX_CAP = capacity
        self._front = 0
        self._rear = 0
        self.buffer = [None] * self.MAX_CAP

    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''
        if self._rear > self._front:
            return self._rear - self._front
        elif self._rear < self._front:
            self._rear + self.MAX_CAP - self._front
        else:
            # If empty
            if self.buffer[self._front] is None:
                return 0
            else:
                return self.MAX_CAP

    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        return self.size() == 0
        
    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        return self.size() == self.MAX_CAP

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        # If the buffer is full
        if self.is_full():
            raise RingBufferFull
            
        self.buffer[self._rear] = x
        self._rear += 1
        
        if self._rear >= self.MAX_CAP:
            self._rear = 0

    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        if self.is_empty():
            raise RingBufferEmpty
        
        # Delete front and move
        self._front += 1
        
        # Loop front to the first index if it's greater than the cap
        if self._front >= self.MAX_CAP:
            self._front = 0
        
        temp = self.buffer[self._front - 1]
        self.buffer[self._front - 1] = None
        
        return temp

    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        if self.is_empty():
            raise RingBufferEmpty
        
        return self.buffer[self._front]


class RingBufferFull(Exception):
    '''
    The exception raised when the ring buffer is full when attempting to
    enqueue.
    '''
    pass

class RingBufferEmpty(Exception):
    '''
    The exception raised when the ring buffer is empty when attempting to
    dequeue or peek.
    '''
    pass
