import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_grouped_barplot(df, config):
    """
    Plot a grouped barplot using the provided DataFrame and configuration.

    :param df: The DataFrame containing the data to be plotted.
    :type df: pandas.DataFrame
    :param config: A dictionary containing the configuration parameters for the plot.
    :type config: dict
    """
    x = config['x']
    y = config['y']
    hue = config['hue'] 
    hue_order = config.get('hue_order',df[hue].unique())    
    order = config.get('order',df[x].unique())
    palette = config.get('palette', 'dark')
    xlabel = config['xlabel']
    ylabel = config['ylabel']
    filepath = config.get('filepath', False)

    fig, ax = plt.subplots(1,1,figsize=[10,6])

    sns.barplot(data=df, 
                x=x, 
                y=y, 
                hue=hue, 
                hue_order=hue_order,
                ax=ax, 
                order=order, 
                palette=palette)
    ax.set_xlabel(xlabel, fontsize=18)
    ax.set_ylabel(ylabel, fontsize=18)
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=16)

    if filepath:
        fig.savefig(filepath)
    plt.show()

def plot_slope(df, config):
    """
    Plots slope lines for each column in the dataframe.

    Parameters:
    - df (pandas.DataFrame): The dataframe containing the data to be plotted.
    - config (dict): A dictionary containing the configuration parameters for the plot.

    Configuration Parameters:
    - title1 (str): The main title of the plot.
    - title2 (str): The subtitle of the plot.
    - shift_up (float, optional): The vertical shift of the labels. Default is 2.
    - shift_left (float, optional): The horizontal shift of the labels. Default is 0.5.
    - xaxis_margin (float, optional): The margin added to the x-axis limits. Default is 0.8.
    - highlight_column (str, optional): The column to highlight with a different color. Default is None.
    - ylim_bottom (float, optional): The lower limit of the y-axis. Default is 0.
    - ylim_top (float, optional): The upper limit of the y-axis. Default is 100.
    - second_highlight_line (str, optional): The column to highlight with a second color. Default is None.
    - second_highlight_color (str, optional): The color for the second highlighted line. Default is 'black'.
    - default_color (str, optional): The default color for the slope lines. Default is "#bdbdbd".
    - highlight_color (str, optional): The color for the highlighted line. Default is "#4D77B1".
    - filepath (str, optional): The file path to save the plot. Default is False.

    Returns:
    None
    """
    fig, ax = plt.subplots(1, figsize=(10,8), facecolor="white")

    # Lines to plot should come from the columns of the dataframe
    lines_to_plot = df.columns

    #Title and subtitle
    title1 = config['title1']
    title2 = config['title2']

    #Get config or set to default
    shift_up = config.get('shift_up', 2)
    shift_left = config.get('shift_left', 0.5)
    xaxis_margin = config.get('xaxis_margin', 0.8)
    hihglight_column = config.get('highlight_column', None)
    ylim_bottom = config.get('ylim_bottom', 0)
    ylim_top = config.get('ylim_top', 100)
    second_highlight_line = config.get('second_highlight_line', None)
    second_highlight_color = config.get('second_highlight_color', 'black')
    default_color = config.get('default_color', "#bdbdbd")
    hihglight_color = config.get('highlight_color', "#4D77B1")
    filepath = config.get('filepath', False)
   
    ##Plot each slope line
    for line in lines_to_plot:
        temp = df[line].iloc[[0,-1]]
        color = default_color
        if line == hihglight_column:
            color = hihglight_color
        if line == second_highlight_line:
            color=second_highlight_color
            shift_left = shift_left
        ax.plot(temp.index,  temp.values, color= color, marker='o', markersize=8)
        # end label
        ax.text(temp.index[0]-shift_left, 
                temp.values[0]+shift_up, 
                line, 
                color = color)
        # start label
        ax.text(temp.index[-1]+shift_left, 
                temp.values[-1]+shift_up, 
                line, 
                color = color, ha='right')

    ##add vertical lines
    ax.xaxis.grid(color=default_color, 
                  linestyle='solid', 
                  which='both', 
                  alpha=0.9)
    ax.yaxis.grid(color=second_highlight_color, 
                  linestyle='dashed', 
                  which='both', 
                  alpha=0.1)
    
    ##x limits, x ticks, and y label 
    plt.xlim(df.index[0]-xaxis_margin, 
             df.index[-1].astype(int)+xaxis_margin);
    plt.xticks([df.index[0], df.index[-1]]);
    ax.set_frame_on(False)
    yl = plt.ylim(ylim_bottom, ylim_top)

    ##hide x axis
    ax.tick_params(
            axis='both',          # changes apply to the x-axis
            bottom=False)    # ticks along the bottom edge are off)

    ##Add in title and subtitle
    ax.text(x=0.12, y=1, s=title1, 
            transform=fig.transFigure, 
            ha='left', 
            fontsize=13, weight='bold', alpha=.8)
    ax.text(x=0.12, y=0.95, s=title2,
            transform=fig.transFigure, 
            ha='left', fontsize=11, alpha=.8)

    #ax.set_ylabel('Automation (%)')
    def number_formatter(x,pos):
        s ='{:1.0f}%'.format(x)
        return s 
    ax.yaxis.set_major_formatter(number_formatter)
    
    fig.tight_layout()
    if filepath:
        fig.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.show()

