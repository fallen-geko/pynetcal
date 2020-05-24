"""All tests for the validator.py module and functionalities"""

import pytest
import pynetcal.validator as validator


@pytest.mark.parametrize("ipaddress, expected_result",
[
    ["192.168.1.0", True],
    [6, False],
    ["270.192.0.0", False],
    ["192.168.500.0", False],
    ["10.0.0.1",True],
])
def test_validator_ipv4address(ipaddress, expected_result):
    """Tests the IPv4Address validator
    from the validator module"""
    result = validator.ipv4address(ipaddress)
    assert result == expected_result



@pytest.mark.parametrize("ipaddress, expected_result",
[
    ["11111111.00000000.11110000.01010101", True],
    ["10101010.11110000.11.0010", False],
    ["10101010.10101010.11001100.00110011", True],
    ["11011000.1111.1111111.000001", False],
    ["10000942.1003.00000000.00000000", False],
    ["00000000.00000000.00000000.00000000", True]
])
def test_validator_ipv4address_bin(ipaddress, expected_result):
    """Tests the binary IPv4Address validator
    from the validator module.
    """
    result = validator.ipv4address_bin(ipaddress)
    assert result == expected_result





@pytest.mark.parametrize("netaddr, expected_result",
[
    ["192.168.1.0", True],
    [6, True],
    ["270.192.0.0", False],
    ["192.168.500.0", False],
    ["10.0.0.0/8",True],
    ["est", False]
])
def test_validator_ipv4network(netaddr, expected_result):
    """Tests the IPv4Network validator
    from the validator module"""
    result = validator.ipv4network(netaddr)
    assert result == expected_result








@pytest.mark.parametrize("n, expected_result",
[
    [10, True],
    [112, True],
    [19.45, False], 
    ["number", False],
    ["integer", False],
    ["13", True],
    ["13.897", False]
])
def test_validator_integer(n, expected_result):
    result = validator.integer(n)
    assert result == expected_result

