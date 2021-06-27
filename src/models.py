import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(60), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    mediatype = Column(String(50))
    url = Column(String(50))
    location = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    date = Column(String(20))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)
    post = relationship(Post)

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_from = relationship(User)
    user_to = relationship(User)

class Like(Base):
    __tablename__ = 'like'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    post = relationship(Post)
    user = relationship(User)

class Chat(Base):
    __tablename__ = 'chat'
    id = Column(Integer, primary_key=True)
    user_one_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_two_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_one = relationship(User)
    user_two = relationship(User)

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey('chat.id'), primary_key=True)
    text = Column(String(1000), nullable=False)
    date = Column(String(20))
    chat = relationship(Chat)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e