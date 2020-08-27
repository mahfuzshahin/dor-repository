from odoo import models, fields, tools
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class ResearchGrant(models.Model):
    _name = 'research.grant'
    _description = 'Research Grant'

    paper_title = fields.Char('Paper Title', required=True)
    first_author = fields.Char('First Author')
    author_ids = fields.Many2many('res.partner', string='Co-Authors')
    country = fields.Text('Country, venue & date / Volume/Issue', required=True)
    cj_name = fields.Char('Conference / Journal Name', required=True)
    cj_link = fields.Char('Conference / Journal Link', required=True)
    contribution = fields.Char('Contribution to knowledge', required=True)
    impact = fields.Char('Impact and Practical Application', required=True)
    reg_fees = fields.Char('Registration fees', required=True)
    indexed = fields.Selection(
        [('scopus', 'Scopus'),
         ('nonscopus', 'Non-Scopus')],
        'indexed', default="scopus")
    acceptance_document = fields.Binary('Acceptance Document', required=True)
    payment_invoice = fields.Binary('Payment Invoice', required=True)
    full_paper = fields.Binary('Full Paper', required=True)

