For the Clock
===============

**Drawing Functions**

====================================  =================================================
Function                              Purpose
====================================  =================================================
``drawBackground(size, r)``           Draws tick marks and numbers to face canvas
``drawVFDDisplay(size, r, ctx)``      Renders VFD-style digital time display
``drawDiamondHand(angle, color, r)``  Draws second hand with diamond pointer
``drawMinuteHand(angle, color, r)``   Draws minute hand with diamond pointer
``drawCenterElement(r, baseAngle)``   Draws center circle where hands pivot
``renderFaceStatic(ctx, size, r)``    Complete static face render
``updateAndBlitVFD(ctx, size, r)``    Manages VFD caching and compositing
====================================  =================================================

**Geometry Functions**

* ``getCanvasCenterAndRadius()`` - Calculates current clock center and radius based on drift
* ``resizeCanvasToPanel()`` - Recalculates canvas size when window resizes

**Animation Functions**

* ``drawClock()`` - Main render function, draws all clock elements
* ``frame()`` - Animation loop callback (called via ``requestAnimationFrame``)

**Timing Functions**

The animation loop uses:

* ``performance.now()`` - High-resolution timestamps for smooth animation
* Current system time (``Date``) for hand positions
* Angle calculation: ``(seconds + milliseconds/1000) * 6`` degrees
