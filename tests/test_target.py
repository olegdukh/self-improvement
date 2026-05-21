import pytest
import socket
from target_code import calculate

def test_is_running_on_hetzner():
    """Ensure that tests are indeed running on our isolated Hetzner VPS"""
    hostname = socket.gethostname()
    assert "gh-runner" in hostname, f"Error: tests executed on wrong host: {hostname}"

def test_calculate_logic():
    """Verify basic mathematical correctness of the function"""
    assert calculate(2, 3) == 5
    assert calculate(-1, -1) == -2
    assert calculate(0, 0) == 0