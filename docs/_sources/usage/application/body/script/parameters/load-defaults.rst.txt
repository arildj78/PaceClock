Load Defaults
==============

After defining constants, variables are initialized to defaults (lines ~493-540 in clock.html):

.. code-block:: javascript

   let outerRel = DEFAULT_outerRel;
   let minorInnerRel = DEFAULT_minorInnerRel;
   let majorInnerRel = DEFAULT_majorInnerRel;
   // ... matching variable declarations

These variables track current parameter values and are updated whenever configuration changes.
