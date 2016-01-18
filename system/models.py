from django.db import models

class Status( models.Model ):
	id = models.CharField( primary_key=True, max_length=2, db_column='est_estado' )
	name = models.CharField( max_length=15, db_column='est_descrip' )
	comment = models.CharField( max_length=60, db_column='est_coment' )
	color = models.CharField( max_length=8, db_column='est_color' )

	class Meta:
		app_label = 'system'
		db_table = 'estados_adm'

class Company( models.Model ):
	id = models.SmallIntegerField( primary_key=True, db_column = 'emp_id' )
	name = models.CharField( max_length = 100, db_column = 'emp_razon_soc' )
	status = models.CharField( max_length = 2, db_column = 'emp_id' )

	class Meta:
		app_label = 'system'
		db_table = 'empresas_adm'
