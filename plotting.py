__author__ = 'B2046470858'
import parameters
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
try:
    plt.style.use('ggplot')
except AttributeError:
    pass
import pandas as pd
import os
import ggplot as gg

def firms_dynamics_plot(decision):
    data = pd.read_csv(os.path.join(parameters.OUTPUT_PATH, "temp_general_firms_pop_%s_decision_%s_time_%s.txt" %
                                    (parameters.pop_redutor, decision, parameters.final_Time)), sep=",", header=None, decimal=",").astype(float)
    # renaming the collunms names
    data.columns = ['time', 'total_firms', 'average_output', 'average_age', 'average_size',
                    'new_firms', 'exit_firms','max_size','total_effort','average_effort']

    #logical test to control the process of burn the initial
    if parameters.time_to_cut_plots > 0:
        data = data.loc[(data['time']).astype(int) >= parameters.time_to_cut_plots,:]

    # variable to add in the plot title
    title_pop_val = float(parameters.pop_redutor)*100

    # create a list of a years to plot
    list_of_years_division = list(range(int(data['time'].min()), int(data['time'].max()), 12))+[data['time'].max()+1]
    list_of_years = [int(i/12) for i in list_of_years_division]

    # graph paramter variables
    dpi_var_plot = 700
    width_var_plot = 15
    height_var_plot = 10

    ###############################################################################################################
    # plotting AGENTS UTILITY
    # Total firms
    plot_data = gg.ggplot(data, gg.aes('time', 'total_firms')) + gg.geom_line() + gg.scale_y_continuous(breaks=11) + \
                gg.scale_x_discrete(breaks=list_of_years_division, labels=list_of_years) +\
                gg.ggtitle('Total firms') + gg.xlab('Years') + gg.ylab('Total of Firms')+ gg.theme_bw()

    # logical test for presence of plot, if is TRUE is deleted before save the new one
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH, ('temp_general_total_firms_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time)))) is True:
        os.remove(os.path.join(parameters.OUTPUT_PATH, ('temp_general_total_firms_%s_%s_%s.png' %
                                                        (decision, title_pop_val, parameters.final_Time))))
    # saving the plot
    gg.ggsave(plot_data,os.path.join(parameters.OUTPUT_PATH, ('temp_general_total_firms_%s_%s_%s.png' %
                                                              (decision, title_pop_val, parameters.final_Time))),
              width = width_var_plot, height = height_var_plot, units = "in")

    # Average of output
    plot_data = gg.ggplot(data, gg.aes('time', 'average_output')) + gg.geom_line() + gg.scale_y_continuous(breaks=11) + \
                gg.scale_x_discrete(breaks=list_of_years_division, labels=list_of_years)\
                +gg.ggtitle('Average of output') + gg.xlab('Years') + gg.ylab('Units')+ gg.theme_bw()

    # logical test for presence of plot, if is TRUE is deleted before save the new one
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH, ('temp_general_average_output_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time)))) is True:
        os.remove(os.path.join(parameters.OUTPUT_PATH, ('temp_general_average_output_%s_%s_%s.png' %
                                                        (decision, title_pop_val, parameters.final_Time))))
    # saving the plot
    gg.ggsave(plot_data,os.path.join(parameters.OUTPUT_PATH, ('temp_general_average_output_%s_%s_%s.png' % (decision, title_pop_val, parameters.final_Time))), width = width_var_plot, height = height_var_plot, units = "in")

    # Average of age
    plot_data = gg.ggplot(data, gg.aes('time', 'average_age')) + gg.geom_line() + gg.scale_y_continuous(breaks=11) + \
                gg.scale_x_discrete(breaks=list_of_years_division, labels=list_of_years)\
                +gg.ggtitle('Average of age of firms') + gg.xlab('Years') + gg.ylab('Age of Firms')+ gg.theme_bw()

    # logical test for presence of plot, if is TRUE is deleted before save the new one
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH, ('temp_general_average_age_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time)))) is True:
        os.remove(os.path.join(parameters.OUTPUT_PATH, ('temp_general_average_age_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time))))
    # saving the plot
    gg.ggsave(plot_data,os.path.join(parameters.OUTPUT_PATH, ('temp_general_average_age_%s_%s_%s.png' %
                                                              (decision, title_pop_val, parameters.final_Time))),
              width = width_var_plot, height = height_var_plot, units = "in")

    # Average of size
    plot_data = gg.ggplot(data, gg.aes('time', 'average_size')) + gg.geom_line() + gg.scale_y_continuous(breaks=11) + \
                gg.scale_x_discrete(breaks=list_of_years_division, labels=list_of_years)\
                +gg.ggtitle('Average of size of firms') + gg.xlab('Years') + gg.ylab('Units')+ gg.theme_bw()

    # logical test for presence of plot, if is TRUE is deleted before save the new one
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH, ('temp_general_average_size_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time)))) is True:
        os.remove(os.path.join(parameters.OUTPUT_PATH, ('temp_general_average_size_%s_%s_%s.png' %
                                                        (decision, title_pop_val, parameters.final_Time))))
    # saving the plot
    gg.ggsave(plot_data,os.path.join(parameters.OUTPUT_PATH, ('temp_general_average_size_%s_%s_%s.png' %
                                                              (decision, title_pop_val, parameters.final_Time))),
              width = width_var_plot, height = height_var_plot, units = "in")

    # number of new firms
    plot_data = gg.ggplot(data, gg.aes('time', 'new_firms')) + gg.geom_line() + gg.scale_y_continuous(breaks=11) + \
                gg.scale_x_discrete(breaks=list_of_years_division, labels=list_of_years)\
                +gg.ggtitle('Number of new firms') + gg.xlab('Years') + gg.ylab('Units')+ gg.theme_bw()

    # logical test for presence of plot, if is TRUE is deleted before save the new one
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH, ('temp_general_number_of_new_firms_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time)))) is True:
        os.remove(os.path.join(parameters.OUTPUT_PATH, ('temp_general_number_of_new_firms_%s_%s_%s.png' %
                                                        (decision, title_pop_val, parameters.final_Time))))
    # saving the plot
    gg.ggsave(plot_data,os.path.join(parameters.OUTPUT_PATH, ('temp_general_number_of_new_firms_%s_%s_%s.png' %
                                                              (decision, title_pop_val, parameters.final_Time))),
              width = width_var_plot, height = height_var_plot, units = "in")

    # Number of firms out
    plot_data = gg.ggplot(data, gg.aes('time', 'exit_firms')) + gg.geom_line() + gg.scale_y_continuous(breaks=11) + \
                gg.scale_x_discrete(breaks=list_of_years_division, labels=list_of_years)\
                +gg.ggtitle('Number of firms out') + gg.xlab('Years') + gg.ylab('Units')+ gg.theme_bw()

    # logical test for presence of plot, if is TRUE is deleted before save the new one
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH, ('temp_general_number_of_firms_out_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time)))) is True:
        os.remove(os.path.join(parameters.OUTPUT_PATH, ('temp_general_number_of_firms_out_%s_%s_%s.png' %
                                                        (decision, title_pop_val, parameters.final_Time))))
    # saving the plot
    gg.ggsave(plot_data,os.path.join(parameters.OUTPUT_PATH, ('temp_general_number_of_firms_out_%s_%s_%s.png' %
                                                              (decision, title_pop_val, parameters.final_Time))),
              width = width_var_plot, height = height_var_plot, units = "in")

    # Average and max size of firms
    dat_merged = pd.concat([data.iloc[:, data.columns == 'average_effort'],
                            data.iloc[:, data.columns == 'total_effort']],axis=1)

    plot_data = dat_merged.plot(title='Average and maximum effort of employees')
    plot_data.set_xlabel('Years')
    plot_data.set_ylabel('Values units of effort')
    plot_data.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plot_data.set_xticks(list_of_years_division)
    plot_data.set_xticklabels(list_of_years)
    plot_data.set_axis_bgcolor('w')
    fig = plot_data.get_figure()
    fig.set_size_inches(width_var_plot, height_var_plot)

    # logical test for presence of plot, if is TRUE is deleted before save the new one
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH, ('temp_average_and_maximum_effort_of_firms_out_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time)))) is True:
        os.remove(os.path.join(parameters.OUTPUT_PATH, ('temp_average_and_maximum_effort_of_firms_out_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time))))
    # saving the plot
    fig.savefig(os.path.join(parameters.OUTPUT_PATH, ('temp_average_and_maximum_effort_of_firms_out_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time))), dpi = dpi_var_plot)


    dat_merged = pd.concat([data.iloc[:, data.columns == 'average_size'],
                            data.iloc[:, data.columns == 'max_size']],axis=1)

    plot_data = dat_merged.plot(title='Average and maximum size firms')
    plot_data.set_xlabel('Years')
    plot_data.set_ylabel('Number of employees')
    plot_data.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plot_data.set_xticks(list_of_years_division)
    plot_data.set_xticklabels(list_of_years)
    plot_data.set_axis_bgcolor('w')
    fig = plot_data.get_figure()
    fig.set_size_inches(width_var_plot, height_var_plot)

    # logical test for presence of plot, if is TRUE is deleted before save the new one
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH, ('temp_average_size_and_maximum_of_firms_out_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time)))) is True:
        os.remove(os.path.join(parameters.OUTPUT_PATH, ('temp_average_size_and_maximum_of_firms_out_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time))))
    # saving the plot
    fig.savefig(os.path.join(parameters.OUTPUT_PATH, ('temp_average_size_and_maximum_of_firms_out_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time))), dpi = dpi_var_plot)

def agents_dynamics_plot(decision):
    data = pd.read_csv(os.path.join(parameters.OUTPUT_PATH,"temp_general_agents_pop_%s_decision_%s_time_%s.txt" %
                                    (parameters.pop_redutor, decision, parameters.final_Time)), sep=",",header=None, decimal=",").astype(float)
    data.columns = ['time','municipality','average_utility','average_effort']

    #logical test to control the process of burn the initial
    if parameters.time_to_cut_plots > 0:
        data = data.loc[(data['time']).astype(int) >= parameters.time_to_cut_plots,:]

    # time cutted
    year, months = divmod(parameters.time_to_cut_plots, 12)

    # variable to add in the plot title
    title_pop_val = float(parameters.pop_redutor)*100

    # graph paramter variables
    dpi_var_plot = 700
    width_var_plot = 15
    height_var_plot = 10

    # create a list of a years to plot
    list_of_years_division = list(range(int(data['time'].min()), int(data['time'].max()), 12))+[data['time'].max()+1]
    list_of_years = [int(i/12) for i in list_of_years_division]

    ###############################################################################################################
    # plotting AGENTS UTILITY
    data_utility = data.pivot(index='time', columns='municipality', values='average_utility')
    plot_data = data_utility.plot(title='Average utility agents by municipality, by time')
    plot_data.set_xlabel('Years')
    plot_data.set_ylabel('Values units')
    plot_data.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plot_data.set_xticks(list_of_years_division)
    plot_data.set_xticklabels(list_of_years)
    plot_data.set_axis_bgcolor('w')
    fig = plot_data.get_figure()
    fig.set_size_inches(width_var_plot, height_var_plot)

    # logical test for presence of plot, if is TRUE is deleted before save the new one
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH, ('agents_utility_by_region_decision_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time)))) is True:
        os.remove(os.path.join(parameters.OUTPUT_PATH, ('agents_utility_by_region_decision_%s_%s_%s.png' %
                                                        (decision, title_pop_val, parameters.final_Time))))
    # saving the plot
    fig.savefig(os.path.join(parameters.OUTPUT_PATH, ('agents_utility_by_region_decision_%s_%s_%s.png' %
                                                      (decision, title_pop_val, parameters.final_Time))), dpi = dpi_var_plot)

    # AGENTS EFFORT
    data_effort = data.pivot(index='time', columns='municipality', values='average_effort')
    plot_data = data_effort.plot(title='Average effort agents by municipality, by time')
    plot_data.set_xlabel('Years')
    plot_data.set_ylabel('Values units')
    plot_data.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plot_data.set_xticks(list_of_years_division)
    plot_data.set_xticklabels(list_of_years)
    plot_data.set_axis_bgcolor('w')
    fig = plot_data.get_figure()
    fig.set_size_inches(width_var_plot, height_var_plot)

    # logical test for presence of plot, if is TRUE is deleted before save the new one
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH, ('agents_effort_by_region_decision_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time)))) is True:
        os.remove(os.path.join(parameters.OUTPUT_PATH, ('agents_effort_by_region_decision_%s_%s_%s.png' %
                                                        (decision, title_pop_val, parameters.final_Time))))
    # saving the plot
    fig.savefig(os.path.join(parameters.OUTPUT_PATH, ('agents_effort_by_region_decision_%s_%s_%s.png' %
                                                      (decision, title_pop_val, parameters.final_Time))), dpi = dpi_var_plot)

def firms_together_plot(decision):
    data = pd.read_csv(os.path.join(parameters.OUTPUT_PATH, "temp_general_firms_pop_%s_decision_%s_time_%s.txt" %
                                    (parameters.pop_redutor, decision, parameters.final_Time)), sep=",", header=None, decimal=",").astype(float)
    data.columns = ['time', 'total_firms', 'average_output', 'average_age', 'average_size', 'new_firms', 'exit_firms','max_size','total_effort','average_effort']

    #logical test to control the process of burn the initial
    if parameters.time_to_cut_plots > 0:
        data = data.loc[(data['time']).astype(int) >= parameters.time_to_cut_plots,:]

    # time cutted
    year, months = divmod(parameters.time_to_cut_plots, 12)

    # variable to add in the plot title
    title_pop_val = float(parameters.pop_redutor)*100

    # graph paramter variables
    dpi_var_plot = 700
    width_var_plot = 15
    height_var_plot = 10

    # create a list of a years to plot
    list_of_years_division = list(range(int(data['time'].min()), int(data['time'].max()), 12))+[data['time'].max()+1]
    list_of_years = [int(i/12) for i in list_of_years_division]

    ###############################################################################################################
    # plotting AGENTS UTILITY
    data = data.iloc[:, data.columns != 'average_output']
    data = data.iloc[:, data.columns != 'average_size']
    data = data.iloc[:, data.columns != 'average_age']
    data = data.iloc[:, data.columns != 'time']

    data = pd.concat([data.iloc[:, data.columns == 'total_firms'],
                      data.iloc[:, data.columns == 'new_firms'],
                      data.iloc[:, data.columns == 'exit_firms'],
                      data.iloc[:, data.columns == 'max_size'],
                      data.iloc[:, data.columns == 'total_effort'],
                      data.iloc[:, data.columns == 'average_effort']],axis=1)

    plot_data = data.plot(title='Firms variables, by time')
    plot_data.set_xlabel('Years')
    plot_data.set_ylabel('Values in units')
    plot_data.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plot_data.set_xticks(list_of_years_division)
    plot_data.set_xticklabels(list_of_years)
    plot_data.set_axis_bgcolor('w')
    plot_data.legend(labels=['Total de firmas', 'Novas firmas', 'Firmas fechadas','Máximo tamanho','Esforço','Média do esforço total'])
    plot_data.grid('on', which='major', axis='both' )
    fig = plot_data.get_figure()
    fig.set_size_inches(width_var_plot, height_var_plot)

    # logical test for presence of plot, if is TRUE is deleted before save the new one
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH, ('firms_new_exit_total_decision_%s_%s_%s.png' %
                                                                (decision, title_pop_val, parameters.final_Time)))) is True:
        os.remove(os.path.join(parameters.OUTPUT_PATH, ('firms_new_exit_total_decision_%s_%s_%s.png' %
                                                        (decision, title_pop_val, parameters.final_Time))))
    # saving the plot
    fig.savefig(os.path.join(parameters.OUTPUT_PATH, ('firms_new_exit_total_decision_%s_%s_%s.png' %
                                                      (decision, title_pop_val, parameters.final_Time))), dpi = dpi_var_plot)

def firms_3d_ocurrence_plot(decision):
    data = pd.read_csv(os.path.join(parameters.OUTPUT_PATH,"temp_firms_pop_%s_decision_%s_time_%s.txt" %
                                    (parameters.pop_redutor, decision, parameters.final_Time)), sep=",",header=None, decimal=",")
    data.columns = ['time','firm_id','first_year','last_year','age','number_of_employees','output']
    data = data.loc[data['time']>=data['time'].max()]

    datsize = data.groupby(['age'],as_index=False).size().reset_index()
    datmean = data.groupby(['age'],as_index=False).mean().reset_index()
    dat_merged = pd.merge(datsize, datmean, on='age')
    dat_merged.columns = ['age','freq_firms','index','time','firm_id','first_year','last_year','number_of_employees']

    dat_merged = pd.concat([dat_merged.iloc[:, dat_merged.columns == 'age'],
                            dat_merged.iloc[:, dat_merged.columns == 'freq_firms'],
                            dat_merged.iloc[:, dat_merged.columns == 'number_of_employees']],axis=1)

    # variable to add in the plot title
    title_pop_val = float(parameters.pop_redutor)*100

    # firms occurrence
    freq_firms = dat_merged.pivot_table(index='number_of_employees', columns='age', values='freq_firms').reset_index()
    freq_firms = freq_firms.sort_index(ascending=False)
    freq_firms = freq_firms.fillna(0)

    freq_firms = np.array(freq_firms)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_data, y_data = np.meshgrid(np.arange(freq_firms.shape[1]),
                                  np.arange(freq_firms.shape[0]))

    x_data = x_data.flatten()
    y_data = y_data.flatten()
    z_data = freq_firms.flatten()
    ax.bar3d( x_data,
              y_data,
              np.zeros(len(z_data)),
              1, 1, z_data, color='b', alpha=0.5 )
    plt.xlabel('Age')
    plt.ylabel('Size of firms')
    plt.title('Frequence of Firms by age, by size')
    plt.gca().invert_yaxis()
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH,'fig_freq_occurrence_firms_pop_%s_%s_%s.png' %
            (decision, title_pop_val, parameters.final_Time))) is True:
        os.remove(os.path.join(parameters.OUTPUT_PATH,'fig_freq_occurrence_firms_pop_%s_%s_%s.png' %
                               (decision, title_pop_val, parameters.final_Time)))
    # saving the plot
    plt.savefig(os.path.join(parameters.OUTPUT_PATH,'fig_freq_occurrence_firms_pop_%s_%s_%s.png' %
                             (decision, title_pop_val, parameters.final_Time)))