alpha: dict[str, str] = {
    "ai": "ABCDEFGHI",
    "jr": "JKLMNOPQR",
    "s!": "STUVWXYZ!"
}

a = alpha
AI = "ai"
SZ = "s!"

print(f"#{a[AI][7]}{a[AI][0]}{a[AI][6]}{a[SZ][0]}")