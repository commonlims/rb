from rb.ketama import Ketama
import six


def test_basic():
    def test(k):
        data = {}
        for i in six.range(1000):
            tower = k.get_node('a%s' % i)
            data.setdefault(tower, 0)
            data[tower] += 1

        return [
            k.get_node('Apple'),
            k.get_node('Hello'),
            k.get_node('Data'),
            k.get_node('Computer')
        ]

    k = Ketama([
        '192.168.0.1:6000', '192.168.0.1:6001', '192.168.0.1:6002',
        '192.168.0.1:6003', '192.168.0.1:6004', '192.168.0.1:6005',
        '192.168.0.1:6006', '192.168.0.1:6008', '192.168.0.1:6007'
    ])
    assert test(k) == ['192.168.0.1:6002', '192.168.0.1:6007',
                       '192.168.0.1:6004', '192.168.0.1:6004']

    k.remove_node('192.168.0.1:6007')
    assert test(k) == ['192.168.0.1:6002', '192.168.0.1:6000',
                       '192.168.0.1:6004', '192.168.0.1:6004']

    k.add_node('192.168.0.1:6007')
    assert test(k) == ['192.168.0.1:6002', '192.168.0.1:6007',
                       '192.168.0.1:6004', '192.168.0.1:6004']
