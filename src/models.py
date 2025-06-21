from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    # Add a username field
    username: Mapped[str] = mapped_column(
        String(80), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # return the username
            "username": self.username,
            # do not serialize the password, its a security breach
        }


class Follower(db.Model):
    __tablename__ = 'follower'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    follower_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "follower_id": self.follower_id,
        }


class Comment(db.Model):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    content: Mapped[str] = mapped_column(String(500), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "content": self.content,
        }


class Post(db.Model):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    content: Mapped[str] = mapped_column(String(500), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "content": self.content,
        }


class Media(db.Model):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)
    url: Mapped[str] = mapped_column(String(500), nullable=False)
    type: Mapped[str] = mapped_column(str(50), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "post_id": self.post_id,
            "url": self.url,
        }
