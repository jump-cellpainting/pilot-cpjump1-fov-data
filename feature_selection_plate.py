import pandas as pd
from pycytominer import feature_select

feature_select_operations = ['variance_threshold',
                             'correlation_threshold',
                             'drop_na_columns',
                             'blocklist']

batches = ['2020_11_04_CPJUMP1_1a', '2020_11_04_CPJUMP1_1b', '2020_11_04_CPJUMP1_1c',
           '2020_11_04_CPJUMP1_2a', '2020_11_04_CPJUMP1_2b', '2020_11_04_CPJUMP1_2c',
           '2020_11_04_CPJUMP1_3a', '2020_11_04_CPJUMP1_3b', '2020_11_04_CPJUMP1_3c',
           '2020_11_04_CPJUMP1_4a', '2020_11_04_CPJUMP1_4b', '2020_11_04_CPJUMP1_4c',
           '2020_11_04_CPJUMP1_5a', '2020_11_04_CPJUMP1_5b', '2020_11_04_CPJUMP1_5c',
           '2020_11_04_CPJUMP1_6a', '2020_11_04_CPJUMP1_6b', '2020_11_04_CPJUMP1_6c',
           '2020_11_04_CPJUMP1_7a', '2020_11_04_CPJUMP1_7b', '2020_11_04_CPJUMP1_7c',
           '2020_11_04_CPJUMP1_8a', '2020_11_04_CPJUMP1_8b', '2020_11_04_CPJUMP1_8c',
           '2020_11_04_CPJUMP1_9a', '2020_11_04_CPJUMP1_9b', '2020_11_04_CPJUMP1_9c',
           '2020_11_04_CPJUMP1_10a', '2020_11_04_CPJUMP1_10b', '2020_11_04_CPJUMP1_10c',
           '2020_11_04_CPJUMP1_11a', '2020_11_04_CPJUMP1_11b', '2020_11_04_CPJUMP1_11c',
           '2020_11_04_CPJUMP1_12a', '2020_11_04_CPJUMP1_12b', '2020_11_04_CPJUMP1_12c',
           '2020_11_04_CPJUMP1_13a', '2020_11_04_CPJUMP1_13b', '2020_11_04_CPJUMP1_13c',
           '2020_11_04_CPJUMP1_14a', '2020_11_04_CPJUMP1_14b', '2020_11_04_CPJUMP1_14c',
           '2020_11_04_CPJUMP1_15a', '2020_11_04_CPJUMP1_15b', '2020_11_04_CPJUMP1_15c',
           '2020_11_04_CPJUMP1_16']

plates = ['BR00117015',
          'BR00117016',
          'BR00117017',
          'BR00117019']

float_format = "%.5g"

all_plates_df = pd.DataFrame()

for batch in batches:
    for plate in plates:
        df = (
            pd.read_csv(f'profiles/{batch}/{plate}/{plate}_normalized_negcon.csv.gz')
        )

        fs_df = feature_select(profiles=df,
                               features="infer",
                               operation=feature_select_operations,
                               float_format=float_format)

        fs_df.to_csv(f'profiles/{batch}/{plate}/{plate}_normalized_feature_select_plate_negcon.csv.gz', index=False)
