import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
import models


class Hall(SQLAlchemyObjectType):
    class Meta:
        model = models.Hall


class User(SQLAlchemyObjectType):
    class Meta:
        model = models.User


class Lesson(SQLAlchemyObjectType):
    class Meta:
        model = models.Lesson


class Query(graphene.ObjectType):
    get_all_lessons = graphene.List(Lesson)
    get_all_users = graphene.List(User)

    @staticmethod
    def resolve_get_all_lessons(root, info):
        query = Lesson.get_query(info=info)
        return query.all()


schema = graphene.Schema(query=Query)
