import numpy as np
import pandas as pd
import pytest

from riskkit.data import get_returns

# ------------------------------------------------------------- returns
def test_get_returns_matches_hand_calculation():
    prices = pd.DataFrame({"A": [100, 110, 99]})
    returns = get_returns(prices)
    assert list(returns["A"]) == pytest.approx([0.10, -0.10])

