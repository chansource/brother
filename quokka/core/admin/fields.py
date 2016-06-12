# coding: utf-8
import random
import sys

from werkzeug.datastructures import FileStorage
from flask import current_app
from flask.ext.admin import form
from flask.ext.admin.form.upload import ImageUploadInput

from quokka.core.models.subcontent import SubContent, SubContentPurpose
from quokka.modules.media.models import Image

import logging

if sys.version_info.major == 3:
    unicode = lambda x: u'{}'.format(x)  # noqa  # flake8: noqa

logger = logging.getLogger()

class ThumbWidget(ImageUploadInput):
    empty_template = ""
    data_template = ('<div class="image-thumbnail">'
                     ' <img %(image)s>'
                     '</div>')

    @staticmethod
    def get_url(field):
        '''
        This meethod is not used, but is here for compatibility
        '''
        # if field.thumbnail_size:
        #     filename = field.thumbnail_fn(field.data)
        # else:
        #     filename = field.data
        #
        # if field.url_relative_path:
        #     filename = urljoin(field.url_relative_path, filename)
        return field.data


class ThumbField(form.ImageUploadField):
    widget = ThumbWidget()


class ImageUploadField(form.ImageUploadField):
    def is_file_allowed(self, filename):
        extensions = self.allowed_extensions  # noqa
        if isinstance(extensions, (str, unicode)) and extensions.isupper():
            items = current_app.config.get(extensions, extensions)
            merged_items = [
                item.lower() for item in items
            ] + [item.upper() for item in items]
            self.allowed_extensions = merged_items
        return super(ImageUploadField, self).is_file_allowed(filename)

    def _save_file(self, data, filename):
        '''
        将原版ImageUploadField._save_file函数内容拷贝过来，加日志DEBUG
        '''
        import os.path as op

        path = self._get_path(filename)
        logger.debug("path %s" % path)

        if not op.exists(op.dirname(path)):
            os.makedirs(os.path.dirname(path), self.permission | 0o111)

        # Figure out format
        filename, format = self._get_save_format(filename, self.image)
        logger.debug("filename %s format %s" % (filename, format))

        if self.image and (self.image.format != format or self.max_size):
            if self.max_size:
                image = self._resize(self.image, self.max_size)
            else:
                image = self.image

            self._save_image(image, self._get_path(filename), format)
        else:
            data.seek(0)
            data.save(self._get_path(filename))

        self._save_thumbnail(data, filename, format)

        logger.debug("path %s" % filename)
        return filename


class ContentImageField(ImageUploadField):
    def populate_obj(self, obj, name):
        pass

    def save_contents(self, obj):
        # field = getattr(obj, name, None)
        # if field:
        #     # If field should be deleted, clean it up
        #     if self._should_delete:
        #         self._delete_file(field)
        #         setattr(obj, name, None)
        #         return

        new_image = Image(
            title=u"Image: {0}".format(obj.title),
            slug=u"{0}-{1}".format(obj.slug, random.getrandbits(8)),
            channel=Image.get_default_channel(),
            published=True
        )
        if self.data and isinstance(self.data, FileStorage):
            # if field:
            #     self._delete_file(field)

            filename = self.generate_name(new_image, self.data)
            filename = self._save_file(self.data, filename)

            setattr(new_image, 'path', filename)

            new_image.save()

            if obj.contents.filter(identifier='mainimage'):
                purpose = SubContentPurpose.objects.get(identifier='image')
            else:
                purpose = SubContentPurpose.objects.get(
                    identifier='mainimage'
                )

            subcontent = SubContent(
                content=new_image,
                purpose=purpose,
            )

            obj.contents.append(subcontent)
            obj.save()
