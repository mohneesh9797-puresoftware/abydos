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

"""abydos.distance._quantitative_jaccard.

Quantitative Jaccard similarity
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from ._token_distance import _TokenDistance

__all__ = ['QuantitativeJaccard']


class QuantitativeJaccard(_TokenDistance):
    r"""Quantitative Jaccard similarity.

    For two multisets X and Y drawn from an alphabet S, Quantitative Jaccard
    similarity is

        .. math::

            sim_{QuantitativeJaccard}(X, Y) =
            \frac{\sum_{i \in S} X_iY_i}
            {\sum_{i \in S} X_i^2 + \sum_{i \in S} Y_i^2 -
            \sum_{i \in S} X_iY_i}

    .. versionadded:: 0.4.0
    """

    def __init__(self, tokenizer=None, **kwargs):
        """Initialize QuantitativeJaccard instance.

        Parameters
        ----------
        tokenizer : _Tokenizer
            A tokenizer instance from the :py:mod:`abydos.tokenizer` package
        **kwargs
            Arbitrary keyword arguments

        Other Parameters
        ----------------
        qval : int
            The length of each q-gram. Using this parameter and tokenizer=None
            will cause the instance to use the QGram tokenizer with this
            q value.


        .. versionadded:: 0.4.0

        """
        super(QuantitativeJaccard, self).__init__(
            tokenizer=tokenizer, **kwargs
        )

    def sim(self, src, tar):
        """Return the Quantitative Jaccard similarity of two strings.

        Parameters
        ----------
        src : str
            Source string (or QGrams/Counter objects) for comparison
        tar : str
            Target string (or QGrams/Counter objects) for comparison

        Returns
        -------
        float
            Quantitative Jaccard similarity

        Examples
        --------
        >>> cmp = QuantitativeJaccard()
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
        self._tokenize(src, tar)

        alphabet = self._total().keys()

        product = sum(
            self._src_tokens[tok] * self._tar_tokens[tok] for tok in alphabet
        )

        return product / (
            sum(
                self._src_tokens[tok] * self._src_tokens[tok]
                for tok in alphabet
            )
            + sum(
                self._tar_tokens[tok] * self._tar_tokens[tok]
                for tok in alphabet
            )
            - product
        )


if __name__ == '__main__':
    import doctest

    doctest.testmod()
