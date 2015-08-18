import os
import unittest
import sys
sys.path.append('../')
import ship
import tempfile


class shipTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, ship.app.config['DATABASE'] = tempfile.mkstemp()
        ship.app.config['TESTING'] = True
        self.app = ship.app.test_client()
        ship.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(ship.app.config['DATABASE'])
    
    def test_add_delivery(self):
        """ Test the delivery display """
        body = self.app.post('/add', data={
            'tracking': '10001',
            'carrier': 'UPS',
            'street_address': 'John Doe, Beverly Hills, CA',
            'zipcode': '90069' 
        }, follow_redirects=True)
        assert 'Delivery added' in body.data

        body = self.app.post('/add', data={
            'tracking': '',
            'carrier': 'UPS',
            'street_address': 'John Doe, Beverly Hills, CA',
            'zipcode': '90069' 
        }, follow_redirects=True)
        assert 'Invalid tracking ID' in body.data

        body = self.app.post('/add', data={
            'tracking': '10001',
            'carrier': 'UPS',
            'street_address': '',
            'zipcode': '90069' 
        }, follow_redirects=True)
        assert 'Invalid street address' in body.data

        body = self.app.post('/add', data={
            'tracking': '10001',
            'carrier': 'UPS',
            'street_address': 'John Doe, Beverly Hills, CA',
            'zipcode': '' 
        }, follow_redirects=True)
        assert 'Invalid zipcode' in body.data

        body = self.app.post('/add', data={
            'tracking': '10001',
            'carrier': 'UPS',
            'street_address': 'John Doe, Beverly Hills, CA',
            'zipcode': '9006' 
        }, follow_redirects=True)
        assert 'Invalid zipcode' in body.data

        body = self.app.post('/add', data={
            'tracking': '',
            'carrier': '',
            'street_address': '',
            'zipcode': '' 
        }, follow_redirects=True)
        assert 'Invalid tracking ID, street address, zipcode, carrier' in body.data

    def test_show_deliveries(self):  
        """ Test home page """
        body = self.app.get('/')
        assert 'Shipping Time' in body.data 
        self.app.post('/add', data={
            'tracking': '10001',
            'carrier': 'UPS',
            'street_address': 'John Doe, Beverly Hills, CA',
            'zipcode': '90069' 
        }, follow_redirects=True)
        self.app.post('/add', data={
            'tracking': '10002',
            'carrier': 'FedEx',
            'street_address': 'Jane Doe, West Hollywood, CA',
            'zipcode': '90059' 
        }, follow_redirects=True)
        body = self.app.get('/')
        assert '10001' in body.data 
        assert 'UPS' in body.data 
        assert 'John Doe' in body.data 
        assert '90069' in body.data 
        assert '10002' in body.data 
        assert 'FedEx' in body.data 
        assert 'Jane Doe' in body.data 
        assert '90059' in body.data 


    def test_assert_valid_entries(self):
        result = ship.assert_valid_entries('', 'abc', '90009', 'USPS')
        assert 'tracking ID' in result
        result = ship.assert_valid_entries('10001', '', '90009', 'USPS')
        assert 'street address' in result
        result = ship.assert_valid_entries('10001', 'abc', 'xyz', 'USPS')
        assert 'zipcode' in result
        result = ship.assert_valid_entries('10001', 'abc', '', 'USPS')
        assert 'zipcode' in result
        result = ship.assert_valid_entries('10001', 'abc', 'xyz', '')
        assert 'carrier' in result
        result = ship.assert_valid_entries('', 'abc', 'xyz', '')
        assert 'tracking ID, zipcode, carrier' in result
        result = ship.assert_valid_entries('', '', '', '')
        assert 'tracking ID, street address, zipcode, carrier' in result

if __name__ == '__main__':
    unittest.main()
