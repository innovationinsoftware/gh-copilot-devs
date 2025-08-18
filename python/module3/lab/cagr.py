# Calculate CAGR (Compound Annual Growth Rate)
def cagr(begin: float, end: float, years: int) -> float:
    """ This function calculates the Compound Annual Growth Rate (CAGR).
        CAGR = (End Value / Begin Value)^(1 / Number of Years) - 1
    """
    return (end / begin) ** (1 / years) - 1

def cagr_percent(begin, end, years):
    """ This function calculates the CAGR and returns it as a percentage.
    """
    return cagr(begin, end, years) * 100