Preparing for Glitch-Free Animation
====================================

Canvas Caching
--------------

The application uses multiple canvases to optimize rendering:

* ``faceCanvas`` - Cached static clock face (tick marks, numbers)
* ``vfdCanvas`` - Cached VFD display segments
* Main canvas - Final composite with hands

**Cache Management**

* ``ensureFaceCache(size, r)`` - Creates/updates face cache when settings change
* ``updateAndBlitVFD(targetCtx, size, r)`` - Renders VFD to cache, then blits to screen

Double Buffering
-----------------

The main render loop:

1. Clears main canvas
2. Draws drift-positioned cached face
3. Draws VFD display (if enabled)
4. Draws minute hand (if enabled)
5. Draws second hand
6. Draws center circle

This approach avoids redrawing expensive elements every frame, providing smooth animation on all devices.
