Accessing Configuration
=======================

There are two ways to access and modify clock settings: setup mode and URL parameters.

Setup Mode
----------

**Interactive Control Panel**

The easiest way to adjust settings is through the setup mode control panel.

Open the clock with setup mode enabled:

``https://arildj78.github.io/PaceClock/clock.html?setupmode=1``

The left side of the screen displays an interactive control panel with sliders and checkboxes for all settings. Changes are reflected immediately on the clock.

**Copy Configuration URL**

Once you've configured the clock to your liking:

1. Look at the bottom of the setup panel
2. Click the **Copy URL** button
3. The URL with all your settings is now in your clipboard
4. Share or bookmark this URL to save your configuration

URL Parameters
--------------

All clock settings can be controlled via URL query parameters. You don't need setup mode to use custom URLs—you can manually construct them or share them directly.

See the URL Parameters section for a complete reference of all available parameters and their values.

Manual URL Construction
^^^^^^^^^^^^^^^^^^^^^^^

To manually build a URL with custom settings:

``clock.html?parameter1=value1&parameter2=value2&parameter3=value3``

Example:

``clock.html?outerRel=0.9&showLogo=1&vfdColor=%2300ff00``

*Note: Special characters like # in hex colors need URL encoding (# becomes %23)*

Local Configuration
-------------------

If you're using clock.html locally:

1. Open ``clock.html?setupmode=1`` in your browser
2. Adjust all settings using the control panel
3. Click **Copy URL** to get the configuration
4. Save this URL as a bookmark or share it

The configuration is entirely encoded in the URL, so you can create multiple bookmarks for different setups (pool A, pool B, different screen sizes, etc.).
