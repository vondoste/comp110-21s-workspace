"""Examples of importing modules and global identifiers."""

# Import an entire module
from lessons import helpers

# Access names in that module following the dot
helpers.shout("this functionality was imported!")
print(helpers.THE_ANSWER)

# Alias a module
from lessons import helpers as hp
hp.whisper("THIS IS AN ALIAS OF HELPERS")

# Import names directly from a module
from lessons.helpers import shout, whisper
shout("imported this function!")
