# -*- coding: utf-8 -*-
 from odoo import http

 class IceCatImtech(http.Controller):
     @http.route('/ice_cat_imtech/ice_cat_imtech/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/ice_cat_imtech/ice_cat_imtech/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('ice_cat_imtech.listing', {
             'root': '/ice_cat_imtech/ice_cat_imtech',
             'objects': http.request.env['ice_cat_imtech.ice_cat_imtech'].search([]),
         })

     @http.route('/ice_cat_imtech/ice_cat_imtech/objects/<model("ice_cat_imtech.ice_cat_imtech"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('ice_cat_imtech.object', {
             'object': obj
         })
