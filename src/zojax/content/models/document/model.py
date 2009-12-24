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
from zope import interface
from zope.component import getMultiAdapter
from zojax.content.model.model import ViewModel
from zojax.content.type.interfaces import IContentView, IContentContainer


class ModelView(object):

    def __init__(self, context, request):
        super(ModelView, self).__init__(context.__parent__, request)

        self.model = context

    def update(self):
        self.contentView = getMultiAdapter(
            (self.context, self.request), IContentView)

        self.contentView.update()

    def render(self):
        return self.contentView.render()
