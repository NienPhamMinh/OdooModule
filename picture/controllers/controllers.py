# -*- coding: utf-8 -*-
from odoo import http



class Picture(http.Controller):
    @http.route('/slideshow/', auth='public',type='json', methods=['POST'])
    def alliamge(seft):
        all_images=http.request.env['picture.album'].search_read([],['name','image_ids','date_start','date_end'])
        return all_images
                
    # def images(self):
    #     all_album = {}
    #     all_album=allimages()
        
    # def index(self, **kw):
    #     return "Hello, world"

    # @http.route('/picture/picture/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('picture.listing', {
    #         'root': '/picture/picture',
    #         'objects': http.request.env['picture.picture'].search([]),
    #     })

    # @http.route('/picture/picture/objects/<model("picture.picture"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('picture.object', {
    #         'object': obj
    #     })

