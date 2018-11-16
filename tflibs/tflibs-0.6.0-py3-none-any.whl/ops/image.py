"""
    Image ops
    ~~~~~~~~~
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf


def normalize(images):
    images = tf.image.convert_image_dtype(images, tf.float32)
    # [0, 1] --> [-1, 1]
    images -= 0.5
    images *= 2.

    return images


def decode_image(encoded_image, image_shape, image_format=None, conditional=False):
    # TODO: Fuse decode and crop
    if conditional:
        image = tf.cond(tf.equal(image_format, 'raw', name='is_raw'),
                        true_fn=lambda: tf.decode_raw(encoded_image, tf.uint8),
                        false_fn=lambda: tf.image.decode_image(encoded_image),
                        name='decoded_image')
    else:
        image = tf.image.decode_image(encoded_image)
    image = tf.reshape(image, image_shape)

    return image


def normalize_images(images):
    with tf.name_scope('normalize_images', values=[images]):
        images -= tf.reduce_min(images)
        return images / tf.reduce_max(images)


def concat_images(*list_images):
    with tf.name_scope('concat_images', values=list_images):
        list_images = list(map(normalize_images, list_images))

        return tf.concat(list_images, 2)


def flat_images(images):
    with tf.name_scope('flat_images', values=[images]):
        shape = images.shape.as_list()
        return tf.reshape(images, [shape[0] * shape[1]] + shape[2:])
