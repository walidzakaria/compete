import data_wizard
from .models import GeneralQuestion, PenaltyQuestion, PressureQuestion, WheelQuestion, OtherQuestion


data_wizard.register(GeneralQuestion)
data_wizard.register(PenaltyQuestion)
data_wizard.register(PressureQuestion)
data_wizard.register(WheelQuestion)
data_wizard.register(OtherQuestion)
