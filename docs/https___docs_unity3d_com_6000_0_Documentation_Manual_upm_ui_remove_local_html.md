* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove-local.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Distribute assets as packages](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)
  * Remove local asset packages


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesImport.html)
Import local asset packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-optimizing.html)
Analyzing asset processes
# Remove local asset packages
When you import [local asset packages](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html), the Unity Editor places them in the `Assets` directory in your project.
You can manually remove assets from a project if you know the assets aren’t in use. You might consider this action to unclutter your project directory or to free up space on your local hard drive.
**Warning** : Make sure your project isn’t using any of the assets you remove. Unlike installed packages, the Package Manager doesn’t track assets that you imported from local **asset packages** A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Assetpackage), so it can’t detect when you remove dependent assets.
## Important: before you begin
  * Only use this procedure to remove assets added with the [Import local asset packages](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesImport.html) procedure. 
    * To remove **UPM packages** A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UPMpackage) installed from a registry, refer instead to [Remove a UPM package from a project](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove.html).
    * To remove asset packages downloaded and imported via the Package Manager window, refer instead to [Remove imported assets from a project](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove-asset.html).
  * This procedure removes assets from the current project. It doesn’t remove the same assets that might exist in other projects.


## Procedure
To remove one or more local asset package items from your project:
  1. Open the project you want to remove assets from.
  2. Open the **Package Manager** window and [select a context](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html#contexts) from the [navigation panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html).
  3. Select the package you want to remove from your project and take note of the package name **(A)** and the publisher name **(B)**. These names might help you identify the asset directory in a later step.
![The My Assets context shows the package name \(A\) and the publisher name \(B\)](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-ui-myassets-details.png) The **My Assets** context shows the package name (A) and the publisher name (B)
  4. Open the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow).
  5. Expand the `Assets` directory and locate the subdirectory for the package you identified in the **Package Manager** window in an earlier step.
  6. Explore the directory structure that the publisher created **(C)** , confirm it’s the correct package, and identify the assets you want to delete **(D)**. **Note** : Unity doesn’t impose directory names or structures on publishers, so their assets might not be in an easily identifiable directory. The directory structure might be simple or complex.
![The Project window with an assets folder selected \(C\) and its contents \(D\)](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/upm-proj-assets.png) The Project window with an assets folder selected (C) and its contents (D)
  7. Select the asset or assets you want to delete. Your selection can be a single asset, multiple assets, all assets in a subdirectory, or more.
  8. Right-click the selected items, and select **Delete**.


**Important** : **Scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) that depend on deleted assets aren’t reported as errors in the **Console window** A Unity Editor window that shows errors, warnings and other messages generated by Unity, or your own scripts. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Console.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Consolewindow). If you suspect the removal caused issues, import the package again. Refer to [Download and import an asset package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-import.html).
## Additional resources
  * [Remove a UPM package from a project](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove.html)
  * [Remove imported assets from a project](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-remove-asset.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesImport.html)
Import local asset packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-optimizing.html)
Analyzing asset processes
