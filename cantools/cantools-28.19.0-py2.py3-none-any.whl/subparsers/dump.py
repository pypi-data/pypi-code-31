from __future__ import print_function

from .. import database
from ..database.utils import format_and
from ..j1939 import is_pdu_format_1
from ..j1939 import frame_id_unpack
from ..j1939 import pgn_pack


def _print_j1939_frame_id(message):
    unpacked = frame_id_unpack(message.frame_id)

    print('      Priority:       {}'.format(unpacked.priority))

    if is_pdu_format_1(unpacked.pdu_format):
        pdu_format = 'PDU 1'
        pdu_specific = 0
        destination = '0x{:02x}'.format(unpacked.pdu_specific)
    else:
        pdu_format = 'PDU 2'
        pdu_specific = unpacked.pdu_specific
        destination = 'All'

    print('      PGN:            0x{:05x}'.format(
        pgn_pack(unpacked.reserved,
                 unpacked.data_page,
                 unpacked.pdu_format,
                 pdu_specific)))
    print('      Source:         0x{:02x}'.format(unpacked.source_address))
    print('      Destination:    {}'.format(destination))
    print('      Format:         {}'.format(pdu_format))


def _do_dump(args, _version):
    dbase = database.load_file(args.database,
                               encoding=args.encoding,
                               strict=not args.no_strict)

    print('================================= Messages =================================')
    print()
    print('  ' + 72 * '-')

    for message in dbase.messages:
        cycle_time = message.cycle_time
        signal_choices_string = message.signal_choices_string()

        if cycle_time is None:
            cycle_time = '-'

        if len(message.senders) == 0:
            message.senders.append('-')

        print()
        print('  Name:       {}'.format(message.name))
        print('  Id:         0x{:x}'.format(message.frame_id))

        if message.protocol == 'j1939':
            _print_j1939_frame_id(message)

        print('  Length:     {} bytes'.format(message.length))
        print('  Cycle time: {} ms'.format(cycle_time))
        print('  Senders:    {}'.format(format_and(message.senders)))
        print('  Layout:')
        print()
        print('\n'.join([
            ('    ' + line).rstrip()
            for line in message.layout_string().splitlines()
        ]))
        print()
        print('  Signal tree:')
        print()
        print('\n'.join([
            ('    ' + line).rstrip()
            for line in message.signal_tree_string().splitlines()
        ]))
        print()

        if signal_choices_string:
            print('  Signal choices:')
            print('\n'.join([
                ('    ' + line).rstrip()
                for line in signal_choices_string.splitlines()
            ]))
            print()

        print('  ' + 72 * '-')


def add_subparser(subparsers):
    dump_parser = subparsers.add_parser(
        'dump',
        description='Dump given database in a human readable format.')
    dump_parser.add_argument(
        '-e', '--encoding',
        default='utf-8',
        help='File encoding (default: utf-8).')
    dump_parser.add_argument(
        '--no-strict',
        action='store_true',
        help='Skip database consistency checks.')
    dump_parser.add_argument(
        'database',
        help='Database file.')
    dump_parser.set_defaults(func=_do_dump)
