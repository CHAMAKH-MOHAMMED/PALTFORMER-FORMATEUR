from odoo import models, fields

class TrainerCV(models.Model):
    _name = 'academy.trainer.cv'
    _description = 'Trainer CV'

    name = fields.Char(string='CV Title/File Name', required=True)
    trainer_id = fields.Many2one('academy.trainer.profile', string='Trainer', required=True, ondelete='cascade')
    cv_file = fields.Binary(string='CV File', required=True, attachment=True)
    upload_date = fields.Datetime(string='Upload Date', default=fields.Datetime.now, readonly=True)
    description = fields.Text(string='Description/Notes')
