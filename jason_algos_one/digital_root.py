def digital_root(n):
    if n <= 9:
        return n
    else:
        m = 0
        for i in str(n):
            m += int(i)
        return(digital_root(m))

print(" I return:", digital_root(1275))
