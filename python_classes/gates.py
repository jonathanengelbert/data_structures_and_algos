class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label


    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def get_pin_a(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate {gate}".format(gate=self.get_label())))
        else:
            return self.pinA.getFrom().get_output()

    def get_pin_b(self):
        if self.pinB == None:
            return int(input("Enter Pin A input for gate {gate}".format(gate=self.get_label())))
        else:
            return self.pinB.getFrom().get_output()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def get_pin(self):
        if not self.pin:
            return int(input("Enter Pin A input for gate {gate}".format(gate=self.get_label())))
        else:
            return self.pin.getFrom().get_output()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    def __init__(self, n):
        super(AndGate, self).__init__(n)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()

        if (a == 1 and b == 1):
            return 1
        else:
            return  0

class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 or b == 1:
            return 1
        else:
            return  0

class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1

class Connector:
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.from_gate

    def getTo(self):
        return self.to_gate


def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.get_output())

main()
