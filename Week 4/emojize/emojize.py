import emoji
import sys


def main():
    try:
        prompt = input("Input: ")
        emo = emoji.emojize(prompt, language="alias")
        if emo == prompt:
            raise ValueError
        else:
            print(emo)
    except ValueError:
        sys.exit("No corresponding emoji")


if __name__ == "__main__":
    main()
