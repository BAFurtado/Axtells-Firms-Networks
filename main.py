import parameters
import agents
import firms
import teaming_up
import os
import statistics
from numpy import mean
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import output
import sys
import plotting

# DECISION ON NETWORKING ##############################################################################################
# If full network (all across municipalities) Decision is True
# If network of friends, exclusively within municipalities Decision is False
decision = False
to_print = True
controller = False
#######################################################################################################################

if controller is True:
    if sys.argv[1] == '0':
        decision = True
    else:
        decision = False

start_run = timer()

# Initialize time

time = statistics.my_stats.get_time()


# INSTANTIATE agents and firms

def generate_agents():
    result = []
    control_n = parameters.my_n.get_n()
    for index in range(len(parameters.my_n.get_cod())):
        for sub_n in range(parameters.my_n.get_pop_mun()[index]):
            result.append(agents.Agent(control_n, parameters.my_n.get_cod()[index]))
            control_n -= 1
    return result


def generate_firms():
    result = []
    for item in range(parameters.my_n.get_n()):
        result.append(firms.Firm(item, time))
    return result


my_agents = generate_agents()

my_firms = generate_firms()

# Instantiate singleton firms


def singleton_firms(workers, singletons):
    key = len(workers)
    while key > 0:
        single = singletons[key - 1]
        worker = workers[key - 1]
        single.update_members(worker)
        singleton_effort = teaming_up.singleton_formula(worker, single)
        worker.update_effort(singleton_effort)
        single.update_output()
        worker.update_utility(single.employee_share())
        key -= 1


singleton_firms(my_agents, my_firms)


def networking(nodes, decision):
    for node in nodes:
        num_neighbors = parameters.random.choice([3, 4, 5])
        for friend in range(num_neighbors):
            check = False
            while check is False:
                new_friend = parameters.random.choice(nodes)
                check = node.add_friend_to_network(new_friend, decision)

networking(my_agents, decision)

