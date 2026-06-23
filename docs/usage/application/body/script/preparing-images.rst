Preparing Images
==================

Logo and reference images are preloaded (lines ~621-633 in clock.html):

.. code-block:: javascript

   const logoImg = new Image();
   logoImg.src = './bsk.png';

   const bgImg = new Image();
   bgImg.src = './bsk_klokke.png';

Images load asynchronously. The render loop requests a redraw when they're ready. This prevents the clock from stuttering while waiting for images to download.
