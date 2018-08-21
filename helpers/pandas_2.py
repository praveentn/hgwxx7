# pandas merge

df1
  skuid    brand
0  ax12     sony
1  ak22     nike
2  ak22     levi
3  zm23  addidas
4  zm23  ferrari
5  zm24      NaN

df2
    sid    brand
0  ax11     sony
1  ax12     nike
2  ax12     levi
3  zm23  addidas
4  zm23  ferrari
5  zm23      NaN

df1.merge(df2, how='left')
  skuid    brand   sid
0  ax12     sony  ax11
1  ak22     nike  ax12
2  ak22     levi  ax12
3  zm23  addidas  zm23
4  zm23  ferrari  zm23
5  zm24      NaN  zm23

df1.merge(df2, how='right')
  skuid    brand   sid
0  ax12     sony  ax11
1  ak22     nike  ax12
2  ak22     levi  ax12
3  zm23  addidas  zm23
4  zm23  ferrari  zm23
5  zm24      NaN  zm23


df1.merge(df2, left_on=['brand'], right_on=['brand'])


df1.merge(df2, left_on=['skuid'], right_on=['sid'])


df1.merge(df2, left_on=['skuid', 'brand'], right_on=['sid', 'brand'])


