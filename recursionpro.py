import argparse
import shutil
from pathlib import Path


def parse_argv():
    parser = argparse.ArgumentParser("Сортування картинок")
    parser.add_argument(
        "-S", "--source", type=Path, required=True, help="Папка з картінками"
    )
    parser.add_argument(
        "-O",
        "--output",
        type=Path,
        default=Path("output"),
        help="Папка з відсортованими картінками",
    )
    return parser.parse_args()


def recursive_copy(src: Path, dst: Path):
    for item in src.iterdir():
        if item.is_dir():
            recursive_copy(item, dst)
        else:
            try:
                folder = dst / item.name[:1]  # output/f
                folder.mkdir(exist_ok=True, parents=True)
                with open(item, 'rb') as fsrc, open(folder / item.name, 'wb') as fdst:
                    shutil.copyfileobj(fsrc, fdst)
                print(f"Копіювання файлу: {item} -> {folder}")
            except Exception as e:
                print(f"Помилка копіювання файлу {item}: {e}")


def main():
    args = parse_argv()
    print(f"Вхідні аргументи: {args}")
    recursive_copy(args.source.resolve(), args.output.resolve())


if __name__ == "__main__":
    main()
