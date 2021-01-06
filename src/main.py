# Program Entrypoint
from Melody import melody_writer
import os

out_dir = "./out/"


def clear_files():
    for filename in os.listdir(out_dir):
        os.remove(out_dir + filename)


if __name__ == "__main__":
    melody_writer.generate_default()


