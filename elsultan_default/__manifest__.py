##############################################################################
#
#    Copyright (C) 2022  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   le agregamos esto
##############################################################################

{
    "name": "elsultan",
    "version": "17.0.1.0.0",
    "category": "Tools",
    "summary": "Odoov17 CE",
    "author": "Gabriel-Rivas",
    "website": "https://github.com/Gabriel-Rivas/cl-elsultan",
    "license": "AGPL-3",
    "depends": [],
    "installable": True,
    # manifest version, if omitted it is backward compatible
    "env-ver": "2",
    # if Enterprise it installs in a different directory than community
    "odoo-license": "CE",
    # Config to write in odoo.conf
    "config": [
        "workers = 0",
        "admin_password = admin",
    ],
    "port": "8069",
    "git-repos": [
        "https://github.com/Gabriel-Rivas/cl-elsultan.git",
        ##'git@github.com:jobiols/odoo-jeo-ce.git',
        ##'https://github.com/regaby/odoo-custom.git -b 17.0',
        ## localización
        ##'https://github.com/odoo-mastercore/odoo-venezuela.git -b 16.0',

        ## Addons
        "https://github.com/CybroOdoo/CybroAddons.git -b 17.0",
        "https://github.com/Yenthe666/auto_backup -b 17.0",
    ],
    # list of images to use in the form 'name image-url'
    "docker-images": [
        "odoo jobiols/odoo-jeo:17.0",
        "postgres postgres:15.1-alpine",
    ],
}
