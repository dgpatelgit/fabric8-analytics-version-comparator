# Copyright © 2018 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Pavel Tisnovsky <ptisnovs@redhat.com>


"""Tests for the module item_object."""


import pytest
from f8a_version_comparator.item_object import *


def test_integer_item():
    """Test the IntegerItem class."""
    i1 = IntegerItem("1")
    assert str(i1) == "1"

    # actually the to_string() method is not needed much
    assert str(i1) == i1.to_string()


def test_integer_item_compare_to():
    """Test the IntegerItem.compare_to method."""
    i1 = IntegerItem("1")
    i2 = IntegerItem("2")
    assert i1.compare_to(i2) == -1
    assert i2.compare_to(i1) == 1

    i3 = StringItem("string", False)
    assert i1.compare_to(i3) == 1

    i4 = ListItem()
    assert i1.compare_to(i4) == 1

    assert i1.compare_to(None) == 1

    # try to compare integer with uncomparable item
    with pytest.raises(ValueError) as e:
        i1.compare_to("string")


def test_string_item():
    """Test the StringItem class."""
    i1 = StringItem("string", False)
    assert str(i1) == "string"

    # actually the to_string() method is not needed much
    assert str(i1) == i1.to_string()


def test_string_item_compare_to():
    """Test the StringItem.compare_to method."""
    i1 = StringItem("string", False)
    i2 = IntegerItem("2")
    assert i1.compare_to(i2) == -1
    assert i2.compare_to(i1) == 1

    i3 = StringItem("string", False)
    assert i1.compare_to(i3) == 0

    i4 = ListItem()
    assert i1.compare_to(i4) == -1

    assert i1.compare_to(None) == 1

    # try to compare string with uncomparable item
    with pytest.raises(ValueError) as e:
        i1.compare_to("string")


def test_list_item_compare_to():
    """Test the ListItem.compare_to method."""
    i1 = ListItem()

    i2 = IntegerItem("2")
    assert i1.compare_to(i2) == -1

    i3 = StringItem("string", False)
    assert i1.compare_to(i3) == 1

    i4 = ListItem()
    assert i1.compare_to(i4) == 0

    # try to compare list with uncomparable item
    with pytest.raises(ValueError) as e:
        i1.compare_to("string")


if __name__ == '__main__':
    test_integer_item()
    test_integer_item_compare_to()
    test_string_item()
    test_string_item_compare_to()
    test_list_item_compare_to()
