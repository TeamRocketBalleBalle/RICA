import html
import os
from colorama import Fore
from Database.Database_connection import get_user_type
from flask import Blueprint, session, render_template, current_app