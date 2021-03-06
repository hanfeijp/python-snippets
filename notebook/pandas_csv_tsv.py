import pandas as pd

df = pd.read_csv('data/src/sample.csv')
print(df)
#    11  12  13  14
# 0  21  22  23  24
# 1  31  32  33  34

print(df.columns)
# Index(['11', '12', '13', '14'], dtype='object')

df_none = pd.read_csv('data/src/sample.csv', header=None)
print(df_none)
#     0   1   2   3
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_names = pd.read_csv('data/src/sample.csv', names=('A', 'B', 'C', 'D'))
print(df_names)
#     A   B   C   D
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_header = pd.read_csv('data/src/sample_header.csv')
print(df_header)
#     a   b   c   d
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_header_0 = pd.read_csv('data/src/sample_header.csv', header=0)
print(df_header_0)
#     a   b   c   d
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_header_2 = pd.read_csv('data/src/sample_header.csv', header=2)
print(df_header_2)
#    21  22  23  24
# 0  31  32  33  34

df_header_index = pd.read_csv('data/src/sample_header_index.csv')
print(df_header_index)
#   Unnamed: 0   a   b   c   d
# 0        ONE  11  12  13  14
# 1        TWO  21  22  23  24
# 2      THREE  31  32  33  34

print(df_header_index.index)
# RangeIndex(start=0, stop=3, step=1)

df_header_index_col = pd.read_csv('data/src/sample_header_index.csv', index_col=0)
print(df_header_index_col)
#         a   b   c   d
# ONE    11  12  13  14
# TWO    21  22  23  24
# THREE  31  32  33  34

print(df_header_index_col.index)
# Index(['ONE', 'TWO', 'THREE'], dtype='object')

df_none_usecols = pd.read_csv('data/src/sample.csv', header=None, usecols=[1, 3])
print(df_none_usecols)
#     1   3
# 0  12  14
# 1  22  24
# 2  32  34

df_none_usecols = pd.read_csv('data/src/sample.csv', header=None, usecols=[2])
print(df_none_usecols)
#     2
# 0  13
# 1  23
# 2  33

df_header_usecols = pd.read_csv('data/src/sample_header.csv', usecols=['a', 'c'])
print(df_header_usecols)
#     a   c
# 0  11  13
# 1  21  23
# 2  31  33

df_header_usecols = pd.read_csv('data/src/sample_header.csv', usecols=lambda x:x is not 'b')
print(df_header_usecols)
#     a   c   d
# 0  11  13  14
# 1  21  23  24
# 2  31  33  34

df_header_usecols = pd.read_csv('data/src/sample_header.csv', usecols=lambda x:x not in ['a', 'c'])
print(df_header_usecols)
#     b   d
# 0  12  14
# 1  22  24
# 2  32  34

df_index_usecols = pd.read_csv('data/src/sample_header_index.csv', index_col=0, usecols=[0, 1, 3])
print(df_index_usecols)
#         a   c
# ONE    11  13
# TWO    21  23
# THREE  31  33

df_none = pd.read_csv('data/src/sample.csv', header=None)
print(df_none)
#     0   1   2   3
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_none = pd.read_csv('data/src/sample.csv', header=None, skiprows=2)
print(df_none)
#     0   1   2   3
# 0  31  32  33  34

df_none_skiprows = pd.read_csv('data/src/sample.csv', header=None, skiprows=[0, 2])
print(df_none_skiprows)
#     0   1   2   3
# 0  21  22  23  24

df_none_skiprows = pd.read_csv('data/src/sample.csv', header=None, skiprows=[1])
print(df_none_skiprows)
#     0   1   2   3
# 0  11  12  13  14
# 1  31  32  33  34

df_none_skiprows = pd.read_csv('data/src/sample.csv', header=None, skiprows=lambda x:x not in [0, 2])
print(df_none_skiprows)
#     0   1   2   3
# 0  11  12  13  14
# 1  31  32  33  34

df_header_skiprows = pd.read_csv('data/src/sample_header.csv', skiprows=[1])
print(df_header_skiprows)
#     a   b   c   d
# 0  21  22  23  24
# 1  31  32  33  34

df_header_skiprows = pd.read_csv('data/src/sample_header.csv', skiprows=[0, 3])
print(df_header_skiprows)
#    11  12  13  14
# 0  21  22  23  24

df_none_skipfooter = pd.read_csv('data/src/sample.csv', header=None, skipfooter=1, engine='python')
print(df_none_skipfooter)
#     0   1   2   3
# 0  11  12  13  14
# 1  21  22  23  24

df_none_nrows = pd.read_csv('data/src/sample.csv', header=None, nrows=2)
print(df_none_nrows)
#     0   1   2   3
# 0  11  12  13  14
# 1  21  22  23  24

df_tsv = pd.read_table('data/src/sample_header_index.tsv', index_col=0)
print(df_tsv)
#         a   b   c   d
# ONE    11  12  13  14
# TWO    21  22  23  24
# THREE  31  32  33  34

df_tsv_sep = pd.read_csv('data/src/sample_header_index.tsv', index_col=0, sep='\t')
print(df_tsv_sep)
#         a   b   c   d
# ONE    11  12  13  14
# TWO    21  22  23  24
# THREE  31  32  33  34
