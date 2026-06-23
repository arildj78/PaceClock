Set Defaults
=============

Constants define default values for all parameters (lines ~444-490 in clock.html):

.. code-block:: javascript

   const DEFAULT_outerRel = 0.95;
   const DEFAULT_minorInnerRel = 0.816;
   const DEFAULT_majorInnerRel = 0.774;
   // ... 40+ more default constants

These defaults ensure the clock works immediately without any URL parameters. All ``DEFAULT_*`` constants should have sensible fallback values.
