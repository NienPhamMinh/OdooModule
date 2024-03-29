# -*- coding: utf-8 -*-

from odoo import models, fields, api


class album(models.Model):
    _name = 'picture.album'
    _description = 'slide'
    name = fields.Text('Description')
    # model hình chứa nhiếu hình ảnh quản lý chỉ bởi 1 album
    image_ids =fields.Many2many("picture.image",relation="picture_album_picture_image_rel", string='Hình ảnh')
   
    date_start = fields.Date(string="Start Date") 
    date_end = fields.Date(string="End Date")      
         
    # @api.model
    # def create(self ,vals):
    #     attachment = self.env['ir.attachment'].create({
    #         'name': 'my-album',
    #         'data': vals['image'],
    #         'res_model': 'album',
    #         'res_id':vals['id'],
    #     })
    #     vals['image']=attachment.id
    #     return super(picture,self).create(vals)
    # def get_image(self,record):
    #     if record.image:
    #         return '/web/image/%s/%s'%(record.image.id,'image')
    #     else: 
    #         return'/web/static/img/'
        
    