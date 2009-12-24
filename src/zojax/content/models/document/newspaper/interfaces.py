##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope import interface, schema
from zojax.content.type.interfaces import IContentView
from zojax.content.models.document.interfaces import _


class INewspaperModel(interface.Interface):
    """ Newspaper model """

    primaryImage = schema.Choice(
        title = _(u'Primary image'),
        vocabulary = 'content.attachments.images',
        required = False)

    showTitles = schema.Bool(
        title = _('Show images titles'),
        default = False,
        missing_value = False,
        required = False)

    additionalImages = schema.List(
        title = _(u'Additional images'),
        value_type = schema.Choice(vocabulary='content.attachments.images'),
        default = [],
        missing_value = [],
        required = False)

    attachments = schema.List(
        title = _(u'Document attachments'),
        value_type = schema.Choice(vocabulary='content.attachments.all'),
        default = [],
        missing_value = [],
        required = False)


class INewspaperModelView(IContentView):
    """ Newspaper model view """
