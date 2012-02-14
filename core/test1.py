# turing.py
#
# A Turing Machine simulator for Math Circle talk
#
# Bart Kastermans, www.bartk.nl
 
ADD_PROGRAM = [['START', 1, 'START', 1, 'RIGHT'],
               ['START', 0, 'SECOND', 1, 'RIGHT'],
               ['SECOND', 1, 'SECOND', 1, 'RIGHT'],
               ['SECOND', 0, 'THIRD', 0, 'LEFT'],
               ['THIRD', 1, 'ENDL', 0, 'LEFT'],
               ['ENDL', 1, 'ENDL', 1, 'LEFT'],
               ['ENDL', 0, 'END', 0, 'RIGHT']]
 
MUL_PROGRAM = [['START', 1, 'START', 2, 'RIGHT'],
               ['START', 0, 'SINPUT', 0, 'RIGHT'],
               ['SINPUT', 1, 'SINPUT', 3, 'RIGHT'],
               ['SINPUT', 0, 'SETUPDONE', 0, 'LEFT'],
               ['SETUPDONE', 3, 'SETUPDONE', 3, 'LEFT'],
               ['SETUPDONE', 0, 'FINPUT', 0, 'LEFT'],
               ['FINPUT', 2, 'FINPUT', 2, 'LEFT'],
               ['FINPUT', 0, 'COPYNEXT', 0, 'RIGHT'],
               ['COPYNEXT', 2, 'TOSECOND', 0, 'RIGHT'],
               ['COPYNEXT', 0, 'DONE', 0, 'RIGHT'],
               ['TOSECOND', 2, 'TOSECOND', 2, 'RIGHT'],
               ['TOSECOND', 0, 'DOUBLESECOND', 0, 'RIGHT'],
               ['DOUBLESECOND', 3, 'PDF', 4, 'RIGHT'],
               ['PDF', 1, 'PDF', 1, 'RIGHT'],
               ['PDF', 3, 'PDF', 3, 'RIGHT'],
               ['PDF', 5, 'PDF', 5, 'RIGHT'],
               ['PDF', 0, 'NF', 5, 'LEFT'],
               ['NF', 1, 'NF', 1, 'LEFT'],
               ['NF', 3, 'NF', 3, 'LEFT'],
               ['NF', 5, 'NF', 5, 'LEFT'],
               ['NF', 4, 'DOUBLESECOND', 4, 'RIGHT'],
               ['DOUBLESECOND', 5, 'TOONES', 1, 'RIGHT'],
               ['DOUBLESECOND', 1, 'TOONES', 1, 'RIGHT'],
               ['TOONES', 5, 'TOONES', 1, 'RIGHT'],
               ['TOONES', 1, 'TOONES', 1, 'RIGHT'],
               ['TOONES', 0, 'RESET', 0, 'LEFT'],
               ['RESET', 1, 'RESET', 1, 'LEFT'],
               ['RESET', 4, 'RESET', 3, 'LEFT'],
               ['RESET', 0, 'RESET2', 0, 'LEFT'],
               ['RESET2', 2, 'RESET2', 2, 'LEFT'],
               ['RESET2', 0, 'COPYNEXT', 0, 'RIGHT'],
               ['RESET3', 2, 'COPYNEXT', 0, 'RIGHT'],
               ['DONE', 3, 'DONE', 0, 'RIGHT']]
 
 
class Tape (object):
    """ Tape of the machine.
 
    This represents a two-way infinite tape with initially all zeros
    written on it.
    """
 
    def __init__ (self):
        self.minhead = 0
        self.maxhead = 0
        self.head = 0
        self.tape = {0:0}
 
    def getcursymbol (self):
        return self.tape [self.head]
 
    def setcursymbol (self, value):
        self.tape [self.head] = value
 
    cursymbol = property (getcursymbol, setcursymbol)
 
    def moveright (self):
        """ move the head on position to the right """
        if self.head == self.maxhead:
            self.maxhead += 1
            self.tape [self.maxhead] = 0
 
        self.head += 1
 
    def moveleft (self):
        """ move the head one position to the left """
        if self.head == self.minhead:
            self.minhead -= 1
            self.tape [self.minhead] = 0
 
        self.head -= 1
 
    def __str__ (self):
        """ create a string representation of the tape, * next to head """
        ret_val = ""
 
        for i in range (self.minhead, self.maxhead+1):
            if i == self.head:
                ret_val += "*"
            ret_val += str (self.tape [i]) + " "
 
        return ret_val
 
    def addinteger (self, value):
        """ from location self.head put unary rep of value on tape.
 
        Only use positive natural numbers, the head is left in the
        position one right of the number.
        """
        while value != 0:
            self.cursymbol = 1
            self.moveright ()
            value -= 1
 
    def preparetape (self, listno):
        """ put the list of numbers listno on the tape """
        savehead = self.head
         
        for i in range (0, len (listno)):
            self.addinteger (listno [i])
            self.moveright ()
 
        self.head = savehead
 
    def getnumber (self):
        """ read the number of ones right of the head """
        i = 0
        chead = self.head
        while self.tape [chead] == 1:
            i += 1
            chead += 1
        return i
 
    def reset (self):
        """ set the tape to all zeros and head to 0 """
        self.head = 0
        for i in range (self.minhead, self.maxhead + 1):
            self.tape [i] = 0
 
class Machine (object):
    """ a Turing machine object """
 
    def __init__ (self, program):
        self.tape = Tape ()
        self.state = "START"
        self.program = program
 
    def preparetape (self, listno):
        self.tape.preparetape (listno)
 
    def step (self):
        """ take a step with the machine """
        state = self.state
        symbol = self.tape.cursymbol
        instructions = [inst for inst in self.program
                             if inst[0] == state
                             and inst[1] == symbol]
        if len (instructions) == 0:
            return False  # if no valid instruction HALT the machine
        instruction = instructions [0]
 
        self.state = instruction [2]
        self.tape.cursymbol = instruction [3]
        if instruction [4] == 'RIGHT':
            self.tape.moveright ()
        else:
            self.tape.moveleft ()
 
        return True
 
    def __str__ (self):
        return self.state + " : " + str (self.tape)
 
    def trace (self):
        """ Run the machine and print the state after every step """
        print str (self)
        while self.step ():
            print str (self)
 
    def getoutput (self):
        return self.tape.getnumber ()
 
    def reset (self):
        """ reset the machine """
        self.tape.reset ()
        self.state = 'START'
 
    def run (self, listno):
        """ trace the machine on input represented by listno """
        print "Running on input:", listno
        self.reset ()
        self.preparetape (listno)
        self.trace ()
        print "Output is:", self.getoutput ()
 
ADD = Machine (ADD_PROGRAM)
MUL = Machine (MUL_PROGRAM)
#ADD.run([1,2,3])
MUL.run([2,3,4,5])