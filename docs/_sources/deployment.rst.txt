Deployment & Hosting
====================

GitHub Pages
------------

**Current Deployment**

The project is deployed at: https://arildj78.github.io/PaceClock/clock.html

**Deploying Updates**

To deploy application updates:

.. code-block:: bash

   git add .
   git commit -m "Update clock"
   git push origin main

GitHub Pages automatically serves the updated files from the ``main`` branch.

**Repository Settings**

Ensure GitHub Pages is enabled in repository settings:

1. Go to repository Settings → Pages
2. Source: Deploy from a branch
3. Branch: ``main`` / ``(root)``
4. Save

Changes typically appear within 1-2 minutes of pushing.

Documentation Deployment
------------------------

**Automatic Deployment**

Documentation is auto-deployed via GitHub Actions workflow (``.github/workflows/docs.yml``) to:

https://arildj78.github.io/PaceClock/docs/

The workflow automatically:

1. Triggers on pushes to ``main`` branch
2. Installs Python and Sphinx dependencies
3. Builds HTML documentation from ``docs/`` folder
4. Deploys to ``gh-pages`` branch
5. Publishes to GitHub Pages

**Building Locally**

To build and preview documentation on your machine:

.. code-block:: powershell

   # Install dependencies
   pip install -r docs/requirements.txt

   # Build HTML docs
   cd docs
   ./make.bat html

   # Open in browser
   start _build/html/index.html

**Manual Deployment**

If automatic deployment fails, manually trigger the workflow:

1. Go to Actions tab in GitHub repository
2. Select "Deploy Documentation" workflow
3. Click "Run workflow"

Other Hosting Options
---------------------

**Self-Hosted Web Server**

Copy all project files to your web server:

* ``clock.html`` - Main application
* ``index.html`` - Dual-panel display (optional)
* ``font/bfont.woff2`` - Custom font
* ``bsk.png``, ``bsk_klokke.png`` - Logo images

Serve with any web server (Apache, nginx, IIS, etc.). No server-side processing required.

**Cloud Storage**

Upload to cloud storage with static website hosting:

* **AWS S3** - Enable static website hosting on bucket
* **Azure Blob Storage** - Configure static website serving
* **Google Cloud Storage** - Set up static site bucket
* **Netlify/Vercel** - Drag-and-drop deployment

**Local Display (No Internet)**

For pool deck displays without internet:

1. Copy project folder to USB drive
2. Plug into display computer
3. Open ``clock.html`` directly in a web browser
4. Bookmark or add to startup for quick access

The clock uses system time, so no internet connection is required after initial file load.

**Offline PWA (Future Enhancement)**

Consider adding a service worker for offline functionality and app-like installation on devices.

