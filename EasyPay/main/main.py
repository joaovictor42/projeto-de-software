import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from view.home import home_view
from business.model.User import User
from business.model.Payment import Payment
from business.control.UserControl import UserControl
from business.control.PaymentControl import PaymentControl
from business.control.StatsControl import StatsControl
from infra.persistence.PersistenceControl import PersistenceControl


user_persistence = PersistenceControl(User)
user_persistence.create_table()
users = user_persistence.retrieve()
user_control = UserControl()
user_control.bulk_insert(users)

payment_persistence = PersistenceControl(Payment)
payment_persistence.create_table()
payments = payment_persistence.retrieve()
payment_control = PaymentControl()
payment_control.bulk_insert(payments)

StatsControl()


home_view()


user_persistence.drop_table()
user_persistence.create_table()
users = user_control.migrate()
user_persistence.save(users)



