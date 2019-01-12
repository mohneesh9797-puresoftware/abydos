# -*- coding: utf-8 -*-

# Copyright 2018 by Christopher C. Little.
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

"""abydos.distance._kuhns_viii.

Kuhns VIII similarity
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from ._token_distance import _TokenDistance

__all__ = ['KuhnsVIII']


class KuhnsVIII(_TokenDistance):
    r"""Kuhns VIII similarity.

    For two sets X and Y and a population N, Kuhns VIII similarity
    :cite:`Kuhns:1965`, the excess of coefficient by the arithmetic mean over
    its independence value, is

        .. math::

            sim_{KuhnsVIII}(X, Y) =
            \frac{\delta(X, Y)}{|X \cap Y|+\frac{1}{2}\cdot|X \triangle Y|}

    where

        .. math::

            \delta(X, Y) = |X \cap Y| - \frac{|X|+|Y|}{|N|}

    In :ref:`2x2 confusion table terms <confusion_table>`, where a+b+c+d=n,
    this is

        .. math::

            sim_{KuhnsVIII} =
            \frac{\delta(a+b, a+c)}{a+\frac{1}{2}(b+c)}

    where

        .. math::

            \delta(a+b, a+c) = a - \frac{2a+b+c}{n}

    Note
    ----

    The coefficient presented in :cite:`Eidenberger:2014,Morris:2012` as Kuhns'
    "Coefficient of arithmetic means" is a significantly different
    coefficient, not evidenced in :cite:`Kuhns:1965`.

    .. versionadded:: 0.4.0
    """

    def __init__(
        self,
        alphabet=None,
        tokenizer=None,
        intersection_type='crisp',
        **kwargs
    ):
        """Initialize KuhnsVIII instance.

        Parameters
        ----------
        alphabet : Counter, collection, int, or None
            This represents the alphabet of possible tokens.
            See :ref:`alphabet <alphabet>` description in
            :py:class:`_TokenDistance` for details.
        tokenizer : _Tokenizer
            A tokenizer instance from the :py:mod:`abydos.tokenizer` package
        intersection_type : str
            Specifies the intersection type, and set type as a result:
            See :ref:`intersection_type <intersection_type>` description in
            :py:class:`_TokenDistance` for details.
        **kwargs
            Arbitrary keyword arguments

        Other Parameters
        ----------------
        qval : int
            The length of each q-gram. Using this parameter and tokenizer=None
            will cause the instance to use the QGram tokenizer with this
            q value.
        metric : _Distance
            A string distance measure class for use in the 'soft' and 'fuzzy'
            variants.
        threshold : float
            A threshold value, similarities above which are counted as
            members of the intersection for the 'fuzzy' variant.


        .. versionadded:: 0.4.0

        """
        super(KuhnsVIII, self).__init__(
            alphabet=alphabet,
            tokenizer=tokenizer,
            intersection_type=intersection_type,
            **kwargs
        )

    def sim(self, src, tar):
        """Return the Kuhns VIII similarity of two strings.

        Parameters
        ----------
        src : str
            Source string (or QGrams/Counter objects) for comparison
        tar : str
            Target string (or QGrams/Counter objects) for comparison

        Returns
        -------
        float
            Kuhns VIII similarity

        Examples
        --------
        >>> cmp = KuhnsVIII()
        >>> cmp.sim('cat', 'hat')
        0.0
        >>> cmp.sim('Niall', 'Neil')
        0.0
        >>> cmp.sim('aluminum', 'Catalan')
        0.0
        >>> cmp.sim('ATCG', 'TAGC')
        0.0


        .. versionadded:: 0.4.0

        """
        self.tokenize(src, tar)

        a = self.intersection_card()
        b = self.src_only_card()
        c = self.tar_only_card()
        n = self.population_card()

        delta_ab = a - (2 * a + b + c) / n

        return delta_ab / (a + 0.5 * (b + c))


if __name__ == '__main__':
    import doctest

    doctest.testmod()