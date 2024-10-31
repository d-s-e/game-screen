from dataclasses import dataclass
from typing import Optional


@dataclass
class Layer:
    id: str
    name: str
    inverted: bool
    active: bool
    image_file: Optional[str] = None


@dataclass
class Preset:
    id: str
    name: str
    layers: dict[str, Layer]


# -------------------------------------------------------------------------

nemesis_lockdown_surface = Preset("nemesis_lockdown_surface", "Nemesis Lockdown Surface",
    {
        "section-red": Layer("section-red", "Red Section", False, False,
                             "layer_nemesis_lockdown_surface_section_red.png"),
        "section-blue": Layer("section-blue", "Blue Section", False, False,
                              "layer_nemesis_lockdown_surface_section_blue.png"),
        "section-yellow": Layer("section-yellow", "Yellow Section", False, False,
                                "layer_nemesis_lockdown_surface_section_yellow.png"),
        "section-elevator": Layer("section-elevator", "Elevator Section", False, False,
                                  "layer_nemesis_lockdown_surface_section_elevator.png"),
    }
)

# -------------------------------------------------------------------------

nemesis_lockdown = Preset("nemesis_lockdown", "Nemesis Lockdown",
    {
        "section-red": Layer("section-red", "Red Section", False, False,
                             "layer_nemesis_lockdown_section_red.png"),
        "section-blue": Layer("section-blue", "Blue Section", False, False,
                              "layer_nemesis_lockdown_section_blue.png"),
        "section-yellow": Layer("section-yellow", "Yellow Section", False, False,
                                "layer_nemesis_lockdown_section_yellow.png"),
        "section-elevator": Layer("section-elevator", "Elevator Section", False, False,
                                  "layer_nemesis_lockdown_section_elevator.png"),
    }
)

