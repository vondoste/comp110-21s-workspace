"""Handling a large text file."""
lines: list[str] = []
file_handle = open("../data/King James Bible.txt", "r", encoding="utf8")

# Make each line a string in the list
for line in file_handle:
    lines.append(line)

file_handle.close()
print(f"{len(lines)} lines of text read in")

books_of_bible: list[str] = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", 
                            "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", 
                            "Ezra", "Nehemiah", "Esther", "Job", "Psalms", "Proverbs", "Ecclesiastes", 
                            "Song of Songs", "Isaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", 
                            "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", 
                            "Zechariah", "Malachi", "Matthew", "Mark", "Luke", "John", "Acts", "Romans", 
                            "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", 
                            "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", 
                            "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", 
                            "Revelation"]

chapters_of_bible: list[int] = [50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 10, 42, 150, 31, 12, 
                                8, 66, 52, 5, 48, 12, 14, 3, 9, 1, 4, 7, 3, 3, 3, 2, 14, 4, 28, 16, 24, 21, 28, 16, 
                                16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22]

print(f"books_of_bible contains {len(books_of_bible)} entries.")
print(f"chapters_of_bible contains {len(chapters_of_bible)} entries.")

# Make a data structure to hold out bible text.
bible: dict[str, dict[int, list[str]]] = {}

for i in range(len(books_of_bible)):
    book: dict[int, dict[int, str]] = {}
    for j in range(chapters_of_bible[i]):
        book[j] = {}
    bible[books_of_bible[i]] = book

type(bible)

for line in lines:
    