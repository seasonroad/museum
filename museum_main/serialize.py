# encoding: utf-8
import mimetypes
import re
import os
from flask import url_for
#from django.core.urlresolvers import reverse


def order_name(name):
    """order_name -- Limit a text to 20 chars length, if necessary strips the
    middle of the text and substitute it for an ellipsis.

    name -- text to be limited.

    """
    name = re.sub(r'^.*/', '', name)
    if len(name) <= 20:
        return name
    return name[:10] + "..." + name[-7:]


def serialize(instance):
    """serialize -- Serialize a Picture instance into a dict.

    instance -- Picture instance
    file_attr -- attribute name that contains the FileField or ImageField

    """
    obj = instance
    d= {
        'url': obj.url,
        'name': order_name(obj.name),
        'type': mimetypes.guess_type(obj.file_path_ori)[0] or 'image/png',
        'thumbnailUrl': obj.thumb_url,
        'size': obj.size,
        #'deleteUrl': reverse('upload-delete', args=[instance.pk]),
        'deleteUrl': url_for('picture_delete', values=obj.id),
        'deleteType': 'DELETE',
    }
    print d
    return d


