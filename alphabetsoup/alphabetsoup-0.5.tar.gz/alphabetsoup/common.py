# -*- coding: utf-8 -*-
# imports
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# global variables
PROGRAM_NAME = 'alphabetsoup'
DUP_NAME = 'Dups'
SUBSTRING_NAME = 'Substr'
GRAPH_TYPES = [DUP_NAME, SUBSTRING_NAME]
AMBIG_NAME = 'Ambig%'
SHORT_NAME = 'Short'
FILESMALL_NAME = 'Small'
INT_TYPES = [SHORT_NAME, FILESMALL_NAME]
FLOAT_TYPES = [AMBIG_NAME]
NUMBER_TYPES = FLOAT_TYPES + INT_TYPES
STRING_TYPES = ['Name']
LENGTH_NAME = 'Length'
LOG_TYPES = [LENGTH_NAME]
STAT_TYPES = NUMBER_TYPES + LOG_TYPES
STAT_COLS = ['name',
             'seqs_in',
             'seqs_out',
             'residues',
             'n_ambig',
             'n_short',
             'n_small',
             'n_dups',
             'n_substr']
MIN_HIST_LEN = 50
PLOT_TYPES = ['png','svg']
LOG_DIR = 'log'
LOG_PATH = Path('.')/ LOG_DIR

def make_histogram(dist, name, log10=False):
    # do histogram plot with kernel density estimate
    mean = dist.mean()
    if log10:
        dist = np.log10(dist)
    sns.distplot(dist,
                 rug=True,
                 rug_kws={'color': 'b'},
                 kde_kws={'color': 'k',
                          'linewidth': 1,
                          'label': 'KDE'},
                 hist_kws={'histtype': 'step',
                           'linewidth': 2,
                           'alpha': 1,
                           'color': 'b'}
                 )
    plt.title('%s histogram of %d values, mean=%.1f'
              % (name, len(dist), mean))
    if log10:
        plt.xlabel('log ' + name)
    else:
        plt.xlabel(name)
    plt.ylabel('Frequency')
    for ext in PLOT_TYPES:
        plt.savefig(LOG_PATH / ('%s-histogram.' % (name.rstrip('%')) + ext),
                    bbox_inches='tight')
    plt.close('all')