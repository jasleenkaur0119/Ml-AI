import pickle
from pathlib import Path

FILE_PATH = Path("model_best.pkl")


def main() -> None:
    if not FILE_PATH.exists():
        raise FileNotFoundError(f"Could not find: {FILE_PATH}")

    with FILE_PATH.open("rb") as file:
        exported_object = pickle.load(file)

    print("Object type:", type(exported_object))

    if hasattr(exported_object, "get_params"):
        print("\nModel parameters:")
        print(exported_object.get_params())

    if hasattr(exported_object, "shape"):
        print("\nObject shape:")
        print(exported_object.shape)


if __name__ == "__main__":
    main()
