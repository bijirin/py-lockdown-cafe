from app.cafe.cafe import Cafe
from app.cafe.errors import (
    NotWearingMaskError,
    VaccineError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    message = ""
    masks_to_buy = 0
    error_flag = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            message = "All friends should be vaccinated"
            error_flag = True
        except NotWearingMaskError:
            masks_to_buy += 1
            error_flag = True

    if masks_to_buy > 0:
        message = f"Friends should buy {masks_to_buy} masks"

    if not error_flag:
        message = f"Friends can go to {cafe.name}"

    return message
