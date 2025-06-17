from odoo import models, fields

class TrainerProfile(models.Model):
    _name = 'academy.trainer.profile'
    _description = 'Trainer Profile'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # For communication and activity tracking

    name = fields.Char(string='Full Name', required=True, tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    phone = fields.Char(string='Phone', tracking=True)
    bio = fields.Html(string='Biography/Summary', tracking=True)
    domains = fields.Many2many('academy.trainer.domain', string='Expertise Domains', tracking=True) # New model to be created
    availability = fields.Selection([
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('partial', 'Partially Available')
    ], string='Availability', default='available', tracking=True)
    location = fields.Char(string='Location (City, Country)', tracking=True)
    website_published = fields.Boolean(string='Visible on Website', default=True, tracking=True)
    user_id = fields.Many2one('res.users', string='Related User', ondelete='set null', help="Optional: Link to an Odoo user for self-management.")
    cv_ids = fields.One2many('academy.trainer.cv', 'trainer_id', string='CVs')
    # Add other fields as needed, e.g., experience, certifications, profile_image

    _sql_constraints = [
        ('email_uniq', 'unique (email)', 'The email address must be unique.')
    ]

class TrainerDomain(models.Model):
    _name = 'academy.trainer.domain'
    _description = 'Trainer Expertise Domain'

    name = fields.Char(string='Domain Name', required=True)
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The domain name must be unique.')
    ]
