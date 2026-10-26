Screen Saver
=============

Prevent screen burn-in by slowly drifting the clock position across the screen.

The Edge margin slider ranges from -0.2 to 0.2, as a fraction of the smaller
canvas dimension. Zero allows the clock to reach the screen edges. Negative
values allow drift beyond the edges and may clip part of the clock; positive
values keep it farther inside the screen. This applies to all three clock modes.
The margin is preserved in shared URLs.

========================  ===========  =============================================
Parameter                 Default      Description
========================  ===========  =============================================
``driftEnabled``          1            Enable drift mode (0=off, 1=on)
``driftSpeedRel``         0.00002      Drift speed (very slow by default)
``driftAngleDeg``         60           Drift direction in degrees (0-360)
``driftMarginRel``        0.00         Margin from canvas edges
``driftSetupMultiplier``  120          Speed boost in setup mode for visibility
========================  ===========  =============================================
