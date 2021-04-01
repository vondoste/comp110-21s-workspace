"""RV09 filter example."""


def odd_length(words: list[str]) -> list[bool]:
    result: list[bool] = []
    for e in words:
        if len(e) % 2 == 1:
            result.append(True)
        else:
            result.append(False)
    return result


def filter_str(words: list[str], mask: list[bool]) -> list[str]:
    result: list[str] = []
    for i in range(len(words)):
        if mask[i]:
            result.append(words[i])
    return result

example = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth", "1st Samuel", "2nd Samuel", "1st Kings", "2nd Kings", "1st Chronicles", "2nd Chronicles", "Ezra", "Nehemiah", "Esther", "Job", "Psalms", "Proverbs", "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi", "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1st Corinthians", "2nd Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1st Thessalonians", "2nd Thessalonians", "1st Timothy", "2nd Timothy", "Titus", "Philemon", "Hebrews", "James", "1st Peter", "2nd Peter", "1st John", "2nd John", "3rd John", "Jude", "Revelation"]
mask = odd_length(example)
odd = filter_str(example, mask)
print(len(example))
print(len(odd))
print(f"Odd length words are {odd} ")