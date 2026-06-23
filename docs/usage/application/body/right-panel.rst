Right Panel
============

The right panel (``#rightPanel``) contains the main clock canvas.

**Structure**

.. code-block:: html

   <div id="rightPanel">
     <canvas id="clock"></canvas>
   </div>

The canvas fills the available space using flexbox centering. Canvas dimensions are dynamically calculated based on screen size and the ``outerRel`` parameter.
