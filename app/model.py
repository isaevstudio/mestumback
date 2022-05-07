import peewee as pw
from decouple import config


pg_db = pw.PostgresqlDatabase(config('database'),
                              user=config('user'),
                              password=config('password'),
                              host=config('host'),
                              port=config('port'))
pg_db.connect()

class UserPlayer(pw.Model):
    id = pw.PrimaryKeyField()
    uid = pw.IntegerField(null=False)
    is_active = pw.IntegerField(null=False)


    class Meta:
        database = pg_db


if __name__ == '__main__':
    UserPlayer.create_table()
