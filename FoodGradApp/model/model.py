# from peewee import SqliteDatabase, Model, CharField, IntegerField
#
#
# db = SqliteDatabase("all_restaurant_table.sql")
#
# # создаём модель User
# class Table_booking_McDonald(Model):
# # имя пользователя, CharField -- строка
#        number_table = IntegerField()
# # возраст пользователя, IntegerField -- целое число
#        booking = IntegerField()
#        name = CharField()
# # во внутреннем классе Meta указываем нашу базу данных
#
#
# class Meta:
#     database = db
#     db.create_tables([Table_booking_McDonald])
#
# # Добавим
# # пользователей
# # в
# # базу
# # данных:
#
#      user1 = Table_booking_McDonald(name="Дима", age=25)
#      user1.save()
#      user2 = Table_booking_McDonald(name="Костя", age=30)
#      user2.save()