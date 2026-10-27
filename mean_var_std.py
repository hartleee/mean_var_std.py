import numpy as np

def calculate(list):

    # if not 9 elements, raise error
    if (len(list) < 9):
        raise ValueError("List must contain nine numbers.")
    
    else:
        # convert to numpy array and reshape
        nplist = np.reshape(list,(3,3))
        
        # create dictionary (instantiate empty list so .append works)
        keys = ['mean','variance','standard deviation', 'max', 'min', 'sum']
        calculations = {key: [] for key in keys}

        # ADD TO DICTIONARY

        # means
        calculations['mean'].append(nplist.mean(axis=0).tolist())
        calculations['mean'].append(nplist.mean(axis=1).tolist())
        calculations['mean'].append(nplist.mean().tolist())

        # variance
        calculations['variance'].append(nplist.var(axis=0).tolist())
        calculations['variance'].append(nplist.var(axis=1).tolist())
        calculations['variance'].append(nplist.var().tolist())

        # std deviation
        calculations['standard deviation'].append(nplist.std(axis=0).tolist())
        calculations['standard deviation'].append(nplist.std(axis=1).tolist())
        calculations['standard deviation'].append(nplist.std().tolist())

        # max
        calculations['max'].append(nplist.max(axis=0).tolist())
        calculations['max'].append(nplist.max(axis=1).tolist())
        calculations['max'].append(nplist.max().tolist())

        # min
        calculations['min'].append(nplist.min(axis=0).tolist())
        calculations['min'].append(nplist.min(axis=1).tolist())
        calculations['min'].append(nplist.min().tolist())

        # sum
        calculations['sum'].append(nplist.sum(axis=0).tolist())
        calculations['sum'].append(nplist.sum(axis=1).tolist())
        calculations['sum'].append(nplist.sum().tolist())
        
    return calculations
