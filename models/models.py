from odoo import models, fields

class Requests(models.Model):
    _name = "requests"
    _description = "Requests"

    title = fields.Char('Title', required=True)
    body = fields.Char('Body')
    category = fields.Many2one('requests.category', string="Category", required=True)
    approver_id = fields.Many2one('hr.employee', string="Approver", required=True)
    user_id = fields.Many2one('hr.employee', string="User", required=True)
    status = fields.Boolean('Status', default=True)
    request_date = fields.Date('Publish Date')


class RequestsCategory(models.Model):
    _name = "requests.category"
    _description = "Requests Category"

    name = fields.Char('Name', required=True)
    description = fields.Char('Description')
