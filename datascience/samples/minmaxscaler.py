from sklearn.preprocessing import StandardScaler, MinMaxScaler

# scale col1 and col2
vals = df[['col1', 'col2']].values #returns a numpy array

min_max_scaler = MinMaxScaler()
vals_scaled = min_max_scaler.fit_transform(vals)

# scaled
df_scaled = pd.DataFrame(vals_scaled, columns=['scaled_col1', 'scaled_col2'])
