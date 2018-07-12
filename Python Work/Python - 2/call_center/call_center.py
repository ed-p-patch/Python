num = 0000
class call(object):
    def __init__(self, u_id, caller_name, caller_number, time_oc, reason_oc):
        self.u_id = u_id
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time_oc = time_oc
        self.reason_oc = reason_oc
        self.display()
    def display(self):
        print "ID: {}\n Caller Name: {}\n Caller Number: {}\n Time of Call: {}\n Reason of Call: {}\n".format(self.u_id, self.caller_name, self.caller_number, self.time_oc, self.reason_oc)

class call_center(object):
    def __init__(self, calls, q_size):
        self.calls = calls
        self.q_size = q_size
        self.info()
    def add(self, item):
        self.calls.append(item)
        return self
    def remove(self):
        self.calls.remove(self.calls[0])
        return self
    def info(self):
        print "Queue length: {}".format(len(self.calls))+"Of {}".format(self.q_size)+"\n-----------------------------------\n"
        for x in range(0, len(self.calls)):
            print "|{}|{}|\n".format(self.calls[x].caller_name, self.calls[x].caller_number)
        return self

c1 = call(num, 'Patrick', '407-971-1881', '7:30', 'Support')
c2 = call(num, 'Scot', '403-971-1881', '3:30', 'Return')
c3 = call(num, 'Gary', '402-971-1881', '2:30', 'Return')
some_queue = [c1, c2, c3]
CENTER_1 = call_center(some_queue, 15)
c4 = call(num, 'Ryan', '401-971-1881', '1:30', 'Support')
c5 = call(num, 'Michelle', '408-971-1881', '5:30', 'Support')
CENTER_1.add(c4).remove().remove().remove().add(c5)