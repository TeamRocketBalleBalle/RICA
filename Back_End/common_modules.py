import html
import os
from colorama import Fore
from Database.Database_connection import get_user_type , get_doc_names
from flask import Blueprint, session, render_template, current_app
from Back_End.login import login_required