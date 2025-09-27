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
    active_strings = set()

    for i in range(len(keyboard)):
        guitar_strings.append(GuitarString(440 * 1.059463 ** (i - 12)))

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
            if key in keyboard and len(key) != 0:
                string_index = keyboard.index(key)
                string = guitar_strings[string_index]
                string.pluck()
                active_strings.add(string)

        # compute the superposition of samples
        sample = 0
        for i in range(len(guitar_strings)):
            string = guitar_strings[i]
            # if it has been too long since the string was last played
            if string.time() > 300000:
                active_strings.remove(string)
                # create an empty ring buffer
                reset = RingBuffer(string.capacity)
                for _ in range(string.capacity):
                    reset.enqueue(0)
                # reset the buffer of the string
                string.buffer = reset
                # reset the time since last played of the string
                string.tick_count = 0
            sample += string.sample()
        
        # play the sample on standard audio
        if -1 < sample < 1:
            play_sample(sample)
        elif sample > 1:
            play_sample(1)
        else:
            play_sample(-1)

        # advance the simulation of each guitar string by one step
        for string in active_strings:
            string.tick()
