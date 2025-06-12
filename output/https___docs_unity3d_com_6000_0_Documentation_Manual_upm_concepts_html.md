* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Get started with packages](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages.html)
  * Introduction to packages


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages.html)
Get started with packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-overview.html)
How Unity works with packages
# Introduction to packages
This section explains many of the concepts surrounding the Unity Package Manager functionality:
  * [Versions](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Versions)
  * [Manifests](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Manifests)There are two types of manifest files: **project manifest****s** and **package manifest****s**.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Manifest)
  * [Registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Registry)
  * [Package Management](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Management)
  * [Package sources](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Sources)


## Versions
Multiple versions of each package are available, marking changes to that package along its lifecycle. Every time a developer updates the package, they [give it a new version number](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-semver.html). A change in package version tells you whether it contains a breaking change (major), new backward-compatible functionality (minor), or bug fixes only (patch). These indicators follow [Semantic Versioning](http://semver.org/) rules.
To view the list of versions available for a specific package, refer to [Find a specific version of a package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-find-ver.html).
## Manifests
There are two types of manifest files:
  * [Project manifests](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPrj.html)Each Unity project has a _project manifest_ , which acts as an entry point for the Package Manager. This file must be available in the `<project>/Packages` directory. The Package Manager uses it to configure many things, including a list of dependencies for that project, as well as any package repository to query for packages. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPrj.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectmanifest) (`manifest.json`) store information that the Package Manager needs to locate and load the right packages, including a list of packages and versions declared as dependencies.
  * [Package manifests](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html)Each package has a _manifest_ , which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Packagemanifest) (`package.json`) store information about a specific package, and a list of packages and versions that the package requires.


Both files use [JSON](https://json.org) (JavaScript Object Notation) syntax.
## Registry
In the domain of Unity’s Package Manager, a package registry is a server that stores package contents and information (metadata) on each package version. Unity maintains a central registry of official packages that are available for distribution. By default, all projects use the official Unity package registry. But you can [add additional registries](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html) to store and distribute private packages or stage custom packages while you are developing them.
## Package management
The Unity Package Manager is a tool that manages the entire package system. Its primary tasks include the following:
  * It [communicates with the Unity package registry server](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-dependencies.html) and any [additional registries](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html) you specify.
  * It reads your [project manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPrj.html) and fetches package contents and metadata.
  * It [installs](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-install.html), [updates](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-update.html), and [removes](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove.html) **UPM packages** A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UPMpackage), whether they’re dependencies of the project or one of the installed packages.
  * It [downloads and imports asset packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-import.html) that you previously acquired from the **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore).
  * It [enables and disables](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-disable.html) Unity’s built-in packages.
  * It [displays information](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html) about every version of every package.
  * It [resolves conflicts](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-conflicts.html) when the project and its packages require more than one package version.


The Unity Package Manager installs samples, tools, and assets on a per-project basis, rather than installing them across all projects for a specific machine or device. It uses a [global cache](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-cache.html) to store downloaded package metadata and contents. Once installed in a project, Unity treats [package assets](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-assets.html) similarly to other assets in the project. The only difference is that these assets are stored [inside the package folder](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-assets.html) and are **immutable** You cannot change the contents of an immutable (read-only) package. This is the opposite of **mutable**. Most packages are immutable, including packages downloaded from the package registry or by Git URL.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Immutable). You can permanently change content only from [Local](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Local) and [Embedded](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Embedded) package sources.
## Package sources
Sources describe where the package came from:
**Source** | **Description**  
---|---  
**Registry** | The Unity Package Manager downloads most packages from a package registry server into a [global cache](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-cache.html) on your computer as you request them. These packages are immutable, so you can use them in your project, but you can’t modify them or change their package manifests.  
**Built-in** | These packages allow you to enable or disable Unity features (for example, Terrain Physics, Animation, etc.). Built-in packages are immutable. For more information, refer to [Built-in packages](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-build.html) _Built-in_ packages allow users to toggle Unity features on or off through the Package Manager. Enabling or disabling a package reduces the run-time build size. For example, most projects don’t use the legacy Particle System. By removing the abstracted package of this feature, the related code and resources are not part of the final built product. Typically, these packages contain only the package manifest and are bundled with Unity (rather than available on the package registry).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Built-inpackage).  
**Embedded** | An [embedded package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-embed.html)An _embedded_ package is a mutable package that you store under the `Packages` directory at the root of a Unity project. This differs from most packages which you download from a package server and are immutable. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Embedded)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Embeddedpackage) is any package stored inside your project folder. This source corresponds with the [Custom](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-lifecycle.html#Develop) state because you typically put all the scripts, libraries, samples, and other assets your new package needs in a folder under your project folder when you begin development on a custom package.  
**Local** | You can [install a package from any folder](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-local.html) on your computer (for example, if you have cloned a development repository locally).  
**Tarball (local)** | You can [install a package from a tarball file](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-tarball.html) on your computer. The Package Manager extracts the package from the tarball and stores it in the cache. However, these packages are immutable, unlike installations from a local folder.  
**Git** | The Package Manager installs **Git** -based packages directly from a Git repository instead of from the package registry server.  
To edit the package manifest for a package, refer to [Inspecting packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-inspect.html).
The Package Manager window displays a label that corresponds to some of these sources. For more information, refer to [Labels](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html#Tags).
**Note** : The Package Manager stores packages that you download from the Asset Store in different caches, depending on the package type. 
## Additional resources
  * [Package types](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-package-types.html)
  * [Package states and lifecycle](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-lifecycle.html)
  * [Package dependency and resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-dependencies.html)
  * [Global cache](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-cache.html)
  * [Asset Store packages](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePackages.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages.html)
Get started with packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-overview.html)
How Unity works with packages
