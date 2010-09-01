# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Image.text'
        db.add_column('imagehost_image', 'text', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Changing field 'Image.slug'
        db.alter_column('imagehost_image', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100))

        # Adding index on 'Image', fields ['slug']
        db.create_index('imagehost_image', ['slug'])


    def backwards(self, orm):
        
        # Removing index on 'Image', fields ['slug']
        db.delete_index('imagehost_image', ['slug'])

        # Deleting field 'Image.text'
        db.delete_column('imagehost_image', 'text')

        # Changing field 'Image.slug'
        db.alter_column('imagehost_image', 'slug', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True))


    models = {
        'imagehost.image': {
            'Meta': {'ordering': "('-created_on',)", 'object_name': 'Image'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['imagehost']
