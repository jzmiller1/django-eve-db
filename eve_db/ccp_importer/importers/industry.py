"""
Import industry data.
"""
from eve_db.models import *
from importer_classes import SQLImporter, parse_int_bool, parse_char_notnull

class Importer_industryBlueprints(SQLImporter):
    DEPENDENCIES = ['invTypes',]
    model = IndustryBlueprints
    pks = (('type', 'typeID'),)
    field_map = (('type_id', 'typeID'),
                 ('maxProductionLimit', 'maxProductionLimit'),
                 )

class Importer_industryActivity(SQLImporter):
    DEPENDENCIES = ['invTypes',]
    model = IndustryActivity
    pks = (('type', 'typeID'),)
    field_map = (('type_id', 'typeID'),
                 ('time', 'time'),
                 ('activity', 'activityID')
                 )

class Importer_industryActivityMaterials(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invTypeMaterials']
    model = IndustryActivityMaterial
    pks = (('type', 'typeID'),)
    field_map = (('type_id', 'typeID'),
                 ('activity_id', 'activityID'),
                 ('material_type_id', 'materialTypeID'),
                 ('quantity', 'quantity'),
                 ('consume', 'consume')
                 )

class Importer_industryActivityProbabilities(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invTypeMaterials', 'industryActivity']
    model = IndustryActivityProbability
    pks = (('type', 'typeID'),)
    field_map = (('type_id', 'typeID'),
                 ('activity_id', 'activityID'),
                 ('product_type_id', 'productTypeID'),
                 ('probability', 'probability')
                 )

class Importer_industryActivityProducts(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invTypeMaterials', 'industryActivity']
    model = IndustryActivityProduct
    pks = (('type', 'typeID'),)
    field_map = (('type_id', 'typeID'),
                 ('activity_id', 'activityID'),
                 ('product_type_id', 'productTypeID'),
                 ('quantity', 'quantity')
                 )

class Importer_industryActivitySkills(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invTypeMaterials', 'industryActivity']
    model = IndustryActivitySkill
    pks = (('type', 'typeID'),)
    field_map = (('type_id', 'typeID'),
                 ('activity_id', 'activityID'),
                 ('skill_id', 'skillID'),
                 ('level', 'level')
                 )
