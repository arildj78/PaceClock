Helper Functions
=================

**URL Parameter Parsing**

* ``paramFloat(name, current)`` - Reads float parameter from URL, returns current value if not found
* ``paramBool(name, current)`` - Reads boolean parameter (0/1) from URL

**Canvas Utilities**

* ``resizeCanvasToPanel()`` - Calculates and sets canvas dimensions based on viewport
* ``getCanvasCenterAndRadius()`` - Computes clock center position and radius
* ``getFaceSettingsHash()`` - Generates hash of current face settings for cache invalidation
* ``getVFDSettingsHash()`` - Generates hash for VFD display settings

**Drift/Screensaver System**

* ``initializeDrift(w, h)`` - Initializes drift position and velocity
* ``updateDrift(w, h)`` - Updates drift position, handles edge collision and bouncing
