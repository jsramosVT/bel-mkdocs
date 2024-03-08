## Original code by Amanda Sharp, Ph.D.
## Revised by Jay McDonald-Ramos (Feb 2024)

import matplotlib.pyplot as plt
import pandas as pd
from shapely import geometry, ops
# plt.switch_backend('agg')

# 2D INPUT FILES - Change to match your systems.
SYS1 = 'mut_wt_eigtraj.xvg'
SYS2 = 'wt_mut_eigtraj.xvg'

# GRAPH COLORS - Change to match your systems.
C1 = '#001b6b'
C2 = '#965102'
C3 = '#04464a'
C4 = '#5c0b00'

# TITLE AND FILE PARAMETERS - Change graph title and file name.
FILENAME = 'filename'  # Name of file output.
TITLE = r'GRAPH TITLE' # Raw string - can use Mathtext and LaTeX in graph title.
# Example of Mathtext/LaTeX typesetting. Use this in TITLE to check it out :)
    # r'$\mathbfit{Ab}$$\mathbf{CeeD}$$\mathbf{_{WT}}$ projected onto $\mathbfit{Ab}$$\mathbf{CeeD}$$\mathbf{_{Mut}}$' 

def gather_data():
    # FIRST .xvg created by -2d flag of gmx anaeig.
    df1 = pd.read_csv(SYS1, delim_whitespace=True, header=16, usecols=[0,1])
    df1.columns = ['x', 'y']
    
    data1 = df1.values.tolist()

    # SECOND .xvg created by -2d flag of gmx anaeig.
    df2 = pd.read_csv(SYS2, delim_whitespace=True, header=16, usecols=[0,1])
    df2.columns = ['x', 'y']
 
    fig, (ax, ax2) = plt.subplots(1,2, figsize=(10,5))

    # Parameters for 1st graph.
    ax.scatter(df2['x'], df2['y'],c=C1, edgecolor='black')
    ax.scatter(df1['x'], df1['y'],c=C2, edgecolor='black')
    ax.set_xlabel('Projection on Eigenvector 1 (nm)', weight="bold", fontsize=14)
    ax.set_ylabel('Projection on Eigenvector 2 (nm)', weight="bold", fontsize=14)

    # Parameters for 2nd graph. Note the order of dataframes has changed.
    ax2.scatter(df1['x'], df1['y'],c=C2, edgecolor='black')
    ax2.scatter(df2['x'], df2['y'],c=C1, edgecolor='black')
    ax2.set_xlabel('Projection on Eigenvector 1 (nm)', weight="bold", fontsize=14)
    ax2.set_ylabel('Projection on Eigenvector 2 (nm)', weight="bold", fontsize=14)

    ax.tick_params(axis='x', labelsize=12)
    ax2.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y',labelsize=12)
    ax2.tick_params(axis='y', labelsize=12)
    plt.minorticks_on()

    graph_title = TITLE 
    fig.suptitle(graph_title, weight="bold", fontsize=18)
    plt.yticks(fontsize=12)
    plt.xticks(fontsize=12)  
    plt.tight_layout()
    # plt.show()
    plt.savefig(FILENAME + '.png') # Can also be .pdf, .svg, etc.

    ## OUTPUT will be two side-by-side graphs with a single title. ##


if __name__ == '__main__':
    gather_data()