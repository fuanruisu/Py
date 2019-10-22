from tabulate import tabulate

rios2 = {'Río': ['Almanzora', 
                 'Guadiaro', 
                 'Guadalhorce', 
                 'Guadalmedina'],
         'Long. (Km.)': [105,
                         79,
                         154,
                         51.5]}
        
print(tabulate(rios2, headers='keys', tablefmt='fancy_grid'))