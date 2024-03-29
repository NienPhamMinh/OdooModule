# -*- coding: utf-8 -*-

from odoo import models, fields, api
class image(models.Model):
    _name = 'picture.image'
    name = fields.Char('Image Name')
    description = fields.Text('Description')
    image = fields.Binary()
    # album_ids = fields.Many2many('picture.album')