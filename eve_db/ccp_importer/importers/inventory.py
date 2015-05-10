"""
Import inventory data.
"""
from eve_db.models import *
from importer_classes import SQLImporter, parse_int_bool, parse_char_notnull


class Importer_invNames(SQLImporter):
    model = InvName
    pks = (('id', 'itemID'),)
    field_map = (('name', 'itemName', parse_char_notnull),)


class Importer_invCategories(SQLImporter):
    model = InvCategory
    pks = (('id', 'categoryID'),)
    field_map = (('name', 'categoryName'),
                 ('icon_id', 'iconID'),
                 ('description', 'description'),
                 ('is_published', 'published', parse_int_bool))


class Importer_invGroups(SQLImporter):
    DEPENDENCIES = ['invCategories']
    model = InvGroup
    pks = (('id', 'groupID'),)
    field_map = (('name', 'groupName'),
                 ('category_id', 'categoryID'),
                 ('description', 'description'),
                 ('icon_id', 'iconID'),
                 ('use_base_price', 'useBasePrice', parse_int_bool),
                 ('allow_manufacture', 'allowManufacture', parse_int_bool),
                 ('allow_recycle', 'allowRecycler', parse_int_bool),
                 ('allow_anchoring', 'anchorable', parse_int_bool),
                 ('is_anchored', 'anchored', parse_int_bool),
                 ('is_fittable_non_singleton', 'fittableNonSingleton', parse_int_bool),
                 ('is_published', 'published', parse_int_bool))


class Importer_invMetaGroups(SQLImporter):
    model = InvMetaGroup
    pks = (('id', 'metaGroupID'),)
    field_map = (('name', 'metaGroupName'),
                 ('icon_id', 'iconID'),
                 ('description', 'description', parse_char_notnull))


class Importer_invMarketGroups(SQLImporter):
    DEPENDENCIES = ['invMarketGroups']
    HIERARCHY_FIELD = 'parentGroupID'
    ID_FIELD = 'marketGroupID'
    model = InvMarketGroup
    pks = (('id', 'marketGroupID'),)
    field_map = (('name', 'marketGroupName'),
                 ('icon_id', 'iconID'),
                 ('description', 'description'),
                 ('parent_id', 'parentGroupID'),
                 ('has_items', 'hasTypes', parse_int_bool))


class Importer_invTypes(SQLImporter):
    DEPENDENCIES = ['invMarketGroups', 'chrRaces',
                    'invGroups']
    model = InvType
    pks = (('id', 'typeID'),)
    field_map = (('name', 'typeName'),
                 ('description', 'description', parse_char_notnull),
                 ('group_id', 'groupID'),
                 ('mass', 'mass'),
                 ('volume', 'volume'),
                 ('capacity', 'capacity'),
                 ('portion_size', 'portionSize'),
                 ('base_price', 'basePrice'),
                 ('market_group_id', 'marketGroupID'),
                 ('is_published', 'published', parse_int_bool),
                 ('race_id', 'raceID'),
                 ('chance_of_duplicating', 'chanceOfDuplicating'))


class Importer_invTypeMaterials(SQLImporter):
    DEPENDENCIES = ['invTypes']
    model = InvTypeMaterial
    pks = (('type', 'typeID'), ('material_type', 'materialTypeID'))
    field_map = (('quantity', 'quantity'),)


