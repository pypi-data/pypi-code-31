import pandas as pd
import numpy as np
import re
import os

from .reader import read_sample_info

cov_cols = ['Target', 'min_coverage', 'sum_coverage', 'basepairs', 'cov_per_bp', 'fraction_zero_coverage', 'fraction_10x_coverage', 'fraction_30x_coverage']
cov_cols_dtypes = dict(zip(cov_cols, [str, int, int, int, float, float]))

def fraction_zero_coverage(coverage):
    """Calculate fraction of bases with coverage 0."""
    return 1.0 * (coverage == 0).sum() / len(coverage)

def fraction_10x_coverage(coverage):
    """Calculate fraction of bases with coverage 10 or more."""
    return 1.0 * (coverage >= 10).sum() / len(coverage)

def fraction_30x_coverage(coverage):
    """Calculate fraction of bases with coverage 30 or more."""
    return 1.0 * (coverage >= 30).sum() / len(coverage)

def process_file(input: str, output: str):
    """Read raw bedtools coverage file, calculate summary statistics and output them as CSV file.

    Args:
        input: path to a bedtools coverage file
        output: path to the summary CSV file
    """

    #read bedtools output
    depth = pd.read_csv(input, sep='\t', names = ['chr', 'start_0', 'end', 'id', 'score', 'strand', 'position', 'coverage'], low_memory=False)

    #summarize
    summary = depth.groupby('id').aggregate({'coverage': [np.min, np.sum, len, np.mean, fraction_zero_coverage, fraction_10x_coverage, fraction_30x_coverage]})

    #make id index into normal column, then reset column names
    summary.reset_index(level=0, inplace=True)
    summary.columns = cov_cols

    #write file
    summary.to_csv(output, index = False)

def aggregate(input, output):
    """Read coverage summary files and create aggregate files.

    Args:
        input: dict containing 'csvs', the list of csvs fils to aggregate, and optionally 'sample_info', a table with additional sample annotation
        output: dict containing paths for output files: merged, min_coverage, cov_per_bp, fraction_zero_coverage
    """
    #load sample information table
    sample_info = None
    if 'sample_info' in input and len(input['sample_info']) > 0:
        sample_info = read_sample_info(input['sample_info'][0])

    merged = None
    for file in input['csvs']:
        sname = os.path.basename(file)            
        sname = re.sub(r'\.coverage\.csv$', '', sname)

        print('Reading', file, 'for', sname, '...')
        df = pd.read_csv(file,
            index_col = False,
            dtype = cov_cols_dtypes)
        df['Sample'] = sname
        print(sname, 'coverage data shape:', str(df.shape))

        if merged is None:
            merged = df
        else:
            merged = merged.append(df, ignore_index = True)

    assert merged is not None, \
        '\n\nABORTED: Did not find any coverage data!\n\n'
            
    print('Merged data shape:', str(merged.shape))
    print(merged.head())

    print('Duplicated:')
    print(merged[merged.duplicated(['Target', 'Sample'], keep=False)])

    if sample_info is not None:
        merged = merged.join(sample_info, on = ['Sample', 'Target'], how = 'left')

    #make matrices
    for column in ['min_coverage', 'cov_per_bp', 'fraction_zero_coverage']:
        pivoted = merged.pivot(index='Target', columns='Sample', values=column)
        print('Made pivot table for', column, ' with shape', str(pivoted.shape))
        pivoted.to_csv(output[column])
        print(output[column])

    #output full merged data set
    merged.to_csv(output['merged'], index = False)