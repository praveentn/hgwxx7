# plot value counts of a column
def plot_value_counts(df, col, condition=False):
    """Plot value counts of a column, optionally with only the heads of a household"""
    # apply condition here if required
    if condition:
        # define condition below <>
        df = df.loc[df[col] == condition].copy()
        
    plt.figure(figsize = (8, 6))
    df[col].value_counts().sort_index().plot.bar(color = 'red',
                                                 edgecolor = 'g',
                                                 linewidth = 2)
    plt.xlabel(f'{col}')
    plt.title(f'{col} Value Counts')
    plt.ylabel('Count')
    plt.show()

# plot
plot_value_counts(df, col)
plot_value_counts(df, col, condition=True)
