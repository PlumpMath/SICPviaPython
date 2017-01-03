# Exercise 3.28.
# Define an or-gate as a primitive function box. Your or-gate constructor
# should be similar to and-gate.

def or_gate(a1, a2, output):
    def or_action_procedure():
        if not hasattr(or_action_procedure, "new_value"):
            or_action_procedure.new_value = logical_or(get_signal(a1),
                                                       get_signal(a2))
        def func():
            set_signal(output, or_action_procedure.new_value)
        after_delay(or_gate_delay, func)
    add_action(a1, or_action_procedure)
    add_action(a2, or_action_procedure)

def logical_not(s1, s2):
    if s1 == 1 or s2 == 1:
        return 1
    return 0

# Exercise 3.29.
# Another way to construct an or-gate is as a compound digital logic device,
# built from and-gates and inverters. Define a procedure or-gate that
# accomplishes this. What is the delay time of the or-gate in terms of
# and-gate-delay and inverter-delay?

def or_gate(a1, a2, output):
    c1 = make_wire()
    c2 = make_wire()
    c3 = make_wire()
    inverter(a1, c1)
    inverter(a2, c2)
    and_get(c1, c2, c3)
    inverter(c3, output)

# Exercise 3.30.
# Figure 3.27 shows a ripple-carry adder formed by stringing together n
# full-adders. This is the simplest form of parallel adder for adding two n-bit
# binary numbers. The inputs A1, A2, A3, ..., An and B1, B2, B3, ..., Bn are
# the two binary numbers to be added (each Ak and Bk is a 0 or a 1). The
# circuit generates S1, S2, S3, ..., Sn, the n bits of the sum, and C, the
# carry from the addition. Write a procedure ripple-carry-adder that generates
# this circuit. The procedure should take as arguments three lists of n wires
# each -- the Ak, the Bk, and the Sk -- and also another wire C. The major
# drawback of the ripple-carry adder is the need to wait for the carry signals
# to propagate. What is the delay needed to obtain the complete output from an
# n-bit ripple-carry adder, expressed in terms of the delays for and-gates,
# or-gates, and inverters?

def ripple_carry_adder(a, b, s, c)
    c_in = make_wire()
    if cdr(a) == None:
        set_signal(c_in, 0)
        return ripple_carry_adder(cdr(a), cdr(b), cdr(s), c_in)
    return full_adder(car(a), car(b), c_in, car(s), c)









a = make_wire()
b = make_wire()
c = make_wire()
d = make_wire()
e = make_wire()
s = make_wire()

def inverter(input_, output):
    def invert_input():
        if not hasattr(invert_input, "new_value"):
            invert_input.new_value = logical_not(get_signal(input_))
        def func():
            set_signal(output, invert_input.new_value)
        after_delay(inverter_delay, func)
    add_action(input_, invert_input)
    print("ok")

def logical_not(s):
    if s == 0:
        return 1
    if s == 1:
        return 0
    raise Exception("Invalid signal")

def and_gate(a1, a2, output):
    def and_action_procedure():
        if not hasattr(and_action_procedure, "new_value"):
            and_action_procedure.new_value = logical_and(get_signal(a1), get_signal(a2))
        def func():
            set_signal(output, and_action_procedure.new_value)
        after_delay(and_gate_delay, func)
    add_action(a1, and_action_procedure)
    add_action(a2, and_action_procedure)