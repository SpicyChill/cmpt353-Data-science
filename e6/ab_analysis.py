import pandas as pd
import numpy as np
import sys
from scipy import stats
OUTPUT_TEMPLATE = (
    '"Did more/less users use the search feature?" p-value: {more_users_p:.3g}\n'
    '"Did users search more/less?" p-value: {more_searches_p:.3g}\n'
    '"Did more/less instructors use the search feature?" p-value: {more_instr_p:.3g}\n'
    '"Did instructors search more/less?" p-value: {more_instr_searches_p:.3g}'
)


def main():
    filename = sys.argv[1]
    #filename = 'searches.json'
    data = pd.read_json(filename, orient='records', lines=True)
    data_odd = data.copy()
    data_odd = data_odd[data_odd['uid']%2!=0]
    search_0_odd = data_odd.copy()
    search_0_odd = search_0_odd[search_0_odd['search_count']==0]
    num_0_odd = len(search_0_odd)
    search_odd = data_odd.copy()
    search_odd = search_odd[search_odd['search_count']!=0]
    num_odd = len(search_odd)
    data_even = data.copy()
    data_even = data_even[data_even['uid']%2==0]
    search_0_even = data_even.copy()
    search_0_even = search_0_even[search_0_even['search_count']==0]
    num_0_even = len(search_0_even)
    search_even = data_even.copy()
    search_even = search_even[search_even['search_count']!=0]
    num_even = len(search_even)
    contingency = [[num_odd,num_0_odd], [num_even,num_0_even]]
    chi2, p, dof, expected = stats.chi2_contingency(contingency)
    v1 = p
    v2 = stats.mannwhitneyu(data_odd['search_count'], data_even['search_count']).pvalue

    data_new = data.copy()
    data_new = data_new[data_new['is_instructor']==True]
    data_odd2 = data_new.copy()
    data_odd2 = data_odd2[data_odd2['uid']%2!=0]
    search_0_odd2 = data_odd2.copy()
    search_0_odd2 = search_0_odd2[search_0_odd2['search_count']==0]
    num_0_odd2 = len(search_0_odd2)
    search_odd2 = data_odd2.copy()
    search_odd2 = search_odd2[search_odd2['search_count']!=0]
    num_odd2 = len(search_odd2)
    data_even2 = data_new.copy()
    data_even2 = data_even2[data_even2['uid']%2==0]
    search_0_even2 = data_even2.copy()
    search_0_even2 = search_0_even2[search_0_even2['search_count']==0]
    num_0_even2 = len(search_0_even2)
    search_even2 = data_even2.copy()
    search_even2 = search_even2[search_even2['search_count']!=0]
    num_even2 = len(search_even2)
    contingency2 = [[num_odd2,num_0_odd2], [num_even2,num_0_even2]]
    chi2, p, dof, expected = stats.chi2_contingency(contingency2)
    v3 = p
    v4 = stats.mannwhitneyu(data_odd2['search_count'], data_even2['search_count']).pvalue

    # Output
    print(OUTPUT_TEMPLATE.format(
        more_users_p=v1,
        more_searches_p=v2,
        more_instr_p=v3,
        more_instr_searches_p=v4,
    ))


if __name__ == '__main__':
    main()