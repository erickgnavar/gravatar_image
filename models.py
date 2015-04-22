# coding: utf-8
import base64
import hashlib
import urllib2

from openerp import models, api


def get_image(email=''):
    url = 'http://www.gravatar.com/avatar/{}?s=200'
    _hash = hashlib.md5(email).hexdigest()
    try:
        res = urllib2.urlopen(url.format(_hash))
        raw_image = res.read()
        return base64.encodestring(raw_image)
    except urllib2.HTTPError:
        return False


class Partner(models.Model):

    _inherit = 'res.partner'

    @api.one
    def get_gravatar_image(self):
        image = get_image(self.email or '')
        if image:
            self.write({
                'image': image
            })


class ResUser(models.Model):

    _inherit = 'res.users'

    @api.one
    def get_gravatar_image(self):
        image = get_image(self.email or '')
        if image:
            self.write({
                'image': image
            })
