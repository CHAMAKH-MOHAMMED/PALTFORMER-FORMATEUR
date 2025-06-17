from odoo import models, fields

class TrainingCenterProfile(models.Model):
    _name = 'academy.training.center.profile'
    _description = 'Training Center Profile'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Center Name', required=True, tracking=True)
    email = fields.Char(string='Contact Email', required=True, tracking=True)
    phone = fields.Char(string='Contact Phone', tracking=True)
    address = fields.Text(string='Address', tracking=True)
    website = fields.Char(string='Website URL', tracking=True)
    description = fields.Html(string='About the Center', tracking=True)
    user_id = fields.Many2one('res.users', string='Related User', ondelete='set null', help="Optional: Link to an Odoo user for self-management.")
    website_published = fields.Boolean(string='Visible on Website', default=True, tracking=True)
    # Add other fields as needed, e.g., accreditation, logo

    _sql_constraints = [
        ('email_uniq', 'unique (email)', 'The email address must be unique.')
    ]
