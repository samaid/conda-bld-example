from demo_module import hello_init, hello_main

from demo_module.impl.compute import compute_init, compute_update, M, N
from demo_module.impl.visualize import visual_init, visual_draw, visual_prepare_next_frame, visual_user_cancelled
from demo_module.impl.visualize import visual_finalize

def main():
    print("Printing all hello messages from main_demo")
    hello_init()
    hello_main()

    values = compute_init(M, N)
    surface = visual_init(M*10, N*10)
    do_demo = True
    frames = 0
    while do_demo:
        # Compute update
        values = compute_update(frames, values)

        # Visual update
        visual_draw(surface, frames)

        # Prepare for the next iteration
        not_reached_max_frames = visual_prepare_next_frame(surface, frames)
        frames += 1
        do_demo = not visual_user_cancelled() and not_reached_max_frames


    visual_finalize()


if __name__ == "__main__":
    main()
