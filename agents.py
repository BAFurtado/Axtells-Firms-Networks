import parameters


class Agent:

    def __init__(self, unique_number, mun):
        self.unique_number = unique_number
        self.mun = mun
        self.theta = parameters.random.uniform(0, 1)
        self.utility = 0
        self.effort = 0
        self.firm_id = None
        self.network = {}

    def get_theta(self):
        return self.theta

    def get_effort(self):
        return self.effort

    def get_utility(self):
        return self.utility

    def update_effort(self, effort):
        self.effort = effort

    def get_firm(self):
        return self.firm_id

    def update_firm(self, firm_id):
        self.firm_id = firm_id

    def update_utility(self, output_capita):
        self.utility = (output_capita ** self.theta) * ((parameters.omega - self.effort) ** (1 - self.theta))

    def get_id(self):
        return self.unique_number

    def get_mun(self):
        return self.mun

    def add_friend_to_network(self, friend, decision):
        success = False
        if friend.get_id() not in self.network.keys() and friend.get_id() != self.get_id():
            if decision is True:
                self.network[friend.get_id()] = friend
                success = True
            else:
                if self.get_mun() == friend.get_mun():
                    self.network[friend.get_id()] = friend
                    success = True
        return success

    def friends_firms(self):
        firms_ids = []
        for key in self.network.keys():
            firms_ids.append(self.network[key].get_firm())
        return firms_ids

    def __str__(self):
        return 'Ag. ID: %s, Theta %.2f, Effort %.2f, Utility %.2f, Current firm %s, Network %s' % \
               (self.unique_number, self.theta, self.effort, self.utility, self.firm_id, self.network.keys())
