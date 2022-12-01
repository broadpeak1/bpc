# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inheritHrContract(models.Model):
    _inherit = 'hr.contract'

    fuel_threshold = fields.Float(string='Fuel Threshold')
    probation_allowance = fields.Float(string='Probation Allowance')

