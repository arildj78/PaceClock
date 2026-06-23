Initialization
================

The script begins immediately after DOM loading:

1. **Element References** - Gets references to canvas, context, and control elements
2. **Setup Mode Detection** - Checks URL for ``setupmode=1`` parameter
3. **Left Panel Toggle** - Shows/hides setup panel based on setup mode
4. **Event Listeners** - Attaches change handlers to all controls
5. **Window Resize Handler** - Recalculates canvas size when window changes
