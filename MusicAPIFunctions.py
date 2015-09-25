def readJsonUrl(url):
    """This reads the contents of a URL.  Works for json data and Python 3"""
    #####################################################################
    # In this block of code:
    # - Python opens the url
    # - reads the data
    # - stores it as a string
    # - closes the url
    import urllib.request
    try:
        page = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print("There was an error opening the URL (description below).")
        print(e)
        print("Ask for help?")
        return(None)
    data_bytes = page.read()
    data_str = data_bytes.decode('utf-8')
    page.close()
    #####################################################################
    # In this block of code
    # - The json string is converted to a Python dictionary.
    # - This is returned
    import json
    try:
        output = json.loads(data_str)
    except:
        print("Error")
        return(None)
    return(output)    
    #####################################################################

def checkSpotifyPopularity(artist):
    """ Function to check Spotify popularity rating of artist."""
    # The code:
    # - Replaces spaces in artist by %20 (which means space in urls)
    # - Defines URL which makes request for rating
    # - Uses function readJsonUrl to read url
    # - If lyrics found returns them (as a string)
    A = artist.replace(" ", "%20")
    url = "https://api.spotify.com/v1/search?q=%s&type=artist&limit=1"%(A)
    output = readJsonUrl(url)
    return( output["artists"]["items"][0]["popularity"] )

def printRadioOnePlaylist(Letter):
    """ Function to fetch this weeks Radio 1 playlists."""
    # The code:
    # - Defines URL where playlist is stored
    # - Uses function readJsonUrl to read url
    # - Extracts the playlist requested by user
    # - prints it
    myURL = "http://www.bbc.co.uk/radio1/playlist.json"
    output = readJsonUrl(myURL)
    playlist = output["playlist"]
    plB = playlist["b"]
    plC = playlist["c"]
    plI = playlist["introducing"]
    if Letter=="A":
        pl = playlist["a"]
    elif Letter=="B":
        pl = playlist["b"]
    elif Letter=="C":
        pl = playlist["c"]
    elif Letter=="I":
        pl = playlist["introducing"]
    else:
        error("The input to fetchRadioOnePlaylist should be either 'A', 'B', 'C' or 'I'")
    print("-"*50)
    print("Radio 1 Playlist " + Letter)
    print("-"*50)
    for s in pl:
        print( s["artist"] + ": " + s["title"] )

