#!/usr/bin/env python3
import typing


class DecisionNode(typing.NamedTuple):
    property: str
    property_true: typing.Optional[typing.Self]
    property_false: typing.Optional[typing.Self]


if __name__ == "__main__":
    female_node = DecisionNode("skin tone == dark", None, None)
    male_node = DecisionNode("eye color == brown", None, None)
    root = DecisionNode("gender == female", property_true=female_node, property_false=male_node)
