def pixel_to_angle(
        x_pixel,
        image_width):

    MAX_ANGLE = 30.0

    return (
        (
            x_pixel -
            image_width / 2
        )
        /
        (
            image_width / 2
        )
    ) * MAX_ANGLE
