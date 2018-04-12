class Call(object):
    def __init__(self, callID, caller_name, phone_number, time, reason):
        self.callID = callID
        self.caller_name = caller_name
        self.phone_number = phone_number
        self.time = time
        self.reason = reason

    def display(self):
        print "The call ID is ", self.callID
        print "The caller's name is ", self.caller_name
        print "The caller's phone number is " ,self.phone_number
        print "The the time of the call is ", self.time
        print "The reason of the call is ", self.reason
        return self

class CallCenter (object):
    def __init__(self):
        self.calls= []
        self.queue_size = 0
    def add(self,call):
        self.calls.append(call)
        self.queue_size+=1
        return self
    def remove(self):
        self.calls.pop(0)
        self.queue_size-=1
        return self
    def sort(self):
        self.calls.sort(key=lambda calls:calls.time)
        print self.calls

    def info(self):
        for i in self.calls:
            print "name: {}, phone number: {}, calls in queue {}".format(i.caller_name,i.phone_number,self.queue_size)
    def remove_call(self,number):
        i= 0
        for call in self.calls:
            if call.phone_number == number:
                self.calls.pop(i)
                self.queue_size -=1
            i+=1
        return self




CallCenter1=CallCenter()

call1=Call(123,"john",25461205,"12:00","help")
call2=Call(123,"john",44444444,"10:00","help")
call3=Call(123,"john",555555555,"1:00","help")
call4=Call(123,"john",66666666,"5:00","help")
call5=Call(123,"john",77777777,"8:00","help")

CallCenter1.add(call1).add(call2).add(call3).add(call4).add(call5).sort()
CallCenter1.info()