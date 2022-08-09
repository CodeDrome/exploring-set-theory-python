from types import MappingProxyType


symbols = MappingProxyType({ "emptySet": "∅",
                             "union": "∪",
                             "intersection": "∩",
                             "is_element_of": "∈",
                             "is_not_element_of": "∉",
                             "is_subset_of": "⊆",
                             "is_proper_subset_of": "⊂",
                             "is_not_subset_of": "⊄",
                             "is_superset_of": "⊇",
                             "is_proper_superset_of": "⊃",
                             "is_not_superset_of": "⊅",
                             "natural_numbers": "ℕ",
                             "integers": "ℤ",
                             "rational_numbers": "ℚ",
                             "real_numbers": "ℝ",
                             "complex_numbers": "ℂ",
                             "power_set": "ℙ",
                             "universal_set": "ξ",
                             # this is minuscule Greek letter xi
                             # minuscule zeta ζ. V, U or S are also used.
                             "cartesian_product": "×",
                             "set_difference": "\\",
                             "symmetric_difference": "Δ",
                             "cardinality": "|",
                             "complement": "'",})


def cardinality_string(set, setname):

    result = f"{symbols['cardinality']}{setname}{symbols['cardinality']} = {len(set)}"

    return result
