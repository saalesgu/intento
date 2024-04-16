import pandas as pd

def drop_columns_spotify(df):
    df = df.drop(['Unnamed: 0'], axis=1)
    return df

def drop_track_id(df):
    df = df[df['track_id'] != '1kR4gIb7nGxHPI3D2ifs59']
    return df

def drop_duplicate_rows(df):
    df.drop_duplicates(inplace=True)
    return df

def assign_popularity_levels(df):
    interval_values = [0, 20, 40, 60, 80, 101]
    level_names = ['Very Low', 'Low', 'Medium', 'High', 'Very High']

    df['popularity_level'] = pd.cut(df['popularity'], bins=interval_values, labels=level_names, right=False)
    return df

def convert_duration(df):
    df['duration_min_sec'] = pd.to_datetime(df['duration_ms'], unit='ms').dt.strftime('%M:%S')
    return df

def categorize_danceability(df):
    percentiles = [0, 0.25, 0.5, 0.75, 1.0]
    labels = ['Very Low', 'Low', 'Medium', 'High']

    df['danceability_category'] = pd.cut(df['danceability'], bins=percentiles, labels=labels, right=False)
    return df

def categorize_speechiness(df):
    speechiness_bins = [0, 0.33, 0.66, 1.0]
    speechiness_labels = ['Music Only', 'Music and Speech', 'Speech Only']

    df['speechiness_category'] = pd.cut(df['speechiness'], bins=speechiness_bins, labels=speechiness_labels, right=False)
    return df

def assign_valence_categories(df):
    valence_bins = [0, 0.25, 0.5, 0.75, 1.0]
    valence_labels = ['Sad', 'Neutral', 'Happy', 'Euphoric']

    df['valence_category'] = pd.cut(df['valence'], bins=valence_bins, labels=valence_labels, right=False)

    return df

def assign_genre_categories(df):

    genre_mapping = {
        'instrumental': ['acoustic', 'classical', 'folk', 'guitar', 'piano', 'singer-songwriter', 'songwriter', 'world-music', 'opera', 'new-age'],
        'electronic': ['afrobeat', 'breakbeat', 'chicago-house', 'club', 'dance', 'deep-house', 'detroit-techno', 'dub', 'dubstep', 'edm', 'electro', 'electronic', 'house', 'idm', 'techno', 'minimal-techno', 'trance', 'hardstyle'],
        'rock and metal': ['alt-rock', 'alternative', 'british', 'grunge', 'hard-rock', 'indie', 'metal', 'metalcore', 'punk-rock', 'rock', 'rock-n-roll', 'black-metal', 'death-metal', 'hardcore', 'heavy-metal', 'industrial', 'psych-rock', 'rockabilly', 'goth', 'punk', 'j-rock', 'garage'],
        'pop': ['anime', 'cantopop', 'j-pop', 'k-pop', 'pop', 'power-pop', 'synth-pop', 'indie-pop', 'pop-film'],
        'urban': ['hip-hop', 'j-dance', 'j-idol', 'r-n-b', 'trip-hop'],
        'latino': ['brazil', 'latin', 'latino', 'reggaeton', 'salsa', 'samba', 'spanish', 'pagode', 'sertanejo', 'mpb'],
        'global sounds': ['indian', 'iranian', 'malay', 'mandopop', 'reggae', 'turkish', 'ska', 'dancehall', 'tango'],
        'jazz and soul': ['blues', 'bluegrass', 'funk', 'gospel', 'jazz', 'soul'],
        'varied themes': ['children', 'disney', 'forro', 'grindcore', 'kids', 'party', 'romance', 'show-tunes'],
        'mood': ['ambient', 'chill', 'happy', 'sad', 'sleep', 'study',  'comedy'],
        'single genre': ['country', 'progressive-house', 'swedish', 'emo', 'honky-tonk', 'french', 'german', 'drum-and-bass', 'groove', 'disco']
    }

    genre_to_category = {genre: category for category, genres in genre_mapping.items() for genre in genres}
    df['genre'] = df['track_genre'].map(genre_to_category)
    return df

def drop_columns_unnecessary(df):
    df = df.drop(['duration_ms', 'danceability', 'energy', 'key', 'mode', 'loudness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature'], axis=1)
    return df

def fill_null_values(df , columns, word) -> None:
    df[columns] = df[columns].fillna(word)