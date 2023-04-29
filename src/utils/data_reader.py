import pandas as pd
from config import RECOLTABLE_MAP_POSITIONS_FILE_PATH

def read_recoltable_map_positions(recoltable_name: str) -> pd.DataFrame:
    """
    Reads the map positions where at least 2 blocs of a recoltable are present.    

    PARAMETERS
    ----------
    recoltable_name: str
        A recoltable name (such as: wheats, oats, etc.)
    
    Returns
    -------
    pd.DataFrame
        A dataframe of a recoltable map positions and quantities per position. (The saved result of "web_scraper.py")
    """
    filepath = RECOLTABLE_MAP_POSITIONS_FILE_PATH(recoltable_name)
    df = pd.read_csv(filepath)
    df = df[df.quantite>=2].reset_index(drop=True)
    return df


    