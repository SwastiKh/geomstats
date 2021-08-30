""" Homogeneous space module
    ******** INCOMPLETE AND NOT REQUIRED ***********
"""


import geomstats.backend as gs
# Import the class(es) that MyManifold inherits from
from geomstats.geometry.manifold import Manifold


# This class inherits from the class Manifold.
# Inheritance in geomstats means that the class MyManifold will reuse code
# that is in the Manifold class.
class Homogeneous(Manifold):
    r"""
    For example: Class for Homogeneous spaces.

    Formal definition: Let X be a non-empty set and G a group. Then X is called a G-space if it is equipped with an action of G on X. Note that automatically G acts by automorphisms (bijections) on the set. If X in addition belongs to some category, then the elements of G are assumed to act as automorphisms in the same category. That is, the maps on X coming from elements of G preserve the structure associated with the category (for example, if X is an object in Diff then the action is required to be by diffeomorphisms). A homogeneous space is a G-space on which G acts transitively..

    List the parameters of MyManifold, i.e. the parameters given as inputs
    of the constructor __init__.

    For example:
    Parameters
    ----------
    dim : int
        Dimension of the manifold.
    """

    def __init__(self, dim, another_parameter, **kwargs):
        super(MyManifold, self).__init__(dim)
        self.another_parameter = another_parameter

    # Implement the main methods of HomogeneousSpace, for example belongs:
    def belongs(self, point, atol=gs.atol):
        """Evaluate if a point belongs to the Homogeneous Space.

        List the parameters of the method.
        In what follows, the ellipsis ... indicate either nothing
        or any number n of elements, i.e. shape=[..., dim] means
        shape=[dim] or shape=[n, dim] for any n.
        All functions/methods of geomstats should work for any number
        of inputs. In the case of the method `belongs`, it means:
        for any number of input points.
        For example:

        Parameters
        ----------
        point : array-like, shape=[..., dim]
            Point to evaluate.
        atol : float
            Tolerance, unused.
            Optional, default: backend atol


        Returns
        -------
        belongs : array-like, shape=[...,]
            Boolean evaluating if point belongs to the manifold.
        """
        # Perform operations to check if point belongs
        # to the manifold, for example:
        belongs = point.shape[-1] == self.dim
        if gs.ndim(point) == 2:
            belongs = gs.tile([belongs], (point.shape[0],))
        return belongs

    # Another example of method of MyManifold.
    def is_tangent(self, vector, base_point=None, atol=gs.atol):
        """Check whether vector is tangent to the manifold at base_point.

        In what follows, the ellipsis ... indicates either nothing
        or any number n of elements, i.e. shape=[..., dim] means
        shape=[dim] or shape=[n, dim] for any n.
        All functions/methods of geomstats should work for any number
        of inputs. In the case of the function `is_tangent`, it means:
        for any number of input vectors.

        Parameters
        ----------
        vector : array-like, shape=[..., dim]
            Vector.
        base_point : array-like, shape=[..., dim]
            Point on the manifold.
            Optional, default: None.
        atol : float
            Absolute tolerance threshold

        Returns
        -------
        is_tangent : bool
            Boolean denoting if vector is a tangent vector at the base point.
        """
        # Perform operations to determine if vector is a tangent vector,
        # for example:
        is_tangent = gs.shape(vector)[-1] == self.dim
        if gs.ndim(vector) == 2:
            is_tangent = gs.tile([is_tangent], (vector.shape[0],))
        return is_tangent

    def to_tangent(self, vector, base_point):
        """Project a vector to a tangent space of the manifold.

        Parameters
        ----------
        vector : array-like, shape=[..., dim]
            Vector.
        base_point : array-like, shape=[..., dim]
            Point on the manifold.

        Returns
        -------
        tangent_vec : array-like, shape=[..., dim]
            Tangent vector at base point.
        """

    def random_point(self, n_samples=1, bound=1):
        """Sample random points on the homogeneous space of the manifold.

        If the manifold is compact, a uniform distribution is used.

        Parameters
        ----------
        n_samples : int
            Number of samples.
            Optional, default: 1.
        bound : float
            Bound of the interval in which to sample for non compact manifolds.
            Optional, default: 1.

        Returns
        -------
        samples : array-like, shape=[..., n]
            Points sampled on the homogeneous space.
        """
        n = self.n
        self.n_samples = n_samples
        sample = []
        n_accepted, iteration = 0, 0
        criterion_func = (lambda x: x) #if self.positive_det else gs.abs  *****Condition for homogeneous space here
        while n_accepted < n_samples and iteration < n_iter:
            raw_samples = gs.random.normal(size=(n_samples - n_accepted, n, n))
            dets = gs.linalg.det(raw_samples)
            criterion = criterion_func(dets) > gs.atol
            if gs.any(criterion):
                sample.append(raw_samples[criterion])
                n_accepted += gs.sum(criterion)
            iteration += 1
        if n_samples == 1:
            return sample[0][0]
        return gs.concatenate(sample)
