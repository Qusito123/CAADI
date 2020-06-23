from flask import flash, redirect, render_template, url_for

from . import inventory
from ..models import Books, Dvds, Cds
from .. import db

@inventory.route('/inventory', methods=['GET', 'POST'])
def inventory():
    """
    Handle request to the /inventory route
    """

    