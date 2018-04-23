#    pydifact - a python edifact library
#    Copyright (C) 2017  Christian González
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pydifact.Message import Message
import unittest
import os


class CompleteTest(unittest.TestCase):

    def setUp(self):
        self.path = os.path.dirname(os.path.realpath(__file__)) + "/data"

    def test1(self):
        self._testFormat("{}/wikipedia.edi".format(self.path))

    def test2(self):
        self._testFormat("{}/order.edi".format(self.path))

    def _testFormat(self, file):

        output = str(Message.from_file(file))
        message = open(file).read()
        expected = message.replace("\n", "")
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
