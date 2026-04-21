from app.cafe.cafe import Cafe
from app.cafe.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError,
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (
            NotVaccinatedError("Visitor is not vaccinated."),
            OutdatedVaccineError("Visitor's vaccine is outdated.")
        ):
            return "All friends should be vaccinated"
        except NotWearingMaskError("Visitor is not wearing a mask."):
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
