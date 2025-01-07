from Privilegios import Admin as ad

admin = ad('pepe', 'Rojas', 'admin', 'admin@tuempresa.es', '123456')
admin.privilegios.show_privileges()