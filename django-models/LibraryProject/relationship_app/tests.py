from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class RoleAccessTests(TestCase):
	def setUp(self):
		# create users
		self.admin = User.objects.create_user(username='admin', password='pass')
		self.librarian = User.objects.create_user(username='librarian', password='pass')
		self.member = User.objects.create_user(username='member', password='pass')

		# assign roles via userprofile (signal auto-creates profile)
		self.admin.userprofile.role = 'Admin'
		self.admin.userprofile.save()
		self.librarian.userprofile.role = 'Librarian'
		self.librarian.userprofile.save()
		self.member.userprofile.role = 'Member'
		self.member.userprofile.save()

	def test_admin_access(self):
		self.client.login(username='admin', password='pass')
		resp = self.client.get(reverse('admin_view'))
		self.assertEqual(resp.status_code, 200)

		# other roles should be denied
		self.client.login(username='librarian', password='pass')
		resp = self.client.get(reverse('admin_view'))
		self.assertNotEqual(resp.status_code, 200)

		self.client.login(username='member', password='pass')
		resp = self.client.get(reverse('admin_view'))
		self.assertNotEqual(resp.status_code, 200)

	def test_librarian_access(self):
		self.client.login(username='librarian', password='pass')
		resp = self.client.get(reverse('librarian_view'))
		self.assertEqual(resp.status_code, 200)

		self.client.login(username='admin', password='pass')
		resp = self.client.get(reverse('librarian_view'))
		self.assertNotEqual(resp.status_code, 200)

		self.client.login(username='member', password='pass')
		resp = self.client.get(reverse('librarian_view'))
		self.assertNotEqual(resp.status_code, 200)

	def test_member_access(self):
		self.client.login(username='member', password='pass')
		resp = self.client.get(reverse('member_view'))
		self.assertEqual(resp.status_code, 200)

		self.client.login(username='admin', password='pass')
		resp = self.client.get(reverse('member_view'))
		self.assertNotEqual(resp.status_code, 200)

		self.client.login(username='librarian', password='pass')
		resp = self.client.get(reverse('member_view'))
		self.assertNotEqual(resp.status_code, 200)
