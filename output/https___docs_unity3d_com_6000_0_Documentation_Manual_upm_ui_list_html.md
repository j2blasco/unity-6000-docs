* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [The Package Manager window](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui.html)
  * List panel reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html)
Navigation panel reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-sort.html)
Sort the package list
# List panel reference
The Package Manager window displays the list of feature sets, packages, or **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore) packages that meet your criteria.
You set the criteria by selecting a context in the [navigation panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html), and by optionally setting additional filter and search criteria.
For important information about the way search works, refer to [Search box](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-search.html).
![The image on the left displays features sets and packages installed in your project, and the image on the right displays packages from My Assets](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-ui-list.png) The image on the left displays features sets and packages installed in your project, and the image on the right displays packages from **My Assets**
**(A)** [Feature sets](https://docs.unity3d.com/6000.0/Documentation/Manual/FeatureSets.html)A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/FeatureSets.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Featureset) appear at the top of the list panel when you select the **Unity Registry** or **In Project** contexts. Feature sets are indicated with the feature set icon (![Icon showing layers of items](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconPkg.png)). Toggle the expander icon (![Right-pointing triangle](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconCollapsed.png)) to expand or collapse (![Down-pointing triangle](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconExpanded.png)) the list of feature sets. When you select a feature set from the list, [details about it appear on the right](https://docs.unity3d.com/6000.0/Documentation/Manual/fs-details.html). These details include a brief description, a list of included packages, and a link to the **QuickStart** guide for that feature set.
**(B)** Asset Store packages appear in the **In Project** list for all packages you added to your project from the **My Assets** list.
**(C)** Registry groups organize the list of packages installed in your project or available for installation. The list has separate groups for packages that come from Unity’s registry and other scoped registries you installed in your project. Select the expander on the left to expand (![Right-pointing triangle](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconCollapsed.png)) or collapse (![Down-pointing triangle](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconExpanded.png)) the list of packages for each registry.
**(D)** The installed or imported version of the package. If the package isn’t installed or imported yet, the listed version varies by package format:
  * For **UPM packages** A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UPMpackage), the list view displays the recommended version. If a recommended version doesn’t exist, the list view displays the latest version.
  * For **asset packages** A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Assetpackage) (`.unitypackage` format), the list view displays the latest of version of the package, unless you downloaded the package but didn’t import it, in which case the downloaded version displays.


The following icons appear beside the version number for packages whose [state](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-lifecycle.html) isn’t [Released](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-safe.html): 
  * ![Pre-release icon](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconPre.png) [Pre-release](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-preview.html)
  * ![Experimental icon](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconExp.png) [Experimental](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-exp.html)
  * ![Custom icon](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconCustom.png) [Custom](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Embedded) (embedded)


For packages from the Asset Store, the version that appears is either the version you already downloaded or the version that’s available for download from the Asset Store.
**(E)** These icons display the status of the package:
**Icon** | **Description**  
---|---  
![Check mark](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconCheck.png) | A check mark indicates that the package or feature set is already [installed](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-install.html), [enabled](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-disable.html), or [imported](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-import.html).  
![Upward pointing arrow](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconUpdate.png) | The update icon indicates that the package has an available update. To update your package, follow the appropriate instructions based on the package type:  
  
- For Unity Package Manager (UPM) packages, refer to [Switch to another version of a UPM package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-update.html).   
- For asset packages, refer to [Update an asset package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-update2.html).  
- You can’t update feature set versions because they’re fixed to the Editor version.  
![Lock icon](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconLock.png) | The lock icon indicates a package that’s installed as part of a feature set.  
![Link icon](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconDependency.png) | The link icon indicates a package that’s installed as a dependency.  
![Folder with plus sign](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconImport.png) | The import icon indicates that there’s an asset package available to import.  
![Downward pointing arrow](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconDownload.png) | The download icon indicates that there’s an asset package available to download.  
![Warning icon](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconWarning.png) | A warning icon indicates an issue with the package, such as [lifecycle deprecation](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-deprecated.html).  
![Stop icon](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconError.png) | An error icon indicates [package version deprecation](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-deprecated.html) or an issue that occurred during installation or loading. For information about resolving errors, refer to [Package Manager troubleshooting](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-errors.html).  
**(F)** The **My Assets** context displays a counter showing the number of packages from the Asset Store that are available but not shown in the list. To load more packages from the Asset Store , click the **Load** link.
**Note** : If you select the **My Assets** context but the Package Manager window doesn’t list any packages, refer to [Error messages in the Package Manager window](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-errors.html#Errors) for an explanation and solution.
**(G)** The [status bar](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui.html#StatusBar) displays messages about the package load status and network warnings.
**(H)** Click the **reload** ![Reload button](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconReload.png) button to force the Package Manager to reload your packages and feature sets.
By default, the Package Manager window displays the list of all packages and feature sets available in the selected context, but you can [filter](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-find.html) the list to display packages and feature sets that meet your criteria.
You can also [include pre-release packages](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html#advanced_preview) in the list and [search](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-search.html) for a specific package or feature set by [name (ID)](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html#name) or [display name](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html#displayName).
## Additional resources
  * [Package types](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-package-types.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html)
Navigation panel reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-sort.html)
Sort the package list
