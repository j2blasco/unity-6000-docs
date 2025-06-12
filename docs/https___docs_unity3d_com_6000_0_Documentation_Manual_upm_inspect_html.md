* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-inspect.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Package inspection](https://docs.unity3d.com/6000.0/Documentation/Manual/package-inspection.html)
  * Inspect packages


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManifestImporter.html)
Package Manifest window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages-all.html)
Packages
# Inspect packages
The Project view displays the list of packages currently installed in your project from all sources. This means that **immutable** You cannot change the contents of an immutable (read-only) package. This is the opposite of **mutable**. Most packages are immutable, including packages downloaded from the package registry or by Git URL.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Immutable) packages that you installed from a package registry are visible, as well as **mutable** You can change the contents of a mutable package. This is the opposite of **immutable**. Only **Local package****s** and **Embedded package****s** are mutable.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mutable) packages (such as embedded and local packages).
![Registry package \(immutable\) on the left and an embedded package \(mutable\) on the right](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-inspect.png) Registry package (immutable) on the left and an embedded package (mutable) on the right
You can inspect the contents of any package that appears in the Project view. You can also inspect the **package manifest** Each package has a _manifest_ , which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Packagemanifest) through a dedicated **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector). 
To inspect a package manifest, click on it in the Project view.
![Inspecting a package manifest](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-project-view.png) Inspecting a package manifest
For [embedded](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Embedded) or [local](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Local) packages, you can change the package contents and [edit the package manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManifestImporter.html). 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManifestImporter.html)
Package Manifest window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages-all.html)
Packages
