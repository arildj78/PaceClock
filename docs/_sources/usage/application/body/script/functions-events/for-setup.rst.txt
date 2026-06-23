For the Setup
===============

**URL Generation**

* ``buildConfigUrl()`` - Generates URL string with all current parameter values
* ``addFloat(name, val, def)`` - Helper to add float parameter if different from default
* ``addBool(name, val, def)`` - Helper to add boolean parameter if different from default

**Control Synchronization**

* ``syncControls()`` - Updates all slider values and labels from current variables
* Input event listeners - Update variables when controls change

**Control Event Handlers**

Each input has a change/input event listener that:

1. Reads the new value from the control
2. Updates the corresponding variable
3. Invalidates relevant caches (face or VFD)
4. Triggers a redraw

**Special Controls**

* **Copy URL Button** - Calls ``buildConfigUrl()`` and copies to clipboard via ``navigator.clipboard``
* **Reset Drift Button** - Calls ``initializeDrift()`` to recenter the clock
* **VFD Test Mode** - Cycles through test patterns (88:88, etc.) for calibration
* **Run Clock Checkbox** - Toggles between live time and manual angle mode

**Setup Panel Visibility**

The ``setupmode`` URL parameter controls panel visibility:

.. code-block:: javascript

   const SETUPMODE = paramBool('setupmode', false);
   if (SETUPMODE) {
     leftPanel.style.display = 'flex';
   }

**Window Resize Handler**

.. code-block:: javascript

   window.addEventListener('resize', () => {
     resizeCanvasToPanel();
     drawClock();
   });

Recalculates dimensions and redraws when window size changes.
