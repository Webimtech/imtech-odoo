# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ice_cat_imtech(models.Model):
    _name = 'ice_cat_imtech.ice_cat_imtech'
    _description = 'ice_cat_imtech.ice_cat_imtech'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
