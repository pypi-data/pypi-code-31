#
# Copyright (c) 2011, 2015
#  Adam Tauno Williams <awilliam@whitemice.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE
#
# from sqlalchemy import and_
from coils.core import Attachment, BLOBManager, CoilsException, Command
from keymap import COILS_ATTACHMENT_KEYMAP
from command import AttachmentCommand


class CreateAttachment(Command, AttachmentCommand):
    __domain__ = "attachment"
    __operation__ = "new"

    def __init__(self):
        Command.__init__(self)

    def parse_parameters(self, **params):
        Command.parse_parameters(self, **params)

        self.values = {}

        # MIME-type is a required value of attachment
        self.values['mimetype'] = params.get(
            'mimetype', 'application/octet-stream'
        )

        # context_id of the attachments gets set to context which created it
        self.values['context_id'] = params.get(
            'context_id', self._ctx.account_id
        )

        # related_id is the entity to which the attachment is 'attached'
        if ('entity' in params):
            self.values['related_id'] = params.get('entity').object_id
        else:
            self.values['related_id'] = params.get('related_id', None)

        # Optional values
        self.values['kind'] = params.get('kind', None)
        self.values['expiration'] = params.get('expiration', None)
        self.values['webdav_uid'] = params.get('name', None)

        # How were we provided the intended content?
        if ('data' in params):
            # Creating attachment from in-memory value
            self.in_ = None
            self.data_ = params['data']
        elif ('filename' in params):
            # Creating attachment from absolute path (DANGEROUS!)
            self.in_ = open(params['filename'], 'rb')
        elif ('handle' in params):
            # Creating attachment from stream (RECOMMENDED)
            self.in_ = params['handle']
        else:
            raise CoilsException('No attachment data or source specified')

    def run(self):
        """
        Create an attachment entity and store the related content.
        """

        attachment = Attachment()
        attachment.take_values(self.values, COILS_ATTACHMENT_KEYMAP)
        attachment.created = self._ctx.get_utctime()
        attachment.uuid = self.generate_attachment_id()

        try:
            close_input = False
            out_ = BLOBManager.Open(
                self.attachment_text_path(attachment),
                'w',
                encoding='binary',
                create=True,
            )
            if not self.in_:
                """
                Data was passed as a string/block so we need to write it to a
                scratch file so that can be copied into the attachment storage.
                All data goes into attachment storage from a stream as this
                is how we determine octet size and calculate the checksum.
                """
                self.in_ = BLOBManager.ScratchFile()
                close_input = True
                if self.data_:
                    self.in_.write(self.data_)
            # Rewind the input stream
            self.in_.seek(0)
            # Put the data in, return the checksum and size
            attachment.checksum, attachment.size = self.write(self.in_, out_)
            BLOBManager.Close(out_)
            if close_input:
                BLOBManager.Close(self.in_)
        except Exception as exc:
            self.log.exception(exc)
            raise CoilsException('Failure to allocate attachment contents')

        self._ctx.db_session().add(attachment)

        self._result = attachment
