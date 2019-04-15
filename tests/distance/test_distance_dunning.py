# -*- coding: utf-8 -*-

# Copyright 2019 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.tests.distance.test_distance_dunning.

This module contains unit tests for abydos.distance.Dunning
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import Dunning


class DunningTestCases(unittest.TestCase):
    """Test Dunning functions.

    abydos.distance.Dunning
    """

    cmp = Dunning()
    cmp_no_d = Dunning(alphabet=0)

    def test_dunning_sim(self):
        """Test abydos.distance.Dunning.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), 1.0)
        self.assertEqual(self.cmp.sim('a', ''), 0.0)
        self.assertEqual(self.cmp.sim('', 'a'), 0.0)
        self.assertEqual(self.cmp.sim('abc', ''), 0.0)
        self.assertEqual(self.cmp.sim('', 'abc'), 0.0)
        self.assertEqual(self.cmp.sim('abc', 'abc'), 1.0)
        self.assertAlmostEqual(
            self.cmp.sim('abcd', 'efgh'), 0.0010935459910939103
        )

        self.assertAlmostEqual(self.cmp.sim('Nigel', 'Niall'), 0.3536159877)
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Nigel'), 0.3536159877)
        self.assertAlmostEqual(self.cmp.sim('Colin', 'Coiln'), 0.3536159877)
        self.assertAlmostEqual(self.cmp.sim('Coiln', 'Colin'), 0.3536159877)
        self.assertAlmostEqual(
            self.cmp.sim('ATCAACGAGT', 'AACGATTAG'), 0.4828872776
        )

    def test_dunning_dist(self):
        """Test abydos.distance.Dunning.dist."""
        # Base cases
        self.assertEqual(self.cmp.dist('', ''), 0.0)
        self.assertEqual(self.cmp.dist('a', ''), 1.0)
        self.assertEqual(self.cmp.dist('', 'a'), 1.0)
        self.assertEqual(self.cmp.dist('abc', ''), 1.0)
        self.assertEqual(self.cmp.dist('', 'abc'), 1.0)
        self.assertEqual(self.cmp.dist('abc', 'abc'), 0.0)
        self.assertAlmostEqual(
            self.cmp.dist('abcd', 'efgh'), 0.9989064540089061
        )

        self.assertAlmostEqual(self.cmp.dist('Nigel', 'Niall'), 0.6463840123)
        self.assertAlmostEqual(self.cmp.dist('Niall', 'Nigel'), 0.6463840123)
        self.assertAlmostEqual(self.cmp.dist('Colin', 'Coiln'), 0.6463840123)
        self.assertAlmostEqual(self.cmp.dist('Coiln', 'Colin'), 0.6463840123)
        self.assertAlmostEqual(
            self.cmp.dist('ATCAACGAGT', 'AACGATTAG'), 0.5171127224
        )

    def test_dunning_sim_score(self):
        """Test abydos.distance.Dunning.sim_score."""
        # Base cases
        self.assertEqual(self.cmp.sim_score('', ''), 0.0)
        self.assertEqual(self.cmp.sim_score('a', ''), 0.0)
        self.assertEqual(self.cmp.sim_score('', 'a'), 0.0)
        self.assertEqual(self.cmp.sim_score('abc', ''), 0.0)
        self.assertEqual(self.cmp.sim_score('', 'abc'), 0.0)
        self.assertAlmostEqual(
            self.cmp.sim_score('abc', 'abc'), 22.03658785399824
        )
        self.assertAlmostEqual(
            self.cmp.sim_score('abcd', 'efgh'), 0.0292119377521926
        )

        self.assertAlmostEqual(
            self.cmp.sim_score('Nigel', 'Niall'), 11.0364485224
        )
        self.assertAlmostEqual(
            self.cmp.sim_score('Niall', 'Nigel'), 11.0364485224
        )
        self.assertAlmostEqual(
            self.cmp.sim_score('Colin', 'Coiln'), 11.0364485224
        )
        self.assertAlmostEqual(
            self.cmp.sim_score('Coiln', 'Colin'), 11.0364485224
        )
        self.assertAlmostEqual(
            self.cmp.sim_score('ATCAACGAGT', 'AACGATTAG'), 25.0086762304
        )

        # Tests with alphabet=0 (no d factor)
        self.assertEqual(self.cmp_no_d.sim_score('', ''), 0.0)
        self.assertEqual(self.cmp_no_d.sim_score('a', ''), 0.0)
        self.assertEqual(self.cmp_no_d.sim_score('', 'a'), 0.0)
        self.assertEqual(self.cmp_no_d.sim_score('abc', ''), 0.0)
        self.assertEqual(self.cmp_no_d.sim_score('', 'abc'), 0.0)
        self.assertEqual(self.cmp_no_d.sim_score('abc', 'abc'), 0.0)
        self.assertAlmostEqual(
            self.cmp_no_d.sim_score('abcd', 'efgh'), 5.517285850726809
        )

        self.assertAlmostEqual(
            self.cmp_no_d.sim_score('Nigel', 'Niall'), 1.3937830001
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim_score('Niall', 'Nigel'), 1.3937830001
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim_score('Colin', 'Coiln'), 1.3937830001
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim_score('Coiln', 'Colin'), 1.3937830001
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG'), 1.05211615
        )


if __name__ == '__main__':
    unittest.main()
