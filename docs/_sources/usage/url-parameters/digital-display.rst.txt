Digital Display
===============

Standalone 24-hour clock
------------------------

Use ``mode=digital`` for a pure digital clock, ``mode=swim`` for the original
pace clock (the default), or ``mode=wall`` for the analog wall clock.
The digital clock uses local system time in 24-hour format with leading zeros.
It never displays analog hands, dial markings, a reference image, or a logo.

Open ``clock.html?mode=digital&setupmode=1`` to configure it. The three clock
buttons keep separate settings while the page is open. Use the source selector
and "Grab values from other interface" to copy another clock's settings.
Only controls relevant to the selected mode are shown.

========================  ==========  ==========================================
Parameter                 Default     Description
========================  ==========  ==========================================
``digitalStyle``          clean       Design (see choices below)
``digitalFont``           mono        Font for text-based designs (see below)
``digitalShowSeconds``    1           HH:MM:SS when on, HH:MM when off
``digitalScaleRel``       0.9         Size relative to available area (0.2-1)
``digitalSpacingRel``     1           Digit spacing multiplier (-2 to 4)
``digitalYOffsetRel``     0           Vertical position (-0.5 top to 0.5 bottom)
``digitalGlowRel``        0           Glow intensity (0-1)
``digitalManualTime``     12:00:00    Preview time (HH:MM:SS) when ``runClock=0``
``vfdColor``              #00b7ff     Digit color (hex code)
``backgroundColor``       #000000     Background color (hex code)
========================  ==========  ==========================================

Design choices:

* ``clean``: solid, bold text.
* ``segment``: classic seven-segment LED digits.
* ``matrix``: the same dot patterns as the pace clock's VFD.
* ``outline``: outlined text.
* ``split-flap``: text on individual dark cards with a horizontal flap seam.
  This is a static visual treatment, not a flip animation.

Font choices for Clean, Outline, and Split-flap:

* ``mono``: system monospace (default).
* ``sans``: Arial / Helvetica.
* ``serif``: Georgia / Times New Roman.
* ``condensed``: Impact / Arial Narrow.
* ``rounded``: Trebuchet MS / Verdana.
* ``club``: the bundled BFont.

System font availability varies by device; each choice has a fallback.
No external font service is used. Fonts are fitted within fixed digit cells
to keep the display stable as the time changes. Seven-segment and Dot-matrix
use drawn shapes, so the font selector is disabled for those designs.

The Digit spacing (kerning) slider works in all five designs and adjusts the gaps
only between adjacent digits within each HH, MM, or SS pair.
It does not affect the gaps beside colons. Zero removes the extra gap, 1 preserves
the original spacing, and 4 gives four times the extra gap. Negative values down
to -2 pull character cells closer together and can overlap them. Spacing only moves
characters: glyph size, height, and stroke thickness remain unchanged.
Size is fitted using the original spacing, independently of this control.
Wide spacing can extend beyond the drawing area; reduce Size to fit it.
Spacing is retained when switching modes and included in shared URLs.

Colon spacing (``digitalColonPaddingRel``, default 1, range 0-4) adds equal
padding on each side of each separator, independently of digit spacing.
In digit-cell units, a gap between adjacent digits is ``8 * digitalSpacingRel``
and a gap beside a colon is ``8 * digitalColonPaddingRel``.
Neither slider affects the other type of gap. Unlike the Swim Clock's additive
VFD spacing, standalone digital spacing uses separate gaps for digits and colons.
Use Colon vertical offset (``digitalColonYOffsetRel``, default 0, range -0.1 to 0.1)
to move only the separators up (negative) or down
(positive), relative to the 100-unit digit cell height. Both controls apply to
every design and both separators when seconds are shown. They do not change
glyph size or stroke thickness and are retained in mode settings and shared URLs.

Color presets, Run clock, screen-saver drift, debug overlay, and Copy URL work
in digital mode too. Turn off Run clock to edit the manual preview time.
At the original spacing, the display fits both the width and height of its drawing
area. Drift bounds account for the actual character spacing, rectangular shape,
vertical position, and glow. If the display is too wide to drift, it stays centered.

The generated share URL preserves the selected mode and its settings, but omits
``setupmode``. ``vfdEnabled`` and the other VFD geometry/test settings below
apply only to the swim clock's optional display, not the standalone digital clock.

Swim clock VFD
--------------

Configure the optional swim clock time display (HH:MM format) with VFD
(vacuum fluorescent display) styling.

====================  =========  =============================================
Parameter             Default    Description
====================  =========  =============================================
``vfdEnabled``        1          Show digital time display (0=off, 1=on)
``vfdColor``          #00b7ff    Color of digital display (hex code)
``vfdScaleRel``       0.346      Size of digital display
``vfdYOffsetRel``     0.300      Vertical position (0=center, + is down)
``vfdGlowRel``        0.000      Glow intensity (shadow blur)
``vfdColonPadding``   0.400      Space around colon character
``vfdDigitGapRel``    0.380      Space between digits
``vfdCornerRel``      0.25       Corner roundness of display segments
====================  =========  =============================================
