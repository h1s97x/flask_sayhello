import unittest
from flask import Flask
from app.extensions import bootstrap, db, login_manager, moment, csrf, whooshee

class TestExtensions(unittest.TestCase):
    def setUp(self):
        """Setup a Flask app for testing."""
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Cleanup after tests."""
        self.app_context.pop()

    def test_extensions_initialization(self):
        """Test that extensions are correctly initialized."""
        self.assertIsNotNone(bootstrap)
        self.assertIsNotNone(db)
        self.assertIsNotNone(login_manager)
        self.assertIsNotNone(moment)
        self.assertIsNotNone(csrf)
        self.assertIsNotNone(whooshee)

    def test_extensions_binding(self):
        """Test that extensions can be bound to a Flask app."""
        with self.app.app_context():
            bootstrap.init_app(self.app)
            db.init_app(self.app)
            login_manager.init_app(self.app)
            moment.init_app(self.app)
            csrf.init_app(self.app)
            whooshee.init_app(self.app)
            
            # Verifying if extensions are bound to the app
            self.assertIn('bootstrap', self.app.extensions)
            self.assertIn('sqlalchemy', self.app.extensions)
            self.assertIn('login_manager', self.app.extensions)
            self.assertIn('moment', self.app.extensions)
            self.assertIn('csrf', self.app.extensions)
            self.assertIn('whooshee', self.app.extensions)

if __name__ == '__main__':
    unittest.main()