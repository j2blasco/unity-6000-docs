* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove-asset.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Package management with the Package Manager window](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-packages-window.html)
  * [Add and remove asset packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions-ap.html)
  * Remove imported assets from a project


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-update2.html)
Update an asset package
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-del-pkg-as-cache.html)
Delete an asset package from the cache
# Remove imported assets from a project
When you import an **asset package** A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Assetpackage) from the **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore), the Unity Package Manager places the package’s assets in the `Assets` directory in your project.
You can remove assets from a project if you know the assets aren’t in use. You might consider this action to unclutter your project directory or to free up space on your local hard drive.
**Warning** : Make sure your project isn’t using any of the assets you remove.
## Before you begin
Make sure you understand these important notes before you begin:
  * Use this procedure to remove assets only if they came from an asset package and you imported them by following the [Download and import an asset package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-import.html) procedure. 
    * Don’t use this procedure to try to remove UPM packages that you installed. Installed UPM packages can come from a registry, but they can also come from the Asset Store. For information about removing UPM packages that you installed, refer to [Removing a UPM package from a project](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove.html).
    * Don’t use this procedure to try to remove assets that you imported after exporting them to a local asset package. For information about removing assets that you imported from a local asset package, refer to [Removing local asset packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove-local.html).
  * This procedure removes assets from the current project. It doesn’t remove the same assets that might exist in other projects. It also doesn’t remove asset packages from the cache. To completely remove an asset package and its assets from your computer, you must remove them from multiple locations: 
    1. Use the following procedure to remove the assets from each project that uses them.
    2. Delete this asset package from the cache. Refer to [Delete an asset package from the cache](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-del-pkg-as-cache.html).


## Procedure
To remove imported assets from your project:
  1. Open your project.
  2. Open the **Package Manager** window and select **My Assets** or **In Project** from the [navigation panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html).
  3. Select the asset package whose assets you want to remove from your project. 
  4. Open the menu in the top right corner of the [details panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html).
![The action menu in Package Managers details panel](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-ui-details-menu.png) The action menu in Package Manager’s details panel
  5. Select **Remove assets from project** to open the **Remove** dialog.
![The Remove dialog](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-ui-remove-assets.png) The **Remove** dialog
  6. Select the assets to remove. You can remove all assets with **All** , or you can select a subset of assets by using the checkboxes.
  7. Select **Remove**.


**Important** : 
  * **Scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) that depend on deleted assets aren’t reported as errors in the **Console** window. If you suspect the removal caused issues, import the package again. Refer to [Download and import an asset package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-import.html).
  * Assets that you remove from your project remain in the [My Assets list](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html). To remove asset packages from **My Assets** , refer to [Delete an asset package from the cache](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-del-pkg-as-cache.html).


If you deleted a subset of assets, you can view a list of the remaining assets by selecting the **Imported Assets** tab in the [details panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html).
![The Imported Assets tab in the Details panel](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-ui-imported-assets.png) The **Imported Assets** tab in the Details panel
## Additional resources
  * [Package types](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-package-types.html)
  * [Remove a UPM package from a project](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove.html)
  * [Delete an asset package from the cache](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-del-pkg-as-cache.html)
  * [Removing local asset packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove-local.html)
  * [Download and import an asset package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-import.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-update2.html)
Update an asset package
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-del-pkg-as-cache.html)
Delete an asset package from the cache
