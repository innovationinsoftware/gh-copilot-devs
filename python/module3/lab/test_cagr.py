# Test the CAGR function
from cagr import cagr, cagr_percent

def test_cagr():
    # use self.assertAlmostEqual to 4 positions instead of assert
    assert round(cagr(1000, 1500, 3), 2) == 0.14
    assert round(cagr(2000, 3000, 5), 2) == 0.08
    assert roundpip install -U pytest(cagr(1500, 1000, 2), 2) == -0.16