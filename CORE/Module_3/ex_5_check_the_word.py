def goes_after(word: str, first: str, second: str) -> bool:
    try:
        return word.index(second) - word.index(first) == 1

    except ValueError:
        return False


goes_after("world", "w", "o")
goes_after("world", "w", "r")
goes_after("world", "l", "o")
goes_after("panorama", "a", "n")
goes_after("list", "l", "o")
goes_after("", "l", "o")
goes_after("list", "l", "l")
goes_after("world", "d", "w")
goes_after("Almaz", "a", "l")
goes_after("Almaz", "r", "l")
