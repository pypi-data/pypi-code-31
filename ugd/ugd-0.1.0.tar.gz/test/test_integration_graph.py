import numpy as np
from ugd import graph_hyp_test

from test.test_resources.plain_graph_integration import adj_m_1, var_dict_1, adj_m_2, var_dict_2



def test_graph_no_rstrc():
    graphs, stats_list = graph_hyp_test(adj_m=adj_m_1, var_dict=var_dict_1, test_variable=('gender', 'm', 'f'), mixing_time=100, anz_sim=100, show_polt=False)
    mue = np.mean(stats_list)
    true_mean = 0*1/3+ 2/3 * 2
    assert mue > true_mean - 0.15 and mue < true_mean + 0.15

