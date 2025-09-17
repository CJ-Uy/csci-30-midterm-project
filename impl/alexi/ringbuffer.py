#!/usr/bin/env python3

class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''
        # TO-DO: implement this
        self.MAX_CAP = capacity
        self._front = 0
        self._rear =  0
        self.buffer = [None] * capacity

    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''
        if self._rear > self._front:
            return self._rear - self._front
        elif self._rear < self._front:
            self._rear + self.MAX_CAP - self._front
        else:
            if self.buffer[self._front] is None:
                return 0
            else:
                return self.MAX_CAP

        # TO-DO: implement this

    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        return self.size() == 0
        # TO-DO: implement this
        
    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        return self.size() == self.MAX_CAP
        # TO-DO: implement this

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        if self.is_full():
            raise RingBufferFull

        index = self._rear
        if (index >= self.MAX_CAP):
            index = 0

        self.buffer[index] = x
        self._rear = index + 1

        # TO-DO: implement this

    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        if self.is_empty():
            raise RingBufferEmpty
        index = self._front
        item = self.buffer[index]
        self.buffer[index] = None
        index += 1
        if (index >= self.MAX_CAP):
            index = 0
        self._front = index
        return item
        # TO-DO: implement this

    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        if self.is_empty():
            raise RingBufferEmpty
        return self.buffer[self._front]
        # TO-DO: implement this


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
