"""
#   Copyright 2025 Matthew Ralston
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""

import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


logger = logging.getLogger(__file__)


# postgresql://user:password@localhost/dbname
# if "SQLALCHEMY_DATABASE_URI" in os.environ:
#     SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
# else:
#     raise OSError("Cannot retrieve database URI from environment variable 'SQLALCHEMY_DATABASE_URI...")
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
if SQLALCHEMY_DATABASE_URI is None:
    logger.warn("Could not create database connection from unset environment variable...")
    logger.warn("Defaulting to development database URI...")
    SQLALCHEMY_DATABASE_URI = "sqlite+libsql:///example.db"
elif SQLALCHEMY_DATABASE_URI is not None:
    logger.info("Retrieved database URI from environment variable...")


engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


