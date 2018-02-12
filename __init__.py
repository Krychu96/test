# -*- coding: utf-8 -*-
"""
/***************************************************************************
 qqq
                                 A QGIS plugin
 qqq
                             -------------------
        begin                : 2018-02-12
        copyright            : (C) 2018 by qqq
        email                : qqq
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load qqq class from file qqq.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qqq import qqq
    return qqq(iface)
