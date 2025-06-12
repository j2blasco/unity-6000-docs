* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-tarball.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Package management with the Package Manager window](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-packages-window.html)
  * [Add and remove UPM packages or feature sets](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions.html)
  * Install a UPM package from a local tarball file


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-local.html)
Install a UPM package from a local folder
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-giturl.html)
Install a UPM package from a Git URL
# Install a UPM package from a local tarball file
The Package Manager can load a **UPM package** A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UPMpackage) from a tarball file stored locally. This is for advanced scenarios where you break your package publishing workflow into parts and your users can use the intermediate product of one of those parts.
For example, if you’ve set up continuous integration (CI) on your custom package repository, you can create a [Gzip](https://www.gnu.org/software/gzip/) tarball file from a package folder. You can create a `Gzip` tarball file by using the [npm pack](https://docs.npmjs.com/cli/pack.html) CLI or Unity Package Manager’s [Pack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.Pack.html) API. If you create a `Gzip` tarball file, test it before you publish it to a custom registry.
To install a UPM package from a local tarball file:
  1. Open the [Package Manager window](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-access.html), if it’s not already open.
  2. Click the **install (+)** button in the toolbar. The options for installing packages appear.
  3. Select **Install package from tarball** from the install menu to bring up a file browser.
  4. Go to the folder where you saved your tarball.
**Note** : The Package Manager’s file selection dialog recognizes tarballs only if they have a `.tgz` extension.
  5. Double-click the tarball file in the file selection dialog.


The file selection dialog closes, and the package now appears in the [list panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html) with the **Local** label.
## Additional resources
  * [Package types](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-package-types.html)
  * [Add and remove UPM packages or feature sets](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions.html)
  * [Add and remove asset packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions-ap.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-local.html)
Install a UPM package from a local folder
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-giturl.html)
Install a UPM package from a Git URL
