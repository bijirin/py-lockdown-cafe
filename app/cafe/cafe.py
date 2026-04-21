import datetime
from app.cafe.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        error_flag = False
        if not ("vaccine" in visitor):
            error_flag = True
            raise NotVaccinatedError("Visitor is not vaccinated.")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            error_flag = True
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")

        if not visitor["wearing_a_mask"]:
            error_flag = True
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        if not error_flag:
            return f"Welcome to {self.name}"
