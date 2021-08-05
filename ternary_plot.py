#!/usr/bin/env python
# -*- coding: utf-8 -*-
# plot some ternary plots
# Author: Antoine Triantafyllou 2015-05


import matplotlib.pyplot as plt
import pandas as pd
from math import *


def ternary_plot(df_in, abc_headers, norm='no', corner_labels=['A', 'B', 'C'], title='Ternary plot', ticks='grey'):
    """fix some layout of the ternary plot"""
    """df_in is the imported dataframe, abc_headers are columns names in df, norm = if you need these data to be normalized before plotting, then some plotting customization"""
    fig = plt.figure(figsize=(15, 11), dpi=70)
    fig.suptitle(str(title), fontsize=30)
    fig.subplots_adjust(top=0.93)

    # triangle reperes
    plt.plot([0, 100], [0, 0], 'k-', lw=1)
    plt.plot([0, 50], [0, 100*sin(radians(60))], 'k-', lw=1)
    plt.plot([50, 100], [100*sin(radians(60)), 0], 'k-', lw=1)

    if ticks:
        for i in range(10, 91, 10):
            # A ticks
            plt.plot([i/2, 100-(i/2)], [i*sin(radians(60)), i*sin(radians(60))], color=str(ticks), lw=0.4)
            # C ticks
            plt.plot([100-i, 100-(i/2)], [0, i*sin(radians(60))], color=str(ticks), lw=0.3)
            # B ticks
            plt.plot([i, i/2], [0, i*sin(radians(60))], color=str(ticks), lw=0.3)

    else:
        pass

    plt.text(50, 100*sin(radians(60))+1, str(corner_labels[1]), fontsize=20, ha='center')
    plt.text(-6, -5, '        ' + str(corner_labels[0]), fontsize=20, ha='center')
    plt.text(101, -5, '  '+str(corner_labels[2]), fontsize=20, ha='center')

    ax = fig.add_subplot(111)
    ax.patch.set_facecolor('white')
    ax.plot(0, 0, 'k')
    ax.plot(100, 0, 'k')
    ax.plot(50, 100*sin(radians(60)), 'k')

    plt.ylim([-7, 93])
    plt.xlim([-15, 115])
    ax.axes.get_yaxis().set_visible(False)
    ax.axes.get_xaxis().set_visible(False)

    A_head, B_head, C_head = abc_headers
    if norm == 'no':
        df_in['new_A'] = 100*df_in[A_head]/(df_in[A_head]+df_in[B_head]+df_in[C_head])
        df_in['new_B'] = 100 * df_in[B_head] / (df_in[A_head] + df_in[B_head] + df_in[C_head])
        df_in['new_C'] = 100 * df_in[C_head] / (df_in[A_head] + df_in[B_head] + df_in[C_head])
    else:
        df_in['new_A'] = df_in[A_head]
        df_in['new_B'] = df_in[B_head]
        df_in['new_C'] = df_in[C_head]
    abc_headers = ['A', 'F', 'M']

    s = ax.scatter(y=df_in['new_B'] * sin(radians(60)), x=df_in['new_C'] + (df_in['new_B'] * tan(radians(26.75))), marker='D', color='red', s=160,
                   linewidths=0.3)  # , vmin=0, vmax=1
    plt.show()


if __name__ == '__main__':
    #add your file directory and import your datatable as a pandas df
    file_in = r'C:\Users\Utilisateur\PycharmProjects\ternary\data_example.xlsx'
    df_in = pd.read_excel(file_in, sheet_name='Sheet1')

    # call the function ternary-plot
    ternary_plot(df_in, abc_headers=['cr', 'fe3', 'al'], norm='no', corner_labels=['Cr', 'Fe3+', 'Al'], title='Ternary plot', ticks='grey')


