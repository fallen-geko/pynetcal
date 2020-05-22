"""All tests for pynetcal.py module and 
functionality all in here.
"""
import pytest
from ipaddress import IPv4Address, IPv4Network
from pynetcal.pynetcal import PyNetcalSubnetter, PyNetcalIPv4
from pynetcal.ipv4subnetlist import IPv4SubnetList
from pynetcal.ipv4subnet import IPv4Subnet



# Tests for PyNetcalSubnetter class

@pytest.mark.parametrize("network, hosts, subnets, \
    prioritize_host, expected_result",
    [
        [IPv4Network("192.168.1.0/24"),
        45,
        10,
        True,
        IPv4SubnetList(
            IPv4Subnet(0,IPv4Network("192.168.1.0/26")),
            IPv4Subnet(1,IPv4Network("192.168.1.64/26")),
            IPv4Subnet(2,IPv4Network("192.168.1.128/26")),
            IPv4Subnet(3,IPv4Network("192.168.1.192/26"))),
        ],

        [IPv4Network("10.0.0.0/8"),
        10,
        4,
        False,
        IPv4SubnetList(
            IPv4Subnet(0,IPv4Network("10.0.0.0/10")),
            IPv4Subnet(1,IPv4Network("10.64.0.0/10")),
            IPv4Subnet(2,IPv4Network("10.128.0.0/10")),
            IPv4Subnet(3,IPv4Network("10.192.0.0/10")))
        ],

        [IPv4Network("192.168.1.0/24"),
        67,
        6,
        True,
        IPv4SubnetList(
            IPv4Subnet(0,IPv4Network("192.168.1.0/25")),
            IPv4Subnet(1,IPv4Network("192.168.1.128/25")))
        ]

    ]
)
def test_PyNetcalSubnetter_ipv4_calculate_subnets_flsm_validargs(
        network, hosts, subnets, prioritize_host,
        expected_result
    ):
    """Tests PyNetcalSubnetter.ipv4_calculate_subnets_flsm()
    function for FLSM subnetting mode
    """
    subnetter = PyNetcalSubnetter()
    the_result = subnetter.ipv4_calculate_subnets_flsm(
        network, hosts, subnets, prioritize_host
    )
    assert the_result == expected_result









@pytest.mark.parametrize("network, hosts, expected_result",
    [
        [IPv4Network("192.168.1.0/24"),
        [50,20,10],
        IPv4SubnetList(
            IPv4Subnet(0,IPv4Network("192.168.1.0/26")),
            IPv4Subnet(1,IPv4Network("192.168.1.64/27")),
            IPv4Subnet(2,IPv4Network("192.168.1.96/28"))),
        ],

        [IPv4Network("192.168.1.0/24"),
        [100, 60, 80, 156, 17],
        IPv4SubnetList(
            IPv4Subnet(0,IPv4Network("192.168.1.0/24")))
        ],

    ]
)
def test_PyNetcalSubnetter_ipv4_calculate_subnets_vlsm(network, hosts, expected_result):
    """Tests PyNetcalSubnetter.ipv4_calculate_subnets_vlsm()
    function for VLSM subnetting mode
    """
    subnetter = PyNetcalSubnetter()
    the_result = subnetter.ipv4_calculate_subnets_vlsm(network, hosts)
    assert the_result == expected_result





# Tests for PyNetcalIPv4 class
@pytest.mark.parametrize("ipv4address, result",
    [
        [IPv4Address("255.255.255.0"),
        "11111111.11111111.11111111.00000000"],

        [IPv4Address("255.255.128.0"),
        "11111111.11111111.10000000.00000000"],
    ]
)
def test_PyNetcalIPv4_to_binary(ipv4address, result):
    ipv4 = PyNetcalIPv4()
    assert ipv4.to_binary(ipv4address) == result