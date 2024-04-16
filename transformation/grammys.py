import pandas as pd
import re

def process_data(df):
    patterns = [r'composer \((.*?)\)', 
                r'\(.*\)',
                r'songwriters? \((.*?)\)']

    def find_artist(workers):
        for pattern in patterns:
            matches = re.findall(pattern, workers)
            if matches:
                return matches[0] if matches[0] else None
        return None

    condition = df['artist'].isnull() & df['workers'].str.contains('|'.join(patterns))

    df.loc[condition, 'artist'] = df.loc[condition, 'workers'].apply(lambda x: find_artist(x) if isinstance(x, str) else None)
    df.loc[df['artist'].notnull() & df['workers'].isnull(), 'workers'] = df['artist']
    return df

def drop_rows(df):
    condition = df['workers'].isnull() & df['artist'].isnull()
    df = df[~condition]
    return df

def clean_artist(df):
    df['artist'] = df['artist'].str.replace(r'\((.*?)\)', r'\1', regex=True)
    return df

def rename_column(df):
    df.rename(columns={'winner': 'nominated'}, inplace=True)
    return df

def drop_columns(df):
    df = df.drop(['id','img', 'published_at', 'updated_at', 'workers', 'title'], axis=1)
    return df

def reemplazar_none_nan(df, valor_reemplazo):
    columnas_integer = df.select_dtypes(include=['int']).columns
    df[columnas_integer] = df[columnas_integer].fillna(valor_reemplazo)
    return df

def column_year(df, column_name):
    df[column_name] = df[column_name].astype(int)
    for index, value in df[column_name].items():
        if isinstance(value, int) and value % 10 == 0:
            df.at[index, column_name] = value // 10
    
    return df