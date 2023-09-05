def main():
    secret = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    if secret == "42":
        print("Yes.")
    elif secret == "forty two":
        print("Yes.")
    elif secret == "forty-two":
        print("Yes.")
    else:
        print("No.")


main()