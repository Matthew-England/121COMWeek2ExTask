# In the separate Python file MusicAPIFunctions.py I have defined 2 functions.
# The next line allows those functions to be used in this script.

from MusicAPIFunctions import checkSpotifyPopularity, printRadioOnePlaylist

# The functions use information stored on the internet regarding music.
# We give examples of each

# 1.  checkSpotifyPopularity finds the current popularity rating for an artist on spotify.
# Example:
print("-"*50)
print("Example of checkSpotifyPopularity")
print("-"*50)
print( checkSpotifyPopularity("Royal Blood") )
print("")

# 2.  printRadioOnePlaylist prints the songs currently being played regularly on BBC Radio 1.
# There are 4 different playlists, indexed by letters A,B,C and I (for introducing).
# Example:
pl = printRadioOnePlaylist("A")




