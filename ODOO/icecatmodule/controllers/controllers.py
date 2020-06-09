# -*- coding: utf-8 -*-
 from odoo import http

 class moduleicecat(http.Controller):
     @http.route('/mdicecat/mdicecat/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/mdicecat/mdicecat/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('mdicecat.listing', {
             'root': '/mdicecat/mdicecat',
             'objects': http.request.env['mdicecat.mdicecat'].search([]),
         })

     @http.route('/mdicecat/mdicecat/objects/<model("mdicecat.mdicecat"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('mdicecat.object', {
             'object': obj
         })
