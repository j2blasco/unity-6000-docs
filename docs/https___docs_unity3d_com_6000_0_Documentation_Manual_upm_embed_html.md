* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-embed.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/dependencies-lp.html)
  * Embedded dependencies


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-conflicts.html)
Package version conflict and resolution
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-conflicts-auto.html)
Lock files
# Embedded dependencies
Any package that appears under your project’s `Packages` folder is embedded in that project. You can create an **embedded package** An _embedded_ package is a mutable package that you store under the `Packages` directory at the root of a Unity project. This differs from most packages which you download from a package server and are immutable. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Embedded)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Embeddedpackage) in several ways:
  * [Create a new package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-embed.html#embed-create) directly in your project’s `Packages` folder.
  * [Manually copy a Unity package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-embed.html#embed-cached) from the project’s package cache into your project’s `Packages` folder.
  * [Use a C# script to embed](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-api.html#Embed) a version of a package that’s already installed.


Embedded packages don’t need to appear in the project manifest as a dependency. However, if you embedded a version of an installed package, your project manifest still lists the dependency on the original installed version. In that case, the package on disk takes priority over the version of the package listed as a dependency, so it doesn’t need to be removed from the project manifest. For example, if the project manifest specifies a dependency on version 1.3.1 of the `com.unity.example` package but the project also has an embedded package with that name, the Package Manager uses the embedded package, regardless of its apparent version, instead of downloading version 1.3.1 from the registry.
Make sure you track the contents of your embedded packages, and any changes you make to it. If your Unity project is under source control, add any packages embedded in that project to the same source control. 
## Creating a new custom package
To embed a new package, create your new package content inside a folder under the `Packages` folder. For more information, follow the [instructions for creating your own custom package](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomPackages.html). 
Typically, your new package remains embedded in your project until you are ready to share it with other users and test it in other projects. You can use different methods to [share your package](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-share.html), for example, you can [host the package on a scoped registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped-host.html).
## Copying a Unity package from the cache
A package installed from a registry is **immutable** You cannot change the contents of an immutable (read-only) package. This is the opposite of **mutable**. Most packages are immutable, including packages downloaded from the package registry or by Git URL.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Immutable), which means you can’t edit it. If you want to edit a package, you can make it **mutable** You can change the contents of a mutable package. This is the opposite of **immutable**. Only **Local package****s** and **Embedded package****s** are mutable.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mutable) by copying it to the `Packages` subfolder in your `Projects` folder. This package type is called an embedded package, and it overrides what’s in your package cache. Later, you can delete that embedded package’s folder from the `Packages` subfolder, and the Package Manager will automatically change to the immutable, cached package.
**Important** : Unity supports the following procedure for creating an embedded package only. Accessing the package cache folder for any other purpose is discouraged and not supported by Unity. Don’t manipulate the contents of the package cache folder.
To find your package’s folder in the cache, locate the installed version directly in the Unity Editor:
  1. Open the Project window by opening the **Window** menu and selecting **General** > **Project**.
  2. From the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), find the installed package you want to embed.
  3. Right-click the folder of the selected package and select **Show in Explorer** (Windows) or **Reveal in Finder** (macOS). That package’s folder opens directly in a file browser and uses the `<package-name>@<fingerprint>` naming convention.
![File browser opened to the package folder under the projects package cache](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-embed.png) File browser opened to the package folder under the project’s package cache
  4. Copy the package folder and paste it directly into your project’s `Packages` subfolder, not the `Packages` root folder. Don’t put it inside the `Assets` folder, because the Package Manager doesn’t scan that folder for packages.
  5. Remove the `@<fingerprint>` part of the folder name.
  6. Add the newly embedded package to source control if your project is already under source control.


If you want to delete the embedded package, use your file browser or command line to locate that package in your `Packages` folder. Consider backing up the folder for the embedded package, otherwise you’ll lose any changes you made to the package. Then, delete the folder for that package from your `Packages` folder. The Package Manager will automatically revert to the immutable, cached package.
## Additional resources
  * [Project manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPrj.html)Each Unity project has a _project manifest_ , which acts as an entry point for the Package Manager. This file must be available in the `<project>/Packages` directory. The Package Manager uses it to configure many things, including a list of dependencies for that project, as well as any package repository to query for packages. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPrj.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectmanifest)
  * [Use a script to embed a package in your project](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-api.html#Embed)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-conflicts.html)
Package version conflict and resolution
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-conflicts-auto.html)
Lock files
