                def get_operator_fn(op):
                    return {
                        "+": operator.add,
                        "-": operator.sub,
                        "*": operator.mul,
                        "divided": operator.__truediv__,
                    }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)

                    speak("your result is")
                    speak(eval_binary_expr(*(my_stringer.split())))