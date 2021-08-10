###
# define here functions to import various csv files you encounter.
# return the data as a pandas data frame
###
import pandas as pd
import numpy as np


#pd csv read function
def read_csv(file_path,col_name=None,header_line=None,delimiter=None):
    """Read a CSV file and return a DataFrame .

    Args:
        file_path ([type]): [description]
        col_name ([type], optional): [description]. Defaults to None.
        header_line ([type], optional): [description]. Defaults to None.
        delimiter ([type], optional): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """
    df=pd.read_csv(file_path,header=header_line,delimiter=delimiter)
    if col_name is not None:
        df.columns=col_name
    return df

def read_network_analyzer_csv(file,col_name=['f','re','im','na1']):
    """Read a net analyzer CSV file .

    Args:
        file ([type]): [description]
        col_name (list, optional): [description]. Defaults to ['f','re','im','na1'].

    Returns:
        [type]: [description]
    """
    data=read_csv(file,header_line=2,col_name=col_name,delimiter=',')
    return data