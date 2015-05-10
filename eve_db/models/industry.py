"""
This module holds industry-related models.
"""

from django.db import models

class IndustryBlueprints(models.Model):
    """
    CCP Table: industryBlueprints
    CCP Primary key: "typeID" smallint(6)
    """
    type = models.ForeignKey('InvType')
    maxProductionLimit = models.IntegerField(null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['type']
        verbose_name = 'Industry Blueprint'
        verbose_name_plural = 'Industry Blueprints'

    def __unicode__(self):
        return self.type.name

    def __str__(self):
        return self.__unicode__()

class IndustryActivity(models.Model):
    """
    CCP Table: industryActivity
    CCP Primary key: "typeID" smallint(6)

    CCP Activity Codes
    1 - manufacturing
    2 - copying
    3 - research_time
    4 - research_material
    5 - invention
    """
    type = models.ForeignKey('InvType')
    time = models.IntegerField(null=True)
    activity = models.IntegerField(null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['type']
        verbose_name = 'Industry Activity'
        verbose_name_plural = 'Industry Activities'

    def __unicode__(self):
        return self.type.name

    def __str__(self):
        return self.__unicode__()

class IndustryActivityMaterial(models.Model):
    """
    CCP Table: industryActivityMaterials
    CCP Primary key: "typeID" smallint(6)
    """
    type = models.ForeignKey('InvType')
    activity = models.ForeignKey('IndustryActivity')
    material_type = models.ForeignKey('InvType', related_name='material_type')
    quantity = models.IntegerField(null=True)
    consume = models.BooleanField(default=False)

    class Meta:
        app_label = 'eve_db'
        ordering = ['type']
        verbose_name = 'Industry Activity Material'
        verbose_name_plural = 'Industry Activity Materials'

    def __unicode__(self):
        return "{} - {} {}".format(self.type.name, self.quantity, self.material_type.name)

    def __str__(self):
        return self.__unicode__()

class IndustryActivityProbability(models.Model):
    """
    CCP Table: industryActivityProbabilities
    CCP Primary key: "typeID" smallint(6)
    """
    type = models.ForeignKey('InvType')
    activity = models.ForeignKey('IndustryActivity')
    product_type = models.ForeignKey('InvType', related_name='product_type')
    probability = models.IntegerField(null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['type']
        verbose_name = 'Industry Activity Probability'
        verbose_name_plural = 'Industry Activity Probabilities'

    def __unicode__(self):
        return self.type.name

    def __str__(self):
        return self.__unicode__()

class IndustryActivityProduct(models.Model):
    """
    CCP Table: industryActivityProducts
    CCP Primary key: "typeID" smallint(6)
    """
    type = models.ForeignKey('InvType')
    activity = models.ForeignKey('IndustryActivity')
    product_type = models.ForeignKey('InvType', related_name='product_type_product')
    quantity = models.IntegerField(null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['type']
        verbose_name = 'Industry Activity Product'
        verbose_name_plural = 'Industry Activity Products'

    def __unicode__(self):
        return self.type.name

    def __str__(self):
        return self.__unicode__()

class IndustryActivitySkill(models.Model):
    """
    CCP Table: industryActivitySkills
    CCP Primary key: "typeID" smallint(6)
    """
    type = models.ForeignKey('InvType')
    activity = models.ForeignKey('IndustryActivity')
    skill = models.ForeignKey('InvType', related_name='industry_skill')
    level = models.IntegerField(null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['type']
        verbose_name = 'Industry Activity Skill'
        verbose_name_plural = 'Industry Activity Skills'

    def __unicode__(self):
        return self.type.name

    def __str__(self):
        return self.__unicode__()


