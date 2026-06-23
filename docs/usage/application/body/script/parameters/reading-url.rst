Reading Parameters from URL
============================

URL parameters override defaults (lines ~543-620 in clock.html):

.. code-block:: javascript

   outerRel = paramFloat('outerRel', outerRel);
   minorInnerRel = paramFloat('minorInnerRel', minorInnerRel);
   showLogo = paramBool('showLogo', showLogo);
   vfdColor = params.get('vfdColor') || vfdColor;
   // ... all parameters parsed from URL

The ``URLSearchParams`` API reads query string parameters and converts them to the appropriate type. This happens during initialization, allowing users to share configuration URLs.
