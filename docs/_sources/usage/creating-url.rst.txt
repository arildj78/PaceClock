Creating a URL
===============

**Method 1: Use Setup Mode (Easiest)**

1. Open the clock with setup mode enabled:
   
   ``https://arildj78.github.io/PaceClock/clock.html?setupmode=1``

2. Adjust the sliders and controls in the left panel to configure the clock appearance

3. Click the **Copy URL** button at the top of the setup panel

4. The URL with all your settings is now in your clipboard - paste it anywhere to share or bookmark

**Method 2: Manual URL Construction**

Add parameters to the base URL separated by ``&``:

``clock.html?parameter1=value1&parameter2=value2&parameter3=value3``

Example:

``clock.html?outerRel=0.9&showLogo=1&vfdColor=%2300ff00``

*Note: Special characters like # in hex colors need URL encoding (# becomes %23)*

**Tips for Creating URLs**

* Use ``setupmode=1`` to discover parameter values interactively
* URL encode special characters (spaces, #, &, etc.)
* Parameters can be in any order
* Omitted parameters use default values
* Boolean values: 0=false/off, 1=true/on
* Relative values (``*Rel`` parameters) are typically 0.0-1.0
* Colors use hex format: ``#RRGGBB`` (URL encode the #)

**Storing Multiple Configurations**

Create bookmarks in your browser for different setups:

* Pool deck display
* Presentation mode
* Custom team colors
* Different screen sizes

Each bookmark stores the complete configuration in its URL.
