def mux_model(a_i: int, b_i: int, sel_i: bool) -> int:
    if not sel_i:
        return a_i
    else:
        return b_i

