from . import BaseTestCase


class TestMessageFunctional(BaseTestCase):

    def test_message(self):
        import transaction
        from osmtm.tests import USER1_ID, USER2_ID
        from osmtm.models import Message, User, DBSession
        user1 = DBSession.query(User).get(USER1_ID)
        user2 = DBSession.query(User).get(USER2_ID)
        message = Message(u'subject', user2, user1, u'message')
        DBSession.add(message)
        DBSession.flush()
        id = message.id
        transaction.commit()

        headers = self.login_as_user1()
        self.testapp.get('/message/read/%d' % id, headers=headers, status=200)

        headers = self.login_as_user2()
        self.testapp.get('/message/read/%d' % id, headers=headers, status=403)
