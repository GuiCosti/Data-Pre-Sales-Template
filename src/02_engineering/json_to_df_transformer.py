import os
import json
import pandas as pd

FILE_PATH = '../data/json_data.json'
ITEM_LIST_COLUMN = 'ItemList'
INDEX_COLUMN = 'NFeID'


# Reads a json file and returns the data
def read_json(file_path=FILE_PATH):
    if not os.path.exists(file_path):
        raise Exception(F"The file at {file_path} doesn't exists.")
    else:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data


# Transform a json into a dataframe
def transform_json_into_df(data):
    return pd.DataFrame(data)


# Transform nested json objects into dataframe
def transform_nested_json_into_df(df, data_column, index_column):
    df_list = []
    for index, row in df.iterrows():
        nested_df = pd.DataFrame(row[data_column])
        nested_df[index_column] = row[index_column]
        df_list.append(nested_df)
    concated_df = pd.concat(df_list, axis=0).reset_index(drop=True)
    return concated_df


# Expand item list in the same dataframe
def expand_item_list(df, item_df, item_list_col, index_col):
    exploded_df = df.explode(item_list_col).drop(columns=[item_list_col, index_col]).reset_index(drop=True)
    expanded_df = pd.concat([exploded_df, item_df], axis=1)
    return expanded_df


# Threat item list column
def threat_item_list_column(df, item_list_col=ITEM_LIST_COLUMN, index_col=INDEX_COLUMN):
    item_df = transform_nested_json_into_df(df, item_list_col, index_col)
    expanded_df = expand_item_list(df, item_df, item_list_col, index_col)
    return (expanded_df, item_df)


# Apply business rules in the dataframe
def apply_business_rules(df):
    (expanded_df, item_df) = threat_item_list_column(df)
    return (expanded_df, item_df)


# Print the results dataframes
def show_results(df, item_df):
    print(df)
    print(item_df)


if __name__ == "__main__":
    data = read_json() # read json file
    df = transform_json_into_df(data) # transform json into a dataframe
    (df, item_df) = apply_business_rules(df) # apply business rules transformations on the loaded dataframe
    show_results(df, item_df) # print the results