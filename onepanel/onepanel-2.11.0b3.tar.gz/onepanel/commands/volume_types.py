import click

from onepanel.commands.base import APIViewController
from onepanel.commands.login import login_required


class VolumeTypeViewController(APIViewController):

    def __init__(self, conn):
        APIViewController.__init__(self,conn)


@click.group(name='volume-types', help='Available volume types')
@click.pass_context
def volume_types(ctx):
    ctx.obj['view_controller'] = VolumeTypeViewController(ctx.obj['connection'])


@volume_types.command(
    'list',
    help='Show available volume types and their IDs'
)
@click.pass_context
@login_required
def list_volume_types(ctx):

    vc = ctx.obj['view_controller']

    items = vc.list(params='/volume_types')
    vc.print_items(items, fields=['uid', 'name'], field_names=['ID', 'SPECS'])

