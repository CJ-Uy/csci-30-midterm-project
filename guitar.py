from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys
import math
from ringbuffer import RingBuffer

if __name__ == "__main__":
    # initialize window
    stdkeys.create_window()

    keyboard = "q2we4r5ty7u8i9op-[=]"
    guitar_strings = []
    times = []
    for i in range(len(keyboard)):
        guitar_strings.append(GuitarString(440 * 1.059463 ** (i - 12)))
        times.append(float('inf'))

    n_iters = 0
    while True:
        # it turns out that the bottleneck is in polling for key events
        # for every iteration, so we'll do it less often, say every
        # 1000 or so iterations
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        # check if the user has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            if key in keyboard:
                string_index = keyboard.index(key)
                curr = guitar_strings[string_index]
                times[string_index] = curr.time()
                curr.pluck()

        # compute the superposition of samples
        sample = 0
        for i in range(len(guitar_strings)):
            curr = guitar_strings[i]
            if curr.time() - times[i] > 100000:
                print("Stopped")
                temp = RingBuffer(curr.capacity)
                for _ in range(curr.capacity):
                    temp.enqueue(0)
                curr.buffer = temp
                times[i] = float('inf')
            sample += curr.sample()
        
        # play the sample on standard audio
        if -1 < sample < 1:
            play_sample(sample)
        elif sample > 1:
            play_sample(1)
        else:
            play_sample(-1)

        # advance the simulation of each guitar string by one step
        for string in guitar_strings:
            string.tick()
