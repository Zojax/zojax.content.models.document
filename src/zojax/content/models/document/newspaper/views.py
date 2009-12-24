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
from zope.component import getUtility, queryMultiAdapter
from zope.size.interfaces import ISized
from zope.app.component.hooks import getSite
from zope.app.intid.interfaces import IIntIds
from zope.traversing.browser import absoluteURL
from zojax.content.attachment.interfaces import IImage, IAttachmentsExtension


class Image(object):

    def getImage(self):
        context = self.context
        extension = IAttachmentsExtension(context)

        image = extension.get(self.__parent__.model.primaryImage)

        if IImage.providedBy(image) and image:
            preview = image.preview.generatePreview(100, 100)

            url = '%s/@@content.attachment/%s'%(
                absoluteURL(getSite(), self.request),
                getUtility(IIntIds).queryId(image))

            return {'name': image.__name__,
                    'title': image.title or image.__name__,
                    'url': url,
                    'purl': '%s/preview/100x100'%url}


class Images(object):

    def update(self):
        super(Images, self).update()

        self.model = self.__parent__.model
        self.showTitles = self.model.showTitles

    def getImages(self):
        context = self.context
        extension = IAttachmentsExtension(context)
        url = absoluteURL(context, self.request)

        ids = getUtility(IIntIds)
        url = '%s/@@content.attachment'%absoluteURL(getSite(), self.request)

        for imageId in self.model.additionalImages:
            image = extension.get(imageId)

            if IImage.providedBy(image) and image:
                preview = image.preview.generatePreview(100, 100)

                img_url = '%s/%s'%(url, ids.getId(image))

                yield {'name': imageId,
                       'title': image.title or imageId,
                       'url': img_url,
                       'purl': '%s/preview/100x100'%img_url}

class Attachments(object):

    def update(self):
        super(Attachments, self).update()

        self.model = self.__parent__.model

    def getAttachments(self):
        context = self.context
        request = self.request
        extension = IAttachmentsExtension(context)

        ids = getUtility(IIntIds)
        url = '%s/@@content.attachment'%absoluteURL(getSite(), self.request)

        attachments = []
        for aId in self.model.attachments:
            attach = extension.get(aId)
            aurl = '%s/content.attachments/%s'%(url, ids.getId(attach))

            size = ISized(attach)
            if size.sizeForSorting()[0] is not None:
                size = size.sizeForDisplay()
            else:
                size = ''

            attachments.append(
                {'name': aId,
                 'title': attach.title or aId,
                 'description': attach.description,
                 'url': aurl,
                 'size': size,
                 'icon': queryMultiAdapter((attach, request), name='zmi_icon')})

        return attachments
