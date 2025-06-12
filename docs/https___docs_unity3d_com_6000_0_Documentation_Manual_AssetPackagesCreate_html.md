* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesCreate.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Distribute assets as packages](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)
  * Create and export asset packages


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)
Distribute assets as packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesImport.html)
Import local asset packages
# Create and export asset packages
To share **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), samples, tools, or other assets, you can export them as an **asset package** A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Assetpackage) in the `.unitypackage` format. Asset packages are a convenient way to copy several assets or an entire scene from one project to another quickly, with little additional overhead.
If you want to distribute assets in a more formal way with long-term support, a defined structure, and semantic versioning, an alternative option is to [create your own Unity package](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomPackages.html).
**Note** : If the assets in your asset package are high quality and other users might find them useful, refer to [Publishing to the Asset Store](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePublishing.html) for information on how to create a package draft and upload it to the **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore).
To create and export an asset package:
  1. Open the project you want to export assets from.
  2. Go to the **[Project](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html) In Unity, you use a project to design and develop a game. A project stores all of the files that are related to a game, such as the asset and Scene files. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/2Dor3D.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Project)** window and select one or more items or folders. These items become the starting list for your export. You can also select the `Assets` folder to include all assets as your starting point.
  3. Choose **Assets** Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset) > **Export Package** from the menu to open the **Exporting package** dialog.
  4. In the dialog, select the checkboxes for the assets you want to include in the package.
  5. Enable the **Include dependencies** checkbox to automatically select any assets (including scripts) used by the assets you select.
  6. Enable the **Include all**scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts)** checkbox to export all scripts from your project.
If you disable **Include all scripts** but enable **Include dependencies** , Unity only exports scripts that your selected items directly depend on. Unity can’t trace the full chain of dependencies for your scripts, so enabling **Include all scripts** reduces the likelihood of compilation errors when using the exported package in another project.
  7. Click **Export** to bring up the file explorer and choose where you want to store your package file.
  8. Name and save the package.


## Re-exporting asset packages
To create a new version of your asset package with updated contents, perform the export procedure again and select the changed and unchanged files to include in the new version.
### Naming strategies
Name your updated package using incremental names suffixed with a version identifier, for example `MyAssetPackageVer1`, `MyAssetPackageVer2`, and so on. Unity recognizes these as updates of the same package. Use a naming convention that’s clear for you and anyone you share it with.
**Warning:** Don’t remove files from asset packages and then add different files with the same name. If you remove a file and later replace it, use a unique name for the replacement file. Attempting to reuse previously used file names can confuse Unity’s system for tracking assets and produce warnings on import. For more information, refer to [Asset metadata](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetMetadata.html).
## Additional resources
  * [Create custom packages](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomPackages.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)
Distribute assets as packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesImport.html)
Import local asset packages
