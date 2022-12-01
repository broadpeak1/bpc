# -*- coding: utf-8 -*-
# from odoo import http


# class OcPayrollBpCustomization(http.Controller):
#     @http.route('/oc_payroll_bp_customization/oc_payroll_bp_customization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oc_payroll_bp_customization/oc_payroll_bp_customization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oc_payroll_bp_customization.listing', {
#             'root': '/oc_payroll_bp_customization/oc_payroll_bp_customization',
#             'objects': http.request.env['oc_payroll_bp_customization.oc_payroll_bp_customization'].search([]),
#         })

#     @http.route('/oc_payroll_bp_customization/oc_payroll_bp_customization/objects/<model("oc_payroll_bp_customization.oc_payroll_bp_customization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oc_payroll_bp_customization.object', {
#             'object': obj
#         })
