#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

keyboard = "q2we4r5ty7u8i9op-[=]"

strings = {keyboard[i]:GuitarString(440 * (1.059463 ** (i-12))) for i in range(len(keyboard))}


if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

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
            if key in strings:
                strings[key].pluck()

        # compute the superposition of samples
        sample = sum([string.sample() for string in strings.values()])

        # play the sample on standard audio
        if -1 < sample < 1:
            play_sample(sample)
        elif sample > 1:
            play_sample(1)
        else:
            play_sample(-1)

        # advance the simulation of each guitar string by one step
        for string in strings.values():
            string.tick()
