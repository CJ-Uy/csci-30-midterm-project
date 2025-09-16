from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

if __name__ == "__main__":
    # initialize window
    stdkeys.create_window()

    keyboard = "q2we4r5ty7u8i9op-[=]"
    CONCERT = [i for i in range(220, 660, (660 - 220) // (20 - 1))]
    guitar_strings = [GuitarString(440 * 1.059463 ** (i-12)) for i in range(len(keyboard) + 1)]

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
                guitar_strings[string_index].pluck()

        # compute the superposition of samples
        sample = 0 
        for i in guitar_strings:
            sample += i.sample()
        
        # play the sample on standard audio
        play_sample(sample)

        # advance the simulation of each guitar string by one step
        for string in guitar_strings:
            string.tick()
