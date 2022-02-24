from odoo import models, fields, api
class Film(models.Model):
    _name = 'opencinema.film'
    _descricion = 'opencinema.film'

    name = fields.Char(string="Titulo", required=True)
    fecha = fields.Date(string='Salida')
    descricion = fields.Text()
    duracion = fields.Integer()
