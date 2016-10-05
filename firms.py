import parameters


class Firm:

    def __init__(self, unique_number, first_year, last_year=0, output=0):
        self.unique_number = unique_number
        self.members = {}
        self.first_year = first_year
        self.last_year = last_year
        self.output = output
        # constant returns coefficient
        self.a = parameters.random.uniform(0.001, .5)
        # increasing returns coefficient
        self.b = parameters.random.uniform(.751, 1.25)
        # increasing returns exponent
        # keeping Beta at value 2
        self.beta = 2

    def get_id(self):
        return self.unique_number

    def get_b(self):
        return self.b

    def get_a(self):
        return self.a

    def get_beta(self):
        return self.beta

    def update_members(self, worker):
        worker.update_firm(self.get_id())
        self.members[worker.get_id()] = worker

    def withdraw_members(self, worker):
        worker.update_firm(None)
        del self.members[worker.get_id()]

    def num_members(self):
        return len(self.members)

    def total_effort(self):
        E = 0
        for key in list(self.members.keys()):
            E += self.members[key].get_effort()
        return E

    def employee_share(self):
        return self.output / len(self.members)

    def update_output(self):
        self.output = self.a * self.total_effort() + self.b * self.total_effort() ** self.beta

    def get_output(self):
        return self.output

    def set_last_year(self, last_year):
        self.last_year = last_year

    def get_age(self, year):
        return year - self.first_year

    def __str__(self):
        return 'Firm. ID: %s, Num. Employees %s, Output %.2f, a %.2f, b %.2f, beta %.2f' % \
               (self.unique_number, len(self.members), self.output, self.a, self.b, self.beta)
