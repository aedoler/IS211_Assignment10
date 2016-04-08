CREATE TABLE artists (
	artist_id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE albums (
	album_id INTEGER PRIMARY KEY,
    album_name TEXT,
    artist_id TEXT
);

CREATE TABLE songs (
	song_name text,
    album_id INTEGER,
    song_track INTEGER,
    song_len INTEGER
);