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
import os, unittest, doctest
from zope import interface
from zope.app.schema import vocabulary
from zope.app.testing.functional import getRootFolder
from zope.app.intid import IntIds
from zope.app.intid.interfaces import IIntIds
from zojax.cache.testing import setUpCache, tearDownCache
from zojax.content.model.tests import content
from zojax.filefield.testing import ZCMLLayer, FunctionalDocFileSuite
from zojax.content.models.document.interfaces import IDocumentModelsAware


zojaxDocumentModelsLayer = ZCMLLayer(
    os.path.join(os.path.split(__file__)[0], 'ftesting.zcml'),
    __name__, 'zojaxDocumentModelsLayer', allow_teardown=True)


def setUp(test):
    root = getRootFolder()

    root['ids'] = IntIds()
    root.getSiteManager().registerUtility(root['ids'], IIntIds)

    if 'content' not in root:
        root['content'] = content.MyContent(u'My Content')

    if 'content1' not in root:
        root['content1'] = content.MyContent(u'My Content')

    if 'container' not in root:
        root['container'] = content.MyContentContainer(u'My Content Container')
        root['container']['content1'] = content.MyContent(u'My Content 1')
        root['container']['content2'] = content.MyContent(u'My Content 2')
        root['container']['content3'] = content.MyContent(u'My Content 3')

    setUpCache()

def tearDown(test):
    tearDownCache()


def test_suite():
    plain = FunctionalDocFileSuite(
        "plain.txt", setUp=setUp, tearDown=tearDown)
    plain.layer = zojaxDocumentModelsLayer

    newspaper = FunctionalDocFileSuite(
        "newspaper.txt", setUp=setUp, tearDown=tearDown)
    newspaper.layer = zojaxDocumentModelsLayer

    documentation = FunctionalDocFileSuite(
        "documentation.txt", setUp=setUp, tearDown=tearDown)
    documentation.layer = zojaxDocumentModelsLayer

    return unittest.TestSuite((plain, newspaper, documentation))
