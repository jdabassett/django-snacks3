from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

class TestSnackCreateUpdateDelete(TestCase):
    def setUp(self):
        self.purchaser = get_user_model().objects.create_user(username="tester", email="tester_email", password="tester_password")
        self.snack = Snack.objects.create(title="test_name", description="test_description", purchaser=self.purchaser)

    def test_snack_create(self):
        response = self.client.post(
            reverse("snack_create"),
            {'title': "create_snack", "description": "create_description", "purchaser": self.purchaser.id},
            follow=True
        )

        self.assertRedirects(response, reverse('snack_detailed', kwargs={"pk": "2"}))
        self.assertContains(response, "create_snack")

    def test_snack_update(self):
        response = self.client.post(
            reverse("snack_update", kwargs={"pk": self.snack.id}),
            {'title': "update_snack", "description": "update_description", "purchaser": self.purchaser.id},
            follow=True
        )
        # self.assertRedirects(response, reverse('snacks_list'))
        self.assertContains(response, "update_snack")

    def test_snack_delete(self):
        response = self.client.get(reverse("snack_delete", kwargs={"pk": self.snack.id}))
        self.assertEqual(response.status_code, 200)

        response = self.client.delete(
            reverse("snack_delete", kwargs={"pk": self.snack.id}),
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('snacks_list'), target_status_code=200)

class TestSnacksRead(TestCase):
    def setUp(self):
        self.purchaser = get_user_model().objects.create_user(username="test_username", password="test_password", email="test_email")
        self.snack = Snack.objects.create(title="test_name", description="test_description", purchaser=self.purchaser)

    def test_snack_list_status_code_templates_contents(self):
        response = self.client.get(reverse('snacks_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "snacks_list.html")
        snacks = response.context['snacks_list']
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[0].title, self.snack.title)
        self.assertEqual(snacks[0].description, self.snack.description)

    def test_snack_detailed_status_templates_contents(self):
        response = self.client.get(reverse('snack_detailed', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'snack_detailed.html')
        snack = response.context['snack_detailed']
        self.assertEqual(snack.title, self.snack.title)
        self.assertEqual(snack.description, self.snack.description)
        self.assertEqual(snack.purchaser.username, self.purchaser.username)




