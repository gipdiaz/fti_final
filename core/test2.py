from collections import defaultdict


class TuringMachine(object):

    '''
    This class  implements Turing Machine developed by Alan
    Turing  in 1936. It has  to receive  two  arguments: an
    iterable  object for  the initial configuration  of the
    infinite tape  and a list  of 5-elements  tuple for the
    table. Its  only  no-special method is  necessary to go
    to next step in  the computation. The  configuration of
    this  Turing  Machine has  as  initial and  final state
    respectively  1 and  0, but  it's  possible  to  modify
    them before starting computation.

    Usage:
    >>> machine = TuringMachine('', [(1, '', 1, '', 0)])
    >>> machine.states
    set([1])
    >>> machine.symbols
    set([''])
    >>> machine.step()
    >>> machine.state
    1
    >>> machine.position
    0
    >>> machine.symbol
    ''
    >>> machine.tape
    ['']
    >>> machine.step()
    '''

    def __init__(self, tape, table):

        self.tape_dict = defaultdict(lambda: '')
        self.tape_dict.update(enumerate(list(tape)))
        self.tape = self.tape_dict.values()
        self.table = dict([(x[:2], x[2:]) for x in table])
        self.init_state = 1
        self.final_states = (0,)
        self.states = set(sum([(x[0], x[2]) for x in table], ()))
        self.symbols = set(sum([(x[1], x[3]) for x in table], ()))
        self.symbols.add('')
        self.state = self.init_state
        self.symbol = self.tape_dict[0]
        self.position = 0
        self.result = (1, self.symbol, 0)
        self.is_running = True

    def step(self):

        self.result = self.table[(self.state, self.symbol)]
        self.tape_dict[self.position] = self.result[1]
        self.tape = self.tape_dict.values()
        self.state = self.result[0]
        self.position += self.result[2]
        self.symbol = self.tape_dict[self.position]
        self.is_running = not (self.state in self.final_states)