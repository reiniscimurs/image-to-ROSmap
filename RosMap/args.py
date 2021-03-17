import argparse


def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("--resolution", "-r", help="Manually set pixel resolution",
                        type=float, default=0.5)
    parser.add_argument("--measure","-m", help="Weather to measure the pixel resolution in image",
                         default=False, action='store_true')
    parser.add_argument("--originx", "-ox", help="Set x origin",
                        type=int, default=-1)
    parser.add_argument("--originy", "-oy", help="Set y origin",
                        type=int, default=-1)
    parser.add_argument("--occupied", "-oc", help="Occupied pixel threshold",
                        type=float, default=0.5)
    parser.add_argument("--free", "-fr", help="Free pixel threshold",
                        type=float, default=0.1)

    return parser.parse_args()


d_args = get_arguments()
