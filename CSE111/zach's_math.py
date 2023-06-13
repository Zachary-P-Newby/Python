def annual_interest_savings(initial, years, rate):
    """
    Returns annual savings for [years] years at [rate] rate with an initial payment of [initial]
    Parameters:
    inital: number
    years: number
    rate: number
    """
    rate = rate/100
    return initial * (1 + rate/365) ** (365 *  years)


if __name__ == "__main__":
    
    initial = float(input("initial: "))
    years = int(input("years: "))
    rate = float(input("rate: "))
    print("")
    
    print(f"${annual_interest_savings(initial, years, rate):.2f400}")