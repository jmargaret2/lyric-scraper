import requests, re, lyricsgenius
from bs4 import BeautifulSoup


# Get artist object from API
def request_artist_info(artist_name, page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response


# Get Genius.com song url from artist object
def request_song(artistname, song_cap):
    page = 1
    songs = []

    while True:
        response = request_artist_info(artistname, page)
        json = response.json()

        # Collect up to song_cap song objects from artist
        song_info = []
        for hit in json['response']['hits']:
            if artistname.lower() in hit['result']['primary_artist']['name'].lower():
                song_info.append(hit)

        # Collect song's URL from song objects
        for song in song_info:
            if len(songs) < song_cap:
                url = song['result']['url']
                songs.append(url)
        if len(songs) == song_cap:
            break
        else:
            page += 1

    print("Found {} songs by {}".format(len(songs), artistname))
    return songs


# Scrape lyrics from a Genius.com song URL
def scrape_song_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser")
    lyrics = html.find("div", class_="lyrics").get_text()

    # Remove identifies like "Chorus" "Verse" etc.
    lyrics = re.sub(r'[(\[].*?[)\]]', '', lyrics)

    # Remove empty lines
    # lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])
    return lyrics


# Loop through all URL's and write lyrics to one file
def write_lyrics_to_file(artistname, songcount):
    file = open('lyrics/' + artistname.lower() + '.txt', 'wb')
    urls = request_song(artistname, songcount)

    for url in urls:
        lyrics = scrape_song_lyrics(url)
        file.write(lyrics.encode("utf8"))

    file.close()
    number_of_lines = sum(1 for line in open("lyrics/" + artistname.lower() + ".txt", "rb"))
    print("Wrote {} lines to file from {} songs".format(number_of_lines, songcount))


if __name__ == '__main__':
    artist = input("Enter the artist: ")
    songs = int(input("Enter the number of songs: "))
    write_lyrics_to_file(artist, songs)
