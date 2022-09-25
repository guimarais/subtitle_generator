"""
Function to convert miliseconds into a string format usable in srt subtitle files
"""
import numpy as np


def convert_millis_srt(millis):
    """
    Time conversion function for srt format.
    Converts miliseconds to a string in hh:mm:ss,mmm format
    
    Parameters
    ------------
    millis: int, float
        A number of milliseconds
    
    Returns
    ------------
    stringout: str
        A string in hh:mm:ss,SSS format
    """
    hours = np.floor((millis/(1000*60*60)))
    millis = millis - hours*1000*60*60
    
    minutes = np.floor((millis/(1000*60)))
    millis = millis - minutes*1000*60
    
    seconds = np.floor((millis/1000))
    millis = millis - seconds*1000
    
    stringout = f"{hours:02g}:{minutes:02g}:{seconds:02g},{millis:03g}"
    
    return stringout