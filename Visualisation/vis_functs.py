import plotly.graph_objs as go
import plotly.offline as py
import plotly.tools as tools
# py.init_notebook_mode()


def df_calc_stat(df, chosen_stat='mean', quant_val=0.5):
    if chosen_stat in df.describe().index:
        return df.describe().loc[chosen_stat, :]

    else:
        raise Exception('statistic not defined')



def plotly_feats_stat_comp(labels=None, row_num=None, df_range=None,
                           chosen_stat='mean', title=None, filename='make-subplots-multiple-with-titles'):

    """
    The chosen_stat should be any of: the statistics provided by pandas descibe() method:
    'count', 'mean', 'std', 'min', '25%', '50%', '75%','max'
    """

    df_dict = {}
    for i in range(len(df_range)):
        df_dict.update(
            {i: df_calc_stat(df_range[i], chosen_stat=chosen_stat)}
        )

    fig = tools.make_subplots(
        rows=row_num,
        cols=2,
        subplot_titles=tuple(df_range[0].keys())
    )

    col_count = 1
    row_coord = 1

    for i, key in enumerate(df_dict[i].keys()):
        trace0 = go.Bar(x=labels, y=[df_dict[i].loc[key] for i in df_dict])

        # Define coordinates and update figure
        if col_count % 2 != 0:
            col_coord = 1
        else:
            col_coord = 2

        fig.append_trace(trace0, row_coord, col_coord)
        col_count += 1

        if i % 2 != 0:
            row_coord += 1

    fig['layout'].update(height=600, width=1200, title=title + ' {}'.format(chosen_stat))

    py.iplot(fig, filename=filename)
