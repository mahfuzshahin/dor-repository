from odoo import models, fields, tools
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class DoRPolicy(models.Model):
    _name = 'dor.policy'
    _description = 'Research & SDGs Policy'
    _order = 'name asc, name'

    name = fields.Char('Policy Title', required=True)
    description = fields.Html(string='Description', sanitize=True, strip_style=False)
    attachment = fields.Binary('Attachment')