class Importer_invMetaTypes(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invMetaGroups']
    model = InvMetaType
    pks = (('type', 'typeID'),)
    field_map = (('parent_type_id', 'parentTypeID'),
                 ('meta_group_id', 'metaGroupID'))


class Importer_dgmAttributeCategories(SQLImporter):
    model = DgmAttributeCategory
    pks = (('id', 'categoryid'),)
    field_map = (('name', 'categoryname'),
                 ('description', 'categorydescription'))


class Importer_dgmAttributeTypes(SQLImporter):
    DEPENDENCIES = ['dgmAttributeCategories', 'eveUnits']
    model = DgmAttributeType
    pks = (('id', 'attributeid'),)
    field_map = (('name', 'attributename'),
                 ('description', 'description'),
                 ('default_value', 'defaultvalue'),
                 ('is_published', 'published', parse_int_bool),
                 ('display_name', 'displayname', parse_char_notnull),
                 ('is_stackable', 'stackable', parse_int_bool),
                 ('high_is_good', 'highisgood', parse_int_bool),
                 ('category_id', 'categoryid'),
                 ('unit_id', 'unitid'),
                 ('icon_id', 'iconID'))


class Importer_dgmTypeAttributes(SQLImporter):
    DEPENDENCIES = ['invTypes', 'dgmAttributeTypes', 'dgmTypeAttributes']
    model = DgmTypeAttribute
    pks = (('inventory_type', 'typeid'), ('attribute', 'attributeid'))
    field_map = (('value_int', 'valueint'),
                 ('value_float', 'valuefloat'))


class Importer_dgmEffects(SQLImporter):
    DEPENDENCIES = ['dgmAttributeTypes']
    model = DgmEffect
    pks = (('id', 'effectID'),)
    field_map = (('name', 'effectName'),
                 ('category', 'effectCategory'),
                 ('pre_expression', 'preExpression'),
                 ('post_expression', 'postExpression'),
                 ('description', 'description', parse_char_notnull),
                 ('guid', 'guid', parse_char_notnull),
                 ('icon_id', 'iconID'),
                 ('is_offensive', 'isOffensive', parse_int_bool),
                 ('is_assistance', 'isAssistance', parse_int_bool),
                 ('duration_attribute_id', 'durationAttributeID'),
                 ('tracking_speed_attribute_id', 'trackingSpeedAttributeID'),
                 ('discharge_attribute_id', 'dischargeAttributeID'),
                 ('range_attribute_id', 'rangeAttributeID'),
                 ('falloff_attribute_id', 'falloffAttributeID'),
                 ('disallow_auto_repeat', 'disallowAutoRepeat', parse_int_bool),
                 ('is_published', 'published', parse_int_bool),
                 ('display_name', 'displayName'),
                 ('is_warp_safe', 'isWarpSafe', parse_int_bool),
                 ('has_range_chance', 'rangeChance', parse_int_bool),
                 ('has_electronic_chance', 'electronicChance', parse_int_bool),
                 ('has_propulsion_chance', 'propulsionChance', parse_int_bool),
                 ('distribution', 'distribution'),
                 ('sfx_name', 'sfxName', parse_char_notnull),
                 ('npc_usage_chance_attribute_id', 'npcUsageChanceAttributeID'),
                 ('npc_activation_chance_attribute_id', 'npcActivationChanceAttributeID'),
                 ('fitting_usage_chance_attribute_id', 'fittingUsageChanceAttributeID'))


class Importer_dgmTypeEffects(SQLImporter):
    DEPENDENCIES = ['invTypes', 'dgmEffects', 'dgmTypeEffects']
    model = DgmTypeEffect
    pks = (('type', 'typeID'), ('effect', 'effectID'))
    field_map = (('is_default', 'isDefault'),)


class Importer_invFlags(SQLImporter):
    DEPENDENCIES = ['invFlags']
    model = InvFlag
    pks = (('id', 'flagID'),)
    field_map = (('name', 'flagName'),
                 ('text', 'flagText'),
                 ('order', 'orderID'))


class Importer_invControlTowerResourcePurposes(SQLImporter):
    DEPENDENCIES = ['invControlTowerResourcePurposes']
    model = InvPOSResourcePurpose
    pks = (('id', 'purpose'),)
    field_map = (('purpose', 'purposeText'),)


class Importer_invControlTowerResources(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invControlTowerResourcePurposes']
    model = InvPOSResource
    pks = (('control_tower_type', 'controlTowerTypeID'),
           ('resource_type', 'resourceTypeID'))
    field_map = (('purpose_id', 'purpose'),
                 ('quantity', 'quantity'),
                 ('min_security_level', 'minSecurityLevel'))


class Importer_invTypeReactions(SQLImporter):
    DEPENDENCIES = ['invTypes']
    model = InvTypeReaction
    pks = (('reaction_type', 'reactionTypeID'), ('type', 'typeID'),
           ('input', 'input', False))
    field_map = (('quantity', 'quantity'),)


class Importer_invContrabandTypes(SQLImporter):
    DEPENDENCIES = ['invTypes', 'chrFactions']
    model = InvContrabandType
    pks = (('faction', 'factionID'), ('type', 'typeID'))
    field_map = (('standing_loss', 'standingLoss'),
                 ('confiscate_min_sec', 'confiscateMinSec'),
                 ('fine_by_value', 'fineByValue'),
                 ('attack_min_sec', 'attackMinSec'))

class Importer_invItems(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invFlags']
    model = InvItem
    pks = (('id', 'itemID'),)
    field_map = (('type_id', 'typeID'),
                 ('owner', 'ownerID'),
                 ('location', 'locationID'),
                 ('flag_id', 'flagID'),
                 ('quantity', 'quantity'))

class Importer_invPositions(SQLImporter):
    DEPENDENCIES = ['invItems']
    model = InvPosition
    pks = (('id', 'itemID'),)
    field_map = (('x', 'x'),
                 ('y', 'y'),
                 ('z', 'z'),
                 ('yaw', 'yaw'),
                 ('pitch', 'pitch'),
                 ('roll', 'roll'))

class Importer_invUniqueNames(SQLImporter):
    DEPENDENCIES = ['invItems', 'invGroups']
    model = InvUniqueName
    pks = (('id', 'itemID'),)
    field_map = (('name', 'itemName'),
                 ('group_id', 'groupID'))

class Importer_invVolumes(SQLImporter):
    DEPENDENCIES = ['invTypes',]
    model = InvVolume
    pks = (('id', 'typeID'),)
    field_map = (('type_id', 'typeID'),
                 ('volume', 'volume'),
                 )