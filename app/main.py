"""
Private License (Library Management System)

This script is privately licensed and confidential. It is not intended for
public distribution or use without explicit permission from the owner.

All rights reserved (c) 2024.
"""

__author__ = "Premnath Palanichamy"
__copyright__ = "Copyright 2024, qtools"
__license__ = "Refer Terms and Conditions"
__version__ = "1.0"
__maintainer__ = "Premnath"
__email__ = "creativepremnath@gmail.com"
__status__ = "Development"
__desc__ = "Main Program of the Library Management System"


# Importing necessary modules
from fastapi import FastAPI,Response,HTTPException,status
from fastapi.middleware.cors import CORSMiddleware

from app.routers import books, user  # Importing simple module for demonstration purposes only. Replace with your actual modules.


app = FastAPI(
    title="Library Management System",
    description="Library Management System for College",
    version="1.0.0",
    swagger_ui_parameters={"syntaxHighlight": True}
)

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router)
app.include_router(books.router)