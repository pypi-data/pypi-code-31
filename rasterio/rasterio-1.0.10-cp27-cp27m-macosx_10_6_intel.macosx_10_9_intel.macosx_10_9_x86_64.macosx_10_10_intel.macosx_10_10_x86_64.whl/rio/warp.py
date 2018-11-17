"""$ rio warp"""

import logging
from math import ceil, log
import warnings

import click
from cligj import format_opt

import rasterio
from rasterio.crs import CRS
from rasterio.env import setenv, GDALVersion
from rasterio.errors import CRSError
from rasterio.rio import options
from rasterio.rio.helpers import resolve_inout
from rasterio.transform import Affine
from rasterio.warp import (
    reproject, Resampling, SUPPORTED_RESAMPLING, transform_bounds,
    aligned_target, calculate_default_transform as calcdt)


# Improper usage of rio-warp can lead to accidental creation of
# extremely large datasets. We'll put a hard limit on the size of
# datasets and raise a usage error if the limits are exceeded.
MAX_OUTPUT_WIDTH = 100000
MAX_OUTPUT_HEIGHT = 100000


@click.command(short_help='Warp a raster dataset.')
@options.files_inout_arg
@options.output_opt
@format_opt
@click.option(
    '--like',
    type=click.Path(exists=True),
    help='Raster dataset to use as a template for obtaining affine '
         'transform (bounds and resolution), and crs.')
@click.option('--dst-crs', default=None,
              help='Target coordinate reference system.')
@options.dimensions_opt
@click.option(
    '--src-bounds',
    nargs=4, type=float, default=None,
    help="Determine output extent from source bounds: left bottom right top "
         ". Cannot be used with destination --bounds")
@click.option(
    '--bounds', '--dst-bounds', 'dst_bounds', nargs=4, type=float, default=None,
    help="Determine output extent from destination bounds: left bottom right top")
@options.resolution_opt
@click.option('--resampling',
              type=click.Choice([r.name for r in SUPPORTED_RESAMPLING]),
              default='nearest', help="Resampling method.",
              show_default=True)
@click.option('--src-nodata', default=None, show_default=True,
              type=float, help="Manually override source nodata")
@click.option('--dst-nodata', default=None, show_default=True,
              type=float, help="Manually override destination nodata")
@click.option('--threads', type=int, default=1,
              help='Number of processing threads.')
@click.option('--check-invert-proj/--no-check-invert-proj', default=True,
              help='Constrain output to valid coordinate region in dst-crs')
@click.option('--target-aligned-pixels/--no-target-aligned-pixels', default=False,
              help='align the output bounds based on the resolution')
