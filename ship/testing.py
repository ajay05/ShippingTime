import os
import unittest
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

if __name__ == '__main__':
    unittest.main()