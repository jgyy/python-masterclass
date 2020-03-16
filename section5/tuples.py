"""
Ordered Sets with Tuples
"""
WELCOME = "Welcome to my Nightmare", "Alice Cooper", 1975
BAD = "Bad Company", "Bad Company", 1974
BUDGIE = "Nightflight", "Budgie", 1981
IMELDA = "More Mayhem", "Emilda May", 2011, \
         ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Walts"))

print(IMELDA)

TITLE, ARTIST, YEAR, TRACKS = IMELDA
print(TITLE)
print(ARTIST)
print(YEAR)
for song in TRACKS:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))

C = 12
print(C)
A, B = 12, 13
print(A, B)

A, B = B, A
print("a is {}".format(A))
print("b is {}".format(B))
