import unittest

from datetime import datetime

from app import app, db
from models import Driver, Passenger

from views import get_user_from_token

class DataBaseTests(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def testDriverCreate(self):
        test_token = "test_token"

        # Create driver
        d = Driver(test_token)
        db.session.add(d)
        db.session.commit()

        # Test query
        drivers = Driver.query.all()
        self.assertEqual(len(drivers), 1)
        self.assertEqual(drivers[0].token, test_token)

    def testPassengerCreate(self):
        src = (0.5, -0.5)
        dest = (0.4, -0.4)

        # Create passenger
        p = Passenger(src[0], src[1],
                dest[0], dest[1])
        db.session.add(p)
        db.session.commit()

        passengers = Passenger.query.all()
        self.assertEqual(len(passengers), 1)
        self.assertEqual(passengers[0].src_lat, src[0])
        self.assertEqual(passengers[0].src_long, src[1])
        self.assertEqual(passengers[0].dest_lat, dest[0])
        self.assertEqual(passengers[0].dest_long, dest[1])

    def testPassengerDateTimeDefault(self):
        src = (0.5, -0.5)
        dest = (0.4, -0.4)

        # Create passenger
        p = Passenger(src[0], src[1],
                dest[0], dest[1])
        db.session.add(p)
        db.session.commit()

        passenger = Passenger.query.first()
        # 10 second allowance between creating and testing timestamp
        self.assertAlmostEqual(passenger.datetime.timestamp(),
                datetime.now().timestamp(), delta=10)

    def testPassengerDateTimeCustom(self):
        src = (0.5, -0.5)
        dest = (0.4, -0.4)

        # Create passenger
        time = datetime(2016, 9, 6)
        p = Passenger(src[0], src[1],
                dest[0], dest[1], datetime = time)
        db.session.add(p)
        db.session.commit()

        passenger = Passenger.query.first()
        # 10 second allowance between creating and testing timestamp
        self.assertNotAlmostEqual(passenger.datetime.timestamp(),
                datetime.now().timestamp(), delta=10)

class TokenTest(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_get_new_token(self):
        a = get_user_from_token('get_new_token_test')
        self.assertNotEqual(a, None)
        self.assertEqual(len(Driver.query.all()), 1)

    def test_get_existing_token(self):
        d = Driver('get_existing_token_test')
        db.session.add(d)
        db.session.commit()
        self.assertEqual(len(Driver.query.all()), 1)

        a = get_user_from_token('get_existing_token_test')
        self.assertEqual(a, d)
        self.assertEqual(len(Driver.query.all()), 1)
