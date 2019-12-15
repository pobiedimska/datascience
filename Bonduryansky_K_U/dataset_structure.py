import pandas as pd
info = {'cen-year':['2005', '2006', '2006'],
        'status':['Good', 'Good', 'Excellent'],
        'wire-prime':['No', 'No', 'No'],
        'zip-city':['Bronx', 'Jamaica', 'New York']
        }
tree_info = pd.DataFrame(info, index = ['1', '2', '3'])
