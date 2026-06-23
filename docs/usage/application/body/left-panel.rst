Left Panel
===========

The left panel (``#leftPanel``) contains the interactive configuration interface. It's hidden by default and only appears when ``setupmode=1`` is set in the URL.

**Structure**

.. code-block:: html

   <div id="leftPanel">
     <button id="copyUrlBtn">Copy URL</button>
     <button id="resetDriftBtn">Reset Drift Position</button>
     <details><summary>Tick marks</summary>...</details>
     <details><summary>Hands & diamond</summary>...</details>
     <details><summary>Numbers</summary>...</details>
     <details><summary>Digital display</summary>...</details>
     <details><summary>Minute hand</summary>...</details>
     <details><summary>Logo</summary>...</details>
     <details><summary>Screen saver</summary>...</details>
     <details><summary>Slide size / Animate</summary>...</details>
     <details><summary>Reference image</summary>...</details>
   </div>

**Control Groups**

1. **Copy URL Button** - Generates and copies current configuration URL to clipboard
2. **Reset Drift Button** - Centers the clock on screen (resets drift position)
3. **Tick marks** - Sliders for clock geometry (outer size, tick radii, widths)
4. **Hands & diamond** - Second hand geometry controls (shaft, tip, diamond shape)
5. **Numbers** - Number size, position, and per-number fine-tuning sliders
6. **Digital display** - VFD display settings (enabled, color, size, position, glow)
7. **Minute hand** - Minute hand geometry and color
8. **Logo** - Logo visibility, size, and position
9. **Screen saver** - Drift mode settings (speed, angle, margin)
10. **Slide size / Animate** - Clock animation toggle and manual angle control
11. **Reference image** - Background reference image for design matching

Each group uses ``<details>`` elements for collapsible sections, keeping the interface clean and organized.
