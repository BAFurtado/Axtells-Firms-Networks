import parameters
import firms
import math
import operator
import statistics
from numba import autojit

@autojit
def generate_one_firm():
    parameters.my_n.set_old()
    parameters.my_n.update_n()
    return firms.Firm(parameters.my_n.get_n(), statistics.my_stats.get_time())

@autojit
def singleton_formula(worker, single):
    return (-single.a + 2 * single.b * worker.theta * parameters.omega +
            math.sqrt(single.a ** 2 + 4 * single.b * worker.theta ** 2 * parameters.omega *
                      (single.a + single.b * parameters.omega))) / (2 * single.b * (1 + worker.theta))

@autojit
def larger_firm_formula(new_worker, firm, Ei):
    e_star = max(0, ((-firm.get_a() - 2 * firm.get_b() * (Ei - new_worker.theta * parameters.omega) +
                      (math.sqrt(firm.get_a() ** 2 + 4 * firm.get_b() * new_worker.get_theta() ** 2 *
                                 (parameters.omega + Ei) * (firm.get_a() + firm.get_b() * (parameters.omega + Ei))))) /
                     (2 * firm.get_b() * (1 + new_worker.get_theta()))))
    return e_star

@autojit
def team_up(on_the_market, my_firms):
    for each in on_the_market:
        # Computing possibilities
        # Compute e* and U(e*) in current_firm
        # Choose according to best utility
        current_firm = each.get_firm()
        e_current = each.get_effort()
        u_current = each.get_utility()
        new_firm = False
        for firm in my_firms:
            if firm.get_id() == current_firm:
                firm.withdraw_members(each)
        # Compute for each firm of network e and u
        net_firms = each.friends_firms()
        e_net = {}
        u_net = {}
        firm_net = {}
        for item in net_firms:
            for firm in my_firms:
                if firm.get_id() == item:
                    # calculate Ei
                    Ei = firm.total_effort()
                    # include member
                    firm.update_members(each)
                    # calculate effort e*
                    e_net['u*_' + str(item)] = larger_firm_formula(each, firm, Ei)
                    # update new member effort
                    each.update_effort(e_net['u*_' + str(item)])
                    # calculate total output
                    firm.update_output()
                    # calculate employee share, update agent utility and save
                    each.update_utility(firm.employee_share())
                    u_net['u*_' + str(item)] = each.get_utility()
                    firm_net['u*_' + str(item)] = firm
                    # remove from firm until decision is made
                    firm.withdraw_members(each)

        best_key = max(u_net.items(), key=operator.itemgetter(1))[0]

        # Compute e* and U(e*) for starting up a new firm
        new_start_up = generate_one_firm()
        new_start_up.update_members(each)
        singleton_effort = singleton_formula(each, new_start_up)
        each.update_effort(singleton_effort)
        new_start_up.update_output()
        # update utility based on output per capita and save
        each.update_utility(new_start_up.employee_share())
        s_utility = each.get_utility()
        # Remove member
        new_start_up.withdraw_members(each)

        # Compute best option
        # Current, start_up, network
        utilities = [u_current, s_utility, u_net[best_key]]
        index = utilities.index(max(utilities))

        # set definitive firm for agent
        if index == 0:
            # keep current firm
            for firm in my_firms:
                if firm.get_id() == current_firm:
                    firm.update_members(each)
            each.update_effort(e_current)
            each.update_utility(u_current)
        elif index == 1:
            # start a new company
            new_start_up.update_members(each)
            each.update_effort(singleton_effort)
            each.update_utility(s_utility)
            my_firms.append(new_start_up)
            new_firm = True
        else:
            # join friend's company
            firm_net[best_key].update_members(each)
            each.update_effort(e_net[best_key])
            each.update_utility(u_net[best_key])
        # set n back to original number
        if new_firm is False:
            parameters.my_n.set_n(parameters.my_n.get_old())