* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-package-types.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Get started with packages](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages.html)
  * Package types


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-overview.html)
How Unity works with packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-lifecycle.html)
Package states and lifecycle
# Package types
Unity’s Package Manager supports two package types:
  * **UPM packages** A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UPMpackage) (Unity Package Manager built-in format).
  * **Asset packages** A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Assetpackage) (`.unitypackage` format).


The following table compares the differentiating characteristics of these package types:
**Characteristic** | **UPM packages** | **Asset packages**  
---|---|---  
Format | Collection of files and folders, which might be compressed, depending on the distribution method. | A compressed file with a `.unitypackage` extension.  
Primary source for the package | Unity registry, scoped registry, or **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore) | Asset Store  
Uses a [package manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html)Each package has a _manifest_ , which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Packagemanifest) file | Yes | No  
UI action for adding the package to a project | Install | Download and import  
Project folder the package is added to | `Packages` | `Assets`  
Cache the package is added to | [Global cache](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-cache.html) | Asset package cache. Refer to [Location of downloaded asset package files](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePackages.html#asset-location).  
You can manually remove the package from the cache | No | Yes  
Sets of tabs that appear in the [Details panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html) | Description, Version History, Dependencies, Samples (if provided), Images (if provided) | Overview, Releases, Imported Assets, Images  
## Additional resources
  * [Add and remove UPM packages or feature sets](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions.html)
  * [Add and remove asset packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions-ap.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-overview.html)
How Unity works with packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-lifecycle.html)
Package states and lifecycle
