from django.db import models


class Join(models.Model):
    email = models.EmailField(unique=False)  # unique = False - it's for test
    friend = models.ForeignKey('self', related_name='referral', \
                               null=True, blank=True)
    ref_id = models.CharField(max_length=120, default='NO')  # in real project set unique = True
    ip_address = models.CharField(max_length=120, default='NO')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        unique_together = ('email', 'ref_id')

# class JoinFriends(models.Model):
#     email = models.OneToOneField(Join, related_name='Sharer')
#     friends = models.ManyToManyField(Join, related_name='Friend', \
#                                      null=True, blank=True)
#     emailall = models.ForeignKey(Join, related_name='emailall')
#
#     def __str__(self):
#         # return self.friends.all()[0].email
#         return self.email.email
