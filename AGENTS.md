# AGENTS.md

## Project Overview
**Svømmeklokke2** (Swimming Clock v2) is a web-based analog pace clock application designed for swim training. The application displays a large, customizable analog clock with optional digital display, perfect for timing swimming intervals and pace work.

## Purpose
This pace clock is designed for swim coaches and athletes to:
- Display timing for swimming intervals on large screens
- Provide clear visual reference during training sessions
- Integrate with Google Slides for workout programs
- Offer highly customizable visual appearance for different pool environments

## Architecture

### Main Components

#### 1. **index.html** - Main Display Interface
- **Purpose**: Dual-panel display combining the pace clock with workout slides
- **Layout**: 
  - Left panel: Embedded pace clock (iframe pointing to GitHub Pages hosted clock)
  - Right panel: Embedded Google Slides presentation with daily swim program
- **Display**: Full-screen split-view optimized for large displays/projectors

#### 2. **clock.html** - Analog Pace Clock Application
- **Purpose**: Standalone customizable analog clock with extensive configuration
- **Technology**: Pure JavaScript with HTML5 Canvas
- **Features**:
  - Analog clock face with 60-second markings
  - Dual hand system (second hand + optional minute hand)
  - Digital VFD-style time display (HH:MM format)
  - Logo display capability (BSK logo)
  - Screen drift/screensaver mode
  - Extensive URL-based configuration
  - Optional setup panel for live configuration

### Key Features

#### Visual Customization
- **Clock Geometry**: Adjustable outer size, tick marks (major/minor), tick width
- **Hands**: Configurable shaft width, tip length, diamond pointer shape
- **Numbers**: Adjustable size, position, font, per-number fine-tuning (5, 10, 15...60)
- **Digital Display**: VFD-style display with customizable color, glow, size, position
- **Logo**: Resizable and repositionable club logo
- **Colors**: Customizable hand colors and digital display colors
- **Logo display capability (club logo)

#### Animation & Behavior
- **Clock Running**: Can be toggled on/off
- **Manual Control**: Manual angle adjustment for demonstrations
- **Drift Mode**: Optional screensaver-style drifting of clock across screen
- **Minute Hand**: Optional minute hand for longer intervals

#### Configuration System
- **URL Parameters**: All settings can be controlled via URL query parameters
- **Setup Mode**: Debug panel (`setupmode=1`) with live sliders for all parameters
- **Copy URL**: Generate shareable URLs with current configuration
- **Defaults**: Sensible defaults for immediate use

## File Structure

```
Svømmeklokke2/
├── index.html           # Main dual-panel display
├── clock.html           # Pace clock application
├── font/
│   └── bfont.woff2     # Custom font for numbers
├── bsk.png             # Club logo (main)
├── bsk_klokke.png      # Logo variant (with clock)
├── bsk_sirkel.png      # Logo variant (circle)
└── AGENTS.md           # This file
```

## Technical Details

### Canvas Rendering
- Uses HTML5 Canvas 2D context
- Automatically scales to screen size while maintaining aspect ratio
- Respects `outerRel` parameter for size relative to viewport height
- High-DPI aware (uses `devicePixelRatio`)

### URL Parameters (Key Examples)
- `outerRel`: Clock size relative to screen height (0.2-1.0)
- `showLogo`: Toggle logo visibility (0/1)
- `logoSizeRel`: Logo size relative to clock radius
- `showMinute`: Enable minute hand (0/1)
- `vfdEnabled`: Show digital display (0/1)
- `runClock`: Animate clock (0/1)
- `driftEnabled`: Enable screen drift mode (0/1)
- `driftSpeedRel`: Drift speed multiplier
- `setupmode`: Show control panel for adjustments (0/1)

### Time System
- Displays current system time (HH:MM:SS)
- Second hand completes one revolution per minute
- Minute hand (when enabled) completes one revolution per hour
- Precise timing using `performance.now()` for smooth animation

### Drift/Screensaver Mode
- Prevents burn-in on static displays
- Configurable drift speed, angle, and margin
- Can be reset to center via setup panel

## Usage Scenarios

### 1. Pool Deck Display
Use [index.html](index.html) on a large screen/projector:
- Clock on left for timing
- Workout slides on right for instructions
- Full-screen mode for optimal visibility

### 2. Standalone Clock
Use [clock.html](clock.html) directly:
- Full-screen analog clock
- Configure via URL parameters
- Share custom configurations with teams

### 3. Live Configuration
Use [clock.html?setupmode=1](clock.html?setupmode=1):
- Access control panel for real-time adjustments
- Fine-tune appearance for specific environments
- Copy URL with settings for sharing

## Development Notes

### For AI Assistants
When modifying this code:
1. **Preserve URL parameter system**: All settings should remain URL-configurable
2. **Maintain defaults**: `DEFAULT_*` constants must have sensible fallbacks
3. **Test setup mode**: Changes should work both in normal and setup mode
4. **Canvas scaling**: Be mindful of DPI scaling and aspect ratio preservation
5. **Performance**: Clock runs continuously; optimize rendering loops
6. **Font loading**: Custom BFont must load before rendering numbers

### Code Organization
- **Configuration section**: Lines ~90-300 (defaults and URL parsing)
- **Setup panel creation**: Lines ~300-700 (if `setupmode=1`)
- **Drawing functions**: Lines ~900-1400 (canvas rendering)
- **Animation loop**: Lines ~1400-1600 (main render loop)
- **Event handlers**: Lines ~1600-1800 (controls and resize)

## Future Enhancement Ideas
- [ ] Countdown timer mode
- [ ] Multiple interval presets
- [ ] Sound/beep on lap completion
- [ ] Split time recording
- [ ] Mobile-responsive design
- [ ] Touch controls for setup on tablets
- [ ] Multiple color themes
- [ ] Export/import configuration JSON

## Related Resources
- Live deployment: https://arildj78.github.io/PaceClock/clock.html
- Repository: (Git repository present - check `.git/` directory)

## Contact & Usage
Created by Arild M Johannessen for Bodø Svømmeklubb. This pace clock is designed for swim coaching and training at competitive swim clubs. The design balances functionality with visual clarity for pool deck environments.

---
*Last updated: February 6, 2026*