def run_the_game(my_agents, my_firms, my_stats, decision):
    my_graveyard = []
    time_elapsed = []
    while my_stats.get_time() < parameters.final_Time:
        start_run1 = timer()
        new_firms = parameters.my_n.get_n()
        on_the_market = []
        for i in range(parameters.activation):
            on_the_market.append(parameters.random.choice(my_agents))

        teaming_up.team_up(on_the_market, my_firms)

        # extinguish empty firms
        exit_firms = len(my_graveyard)
        for firm in my_firms:
            if firm.num_members() == 0:
                firm.set_last_year(my_stats.get_time())
                my_graveyard.append(firm)
                my_firms.remove(firm)
            # update output
            firm.update_output()
            # calculate employee share, update agent utility and save
            for key in firm.members.keys():
                firm.members[key].update_utility(firm.employee_share())

        # Collect statistics
        my_stats.update_total_firms(len(my_firms))
        my_stats.update_average_size(mean([firm.num_members() for firm in my_firms]))
        my_stats.update_average_age(mean([firm.get_age(my_stats.get_time()) for firm in my_firms]))
        my_stats.update_new_firms(parameters.my_n.get_n() - new_firms)
        my_stats.update_exit_firms(len(my_graveyard) - exit_firms)
        my_stats.update_average_output(mean([firm.get_output() for firm in my_firms]))
        total_effort = max(my_firms, key=lambda firm: firm.num_members()).total_effort()
        max_size = max(my_firms, key=lambda firm: firm.num_members()).num_members()
        mean_agent_effort = mean([firm.total_effort() for firm in my_firms])

        if to_print:
            print('Total firms', my_stats.get_total_firms())
            print('Larger firm', max(my_firms, key=lambda firm: firm.num_members()))
            print('Total effort of larger firm', max(my_firms, key=lambda firm: firm.num_members()).total_effort())
            print('Average output %.2f' % my_stats.get_average_output())
            print('Average age %.2f' % my_stats.get_average_age())
            print('Average size %.2f' % my_stats.get_average_size())
            print('New firms', my_stats.get_new_firms())
            print('Exit firms', my_stats.get_exit_firms())
            print('time', my_stats.get_time())
            print('')

        elif my_stats.get_time() == (parameters.final_Time - 1):
            # NOTICE. Agents list change every month
            # checking if there is file
            if os.path.isfile(os.path.join(parameters.OUTPUT_PATH, "temp_results_%s_decision_%s_time_%s.txt" %
                    (parameters.pop_redutor, decision, parameters.final_Time))) is True:
                os.remove(os.path.join(parameters.OUTPUT_PATH, "temp_results_%s_decision_%s_time_%s.txt" %
                                       (parameters.pop_redutor, decision, parameters.final_Time)))
            # open the txt file to save the last values
            results_txt = open(os.path.join(parameters.OUTPUT_PATH, "temp_results_%s_decision_%s_time_%s.txt" %
                                            (parameters.pop_redutor, decision, parameters.final_Time)), 'a')
            for index in range(len(parameters.my_n.get_cod())):
                print('%s: avg. utility %.2f, avg. effort %.2f' %
                      (parameters.my_n.get_cod()[index],
                       mean([agent.get_utility() for agent in my_agents if agent.get_mun() == parameters.my_n.get_cod()[index]]),
                       mean([agent.get_effort() for agent in my_agents if agent.get_mun() == parameters.my_n.get_cod()[index]])))
                results_txt.write('%s: avg. utility %.2f, avg. effort %.2f \n' %
                      (parameters.my_n.get_cod()[index],
                       mean([agent.get_utility() for agent in my_agents if agent.get_mun() == parameters.my_n.get_cod()[index]]),
                       mean([agent.get_effort() for agent in my_agents if agent.get_mun() == parameters.my_n.get_cod()[index]])))
            results_txt.close()

        # calling the output
        output.save_general_agents_data(my_agents, decision)
        output.save_general_firms_data(my_stats, max_size, total_effort,mean_agent_effort, decision)
        output.save_firms_data(my_firms, decision, my_stats)
        my_stats.update_time()

        # computing the time for each while
        end_run1 = timer()

        # to print the time
        m, s = divmod((end_run1 - start_run1), 60)
        h, m = divmod(m, 60)

        #creating the vector to plot the time
        time_elapsed.append(end_run1 - start_run1)

        # computing the time for run all process
        total_time = sum(time_elapsed)+((end_run1 - start_run1)*((parameters.final_Time-1)-my_stats.get_time()))

        # saving the time elapsed for each while
        results_txt = open(os.path.join(parameters.OUTPUT_PATH, "time_results_%s_%s.txt" % (parameters.pop_redutor, decision)), 'a')
        results_txt.write('%s, %.4f \n' %(my_stats.get_time(),(end_run1 - start_run1)))
        results_txt.close()

        # print the time elapsed time for each while
        print("Elapsed time to 1 while %d hs %02d min %02d sec" % (h, m, s))
        print('')

        # calculating the forecast time to process all run model
        m, s = divmod(total_time, 60)
        h, m = divmod(m, 60)
        print("Forecast time for all simulation runs %d hs %02d min %02d sec" % (h, m, s))
        print('')

    #controling the time elapsed to "RUN the game"
    plt.plot(time_elapsed)
    plt.xlabel('Simulation time')
    plt.ylabel('Time for each simulation in seconds')
    plt.title('Time for each while loop')
    plt.savefig(os.path.join(parameters.OUTPUT_PATH,'fig_time_elapsed_pop_%s_decision_%s_time_%s.png' %
                             (parameters.pop_redutor, decision, parameters.final_Time)))

run_the_game(my_agents, my_firms, statistics.my_stats, decision)


plotting.firms_dynamics_plot(decision)
plotting.agents_dynamics_plot(decision)
plotting.firms_3d_ocurrence_plot(decision)
plotting.firms_together_plot(decision)

end_run = timer()
m, s = divmod((end_run - start_run), 60)
h, m = divmod(m, 60)

print('Total employees', sum([firm.num_members() for firm in my_firms]))
print("Elapsed time to run the simulation %d hs %02d min %02d sec" % (h, m, s))
print('------------------------------------------------------')
print('')
