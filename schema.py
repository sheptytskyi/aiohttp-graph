import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import select
from sqlalchemy.orm import selectinload

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

    @staticmethod
    async def resolve_get_all_lessons(root, info):
        result = await models.async_session.execute(
            select(models.Lesson).options(
                selectinload(models.Lesson.hall),
                selectinload(models.Lesson.coach)
            )
        )

        return result.scalars().all()


schema = graphene.Schema(query=Query)
