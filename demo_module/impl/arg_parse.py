from demo_module import int_tuple
import argparse


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Conda-build example for demo application")
    parser.add_argument(
        "--variant",
        help="Implementation variant",
        type=str.casefold,
        choices=["numpy", "numba"],
        default="numpy",
    )
    parser.add_argument(
        "--max-frames",
        help="Stop demo after specified amount of frames (default - no stop frame)",
        type=int,
        default=10000000,
    )
    parser.add_argument(
        "--gui",
        help="Render using specified backend. Default --gui no",
        choices=["pygame", "opencv", "matplotlib", "plotly", "no"],
        default="no",
    )
    m = 10
    n = 20
    parser.add_argument(
        "--task-size",
        help=f"2D task size. E.g. 1200,800. Default {m},{n}",
        type=int_tuple,
        default=int_tuple(f"{m},{n}"),
    )

    args = parser.parse_args(argv)
    return args
