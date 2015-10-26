# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Hide Left Navigation Panel For Full Screen View",
    "version": "1.0",
    "author": "Brand Equity Solutions.",
    "website": "http://erp.besplatform.com/",
    "version": "1.0",
    "catagory": "Tools",
    "complexity": "easy",
    "summary": "Odoo Full screen View by hiding left navigation panel",
    "description": """
            This module enables the toggle button at the side of left navigation(sub menus) to hide and show full screen.
    """,
    "depends": ["web"],
    "data": ["views/web_left_panel.xml"],
    "installable": True,
    "auto_install": False
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
