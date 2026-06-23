Head
====

The HTML ``<head>`` section configures the page and loads resources.

Meta Tags
---------

* ``charset="utf-8"`` - UTF-8 character encoding
* ``viewport`` - Responsive viewport settings for proper mobile display

Font Loading
------------

* ``<link rel="preload">`` - Preloads BFont custom web font (woff2 format)
* ``@font-face`` CSS rule defines BFont family for clock numbers

Title
-----

* Page title: "Analog pacing‑klokke" (Analog pacing clock in Norwegian)

Inline CSS
----------

All styles are embedded directly in the ``<head>`` for single-file portability. Key style sections:

=======================  =====================================================
Style Section            Purpose
=======================  =====================================================
``@font-face``           Custom BFont definition for clock numerals
``body``                 Black background on the setup panel, flexbox layout, full viewport height
``#leftPanel``           Setup panel (hidden by default, shown in setup mode)
``#rightPanel``          Main clock display area (takes remaining space)
``#clock``               Canvas element styling
``.groupTitle``          Collapsible section headers in setup panel
``.controls``            Form controls container
``label``                Input label styling
``input[type="..."]``    Slider, checkbox, and color picker customization
``.value``               Display values next to controls
``#resetDriftBtn``       Reset drift button styling
=======================  =====================================================
