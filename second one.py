import time
import sys

CSI="\x1b[" # префикс ESC-последовательностей

def loading(num_tasks):
    bar_width = 31  # ширина прогресс-бара
    for k in range(1, num_tasks + 1):
        for pct in range(0, bar_width):
            filled = pct
            bar = "@" * filled + "-" * (bar_width - filled)
            # ESC[1G — в начало строки; ESC[2K — очистить строку
            print(f"{CSI}1G{CSI}2KЗадачa {k}/{num_tasks} [{bar}] {pct:3d}%", end="", flush=True)
            time.sleep(0.1) 
if __name__ == "__main__":
    m = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    loading(m)