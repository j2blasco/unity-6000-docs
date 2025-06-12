* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * Introduction to assets in Unity


[](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
Assets and media
[](https://docs.unity3d.com/6000.0/Documentation/Manual/import-assets.html)
Importing assets
# Introduction to assets in Unity
An asset is any item that you use in your Unity project to create your application, such as textures, 3D models, or sound files. Assets can include:
  * ****Visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement)**: 3D models, textures, or **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite).
  * **Audio elements** : Sound effects or music.
  * **Abstract items** : Color gradients, animation masks, arbitrary text, or numeric data.


## Importing assets
To use assets in Unity, you must [import them into your project](https://docs.unity3d.com/6000.0/Documentation/Manual/import-assets.html). You can [add assets to the `Assets` folder](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingAssets.html) of your project, or [use scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptedImporters.html) to import assets automatically. 
Unity supports a wide range of asset formats. For more information, refer to [Supported asset type reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html).
If you’re working on a complex project with a large team of people, you can use the [Unity Accelerator](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html) cache server to speed up asset management. 
## How Unity manages assets
Unity uses the [Asset Database](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabase.html) to store the assets in your project and maintain consistency between the original source files and their imported versions used by your application at runtime. You can use the [Import Activity window](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportActivityWindow.html) to inspect how Unity imports the assets in your project. 
## Grouping assets together
You can use [AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-section.html) to group together assets in an archive file format, which you can then use to update assets remotely, or provide DLC content for your application.
You can also use [asset packages](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Assetpackage) to package assets together to share between other Unity projects.
## Managing assets through scripts
You can perform many of the loading, importing, and unloading operations that Unity does with the [Asset Database APIs](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabaseCustomizingWorkflow.html).
An alternative method of managing loading assets is with the [Resources system](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingResourcesatRuntime.html), but it can impact on the performance of your application. 
The [Addressables package](https://docs.unity3d.com/Packages/com.unity.addressables@latest) provides a streamlined workflow for managing asset loading at runtime and is the recommended system for organizing assets in Unity projects.
## Additional resources
  * [Supported asset type reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html)
  * [Introduction to Unity Accelerator](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html)
  * [Programming with the Asset Database](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabaseCustomizingWorkflow.html)
  * [Introduction to AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundlesIntro.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
Assets and media
[](https://docs.unity3d.com/6000.0/Documentation/Manual/import-assets.html)
Importing assets