@options.overwrite_opt
@options.creation_options
@click.pass_context
def warp(ctx, files, output, driver, like, dst_crs, dimensions, src_bounds,
         dst_bounds, res, resampling, src_nodata, dst_nodata, threads,
         check_invert_proj, overwrite, creation_options,
         target_aligned_pixels):
    """
    Warp a raster dataset.

    If a template raster is provided using the --like option, the
    coordinate reference system, affine transform, and dimensions of
    that raster will be used for the output.  In this case --dst-crs,
    --bounds, --res, and --dimensions options are not applicable and
    an exception will be raised.

    \b
        $ rio warp input.tif output.tif --like template.tif

    The output coordinate reference system may be either a PROJ.4 or
    EPSG:nnnn string,

    \b
        --dst-crs EPSG:4326
        --dst-crs '+proj=longlat +ellps=WGS84 +datum=WGS84'

    or a JSON text-encoded PROJ.4 object.

    \b
        --dst-crs '{"proj": "utm", "zone": 18, ...}'

    If --dimensions are provided, --res and --bounds are not applicable and an
    exception will be raised.
    Resolution is calculated based on the relationship between the
    raster bounds in the target coordinate system and the dimensions,
    and may produce rectangular rather than square pixels.

    \b
        $ rio warp input.tif output.tif --dimensions 100 200 \\
        > --dst-crs EPSG:4326

    If --bounds are provided, --res is required if --dst-crs is provided
    (defaults to source raster resolution otherwise).

    \b
        $ rio warp input.tif output.tif \\
        > --bounds -78 22 -76 24 --res 0.1 --dst-crs EPSG:4326

    """
    output, files = resolve_inout(
        files=files, output=output, overwrite=overwrite)

    resampling = Resampling[resampling]  # get integer code for method

    if not len(res):
        # Click sets this as an empty tuple if not provided
        res = None
    else:
        # Expand one value to two if needed
        res = (res[0], res[0]) if len(res) == 1 else res

    if target_aligned_pixels:
        if not res:
            raise click.BadParameter(
                '--target-aligned-pixels requires a specified resolution')
        if src_bounds or dst_bounds:
            raise click.BadParameter(
                '--target-aligned-pixels cannot be used with '
                '--src-bounds or --dst-bounds')

    # Check invalid parameter combinations
    if like:
        invalid_combos = (dimensions, dst_bounds, dst_crs, res)
        if any(p for p in invalid_combos if p is not None):
            raise click.BadParameter(
                "--like cannot be used with any of --dimensions, --bounds, "
                "--dst-crs, or --res")

    elif dimensions:
        invalid_combos = (dst_bounds, res)
        if any(p for p in invalid_combos if p is not None):
            raise click.BadParameter(
                "--dimensions cannot be used with --bounds or --res")

    with ctx.obj['env']:
        setenv(CHECK_WITH_INVERT_PROJ=check_invert_proj)

        with rasterio.open(files[0]) as src:
            l, b, r, t = src.bounds
            out_kwargs = src.profile.copy()
            out_kwargs['driver'] = driver

            # Sort out the bounds options.
            if src_bounds and dst_bounds:
                raise click.BadParameter(
                    "--src-bounds and destination --bounds may not be "
                    "specified simultaneously.")

            if like:
                with rasterio.open(like) as template_ds:
                    dst_crs = template_ds.crs
                    dst_transform = template_ds.transform
                    dst_height = template_ds.height
                    dst_width = template_ds.width

            elif dst_crs is not None:
                try:
                    dst_crs = CRS.from_string(dst_crs)
                except ValueError as err:
                    raise click.BadParameter(
                        str(err), param='dst_crs', param_hint='dst_crs')

                if dimensions:
                    # Calculate resolution appropriate for dimensions
                    # in target.
                    dst_width, dst_height = dimensions
                    bounds = src_bounds or src.bounds
                    try:
                        xmin, ymin, xmax, ymax = transform_bounds(
                            src.crs, dst_crs, *bounds)
                    except CRSError as err:
                        raise click.BadParameter(
                            str(err), param='dst_crs', param_hint='dst_crs')
                    dst_transform = Affine(
                        (xmax - xmin) / float(dst_width),
                        0, xmin, 0,
                        (ymin - ymax) / float(dst_height),
                        ymax
                    )

                elif src_bounds or dst_bounds:
                    if not res:
                        raise click.BadParameter(
                            "Required when using --bounds.",
                            param='res', param_hint='res')

                    if src_bounds:
                        try:
                            xmin, ymin, xmax, ymax = transform_bounds(
                                src.crs, dst_crs, *src_bounds)
                        except CRSError as err:
                            raise click.BadParameter(
                                str(err), param='dst_crs',
                                param_hint='dst_crs')
                    else:
                        xmin, ymin, xmax, ymax = dst_bounds

                    dst_transform = Affine(res[0], 0, xmin, 0, -res[1], ymax)
                    dst_width = max(int(ceil((xmax - xmin) / res[0])), 1)
                    dst_height = max(int(ceil((ymax - ymin) / res[1])), 1)

                else:
                    try:
                        if src.transform.is_identity and src.gcps:
                            src_crs = src.gcps[1]
                            kwargs = {'gcps': src.gcps[0]}
                        else:
                            src_crs = src.crs
                            kwargs = src.bounds._asdict()
                        dst_transform, dst_width, dst_height = calcdt(
                            src_crs, dst_crs, src.width, src.height,
                            resolution=res, **kwargs)
                    except CRSError as err:
                        raise click.BadParameter(
                            str(err), param='dst_crs', param_hint='dst_crs')

            elif dimensions:
                # Same projection, different dimensions, calculate resolution.
                dst_crs = src.crs
                dst_width, dst_height = dimensions
                l, b, r, t = src_bounds or (l, b, r, t)
                dst_transform = Affine(
                    (r - l) / float(dst_width),
                    0, l, 0,
                    (b - t) / float(dst_height),
                    t
                )

            elif src_bounds or dst_bounds:
                # Same projection, different dimensions and possibly
                # different resolution.
                if not res:
                    res = (src.transform.a, -src.transform.e)

                dst_crs = src.crs
                xmin, ymin, xmax, ymax = (src_bounds or dst_bounds)
                dst_transform = Affine(res[0], 0, xmin, 0, -res[1], ymax)
                dst_width = max(int(ceil((xmax - xmin) / res[0])), 1)
                dst_height = max(int(ceil((ymax - ymin) / res[1])), 1)

            elif res:
                # Same projection, different resolution.
                dst_crs = src.crs
                dst_transform = Affine(res[0], 0, l, 0, -res[1], t)
                dst_width = max(int(ceil((r - l) / res[0])), 1)
                dst_height = max(int(ceil((t - b) / res[1])), 1)

            else:
                dst_crs = src.crs
                dst_transform = src.transform
                dst_width = src.width
                dst_height = src.height

            if target_aligned_pixels:
                dst_transform, dst_width, dst_height = aligned_target(dst_transform, dst_width, dst_height, res)

            # If src_nodata is not None, update the dst metadata NODATA
            # value to src_nodata (will be overridden by dst_nodata if it is not None
            if src_nodata is not None:
                # Update the dst nodata value
                out_kwargs.update({
                    'nodata': src_nodata
                })

            # Validate a manually set destination NODATA value
            # against the input datatype.
            if dst_nodata is not None:
                if src_nodata is None and src.meta['nodata'] is None:
                    raise click.BadParameter(
                        "--src-nodata must be provided because dst-nodata is not None")
                else:
                    # Update the dst nodata value
                    out_kwargs.update({'nodata': dst_nodata})

            # When the bounds option is misused, extreme values of
            # destination width and height may result.
            if (dst_width < 0 or dst_height < 0 or
                    dst_width > MAX_OUTPUT_WIDTH or
                    dst_height > MAX_OUTPUT_HEIGHT):
                raise click.BadParameter(
                    "Invalid output dimensions: {0}.".format(
                        (dst_width, dst_height)))

            out_kwargs.update({
                'crs': dst_crs,
                'transform': dst_transform,
                'width': dst_width,
                'height': dst_height
            })

            # Adjust block size if necessary.
            if ('blockxsize' in out_kwargs and
                    dst_width < out_kwargs['blockxsize']):
                del out_kwargs['blockxsize']
            if ('blockysize' in out_kwargs and
                    dst_height < out_kwargs['blockysize']):
                del out_kwargs['blockysize']

            out_kwargs.update(**creation_options)

            with rasterio.open(output, 'w', **out_kwargs) as dst:
                reproject(
                    source=rasterio.band(src, list(range(1, src.count + 1))),
                    destination=rasterio.band(
                        dst, list(range(1, src.count + 1))),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    src_nodata=src_nodata,
                    dst_transform=out_kwargs['transform'],
                    dst_crs=out_kwargs['crs'],
                    dst_nodata=dst_nodata,
                    resampling=resampling,
                    num_threads=threads)
