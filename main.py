from product_service import *
import pandas as pd

bananas = pd.Series(find_by_name('banan'))

print bananas[2]

 type(bananas)