import time
import random
import math
import sys


class LoadingBar:
    def __init__(self, total, done=0, length=20, full="■", empty=" ", edge_left="[", edge_right="]",
                 prefix_text="", suffix_text=""):
        self.done = done
        self.total = total
        self.length = length

        self.full = full
        self.empty = empty
        self.edge_left = edge_left
        self.edge_right = edge_right

        self.prefix_text = prefix_text
        self.suffix_text = suffix_text
        
        self.percent_text_prefix = " "
        self.percent_text_suffix = "% Done"
        
        self.total_length = (len(self.full * self.length) +
                             len(self.edge_left + self.edge_right) +
                             len(self.prefix_text + self.suffix_text) +
                             len(self.percent_text_prefix) +
                             len(self.percent_text_suffix) +
                             5)

    def show_progress(self):
        progress = self.done / self.total

        filled_boxes = math.floor(progress * self.length)
        empty_boxes = self.length - filled_boxes

        bar_text = self.edge_left + self.full * filled_boxes + self.empty * empty_boxes + self.edge_right
        percent_text = self.percent_text_prefix + f"{progress*100:.2f}" + self.percent_text_suffix

        msg = self.prefix_text + bar_text + percent_text + self.suffix_text

        print(msg, end="") if self.done != self.total else print(msg)
        sys.stdout.flush()

    def increment(self):
        self.done += 1

    def log(self, msg):
        full_msg = msg if len(msg) >= self.total_length else msg + " " * (self.total_length - len(msg))
        print(f"\r{full_msg}")
        self.show_progress()


def _save_file(file, loading_bar):
    loading_bar.log(f"Saving {file} . . .")
    time.sleep(0.05 + random.random() * 1.45)

    loading_bar.increment()
    loading_bar.log("Saved")


def _run_loop(fake_files):
    # Some prefixes and extensions to randomise the filenames
    prefixes = ["some_file", "another_file", "abc", "def"]
    extensions = [".jpg", ".csv", ".mp4", ".mp3"]

    # Initialising loading bar object
    loading_bar = LoadingBar(fake_files)

    for i in range(fake_files):
        # "Saving" a randomly named file
        _save_file(f"{random.choice(prefixes)}{i+1}{random.choice(extensions)}", loading_bar)


def _pause():
    input("\nPress Enter to continue . . . ")


def _main():
    _run_loop(9)
    _pause()


if __name__ == '__main__':
    _main()
