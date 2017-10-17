from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        for item in self.db.test_collection.find():
            item['new_column1'] = "fake_value"
            self.db.test_collection.save(item)
