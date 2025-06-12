* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/asset-database-contents.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Managing assets with the Asset Database](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabase.html)
  * Contents of the Asset Database


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabase.html)
Managing assets with the Asset Database
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabaseRefreshing.html)
Refreshing the Asset Database
# Contents of the Asset Database
Unity’s Asset Database keeps track of assets in your project to ensure the original asset source file and its imported counterpart remain in sync.
## Source assets and artifacts
On import, Unity converts most asset types from their original format to one optimized for use at runtime. The original file is referred to as the source asset and its imported counterpart is called an artifact. Unity converts source asset files to artifacts to make them easier to author within the Editor and easier for hardware to consume at runtime.
Artifacts have a serializable C# class representation that inherits from [`UnityEngine.Object`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.Object.html), so you can access their properties and work with them in code. For example, imported PNG files are converted to serialized instances of the [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture) class, which inherits from `UnityEngine.Object`. This is the object you access when you interact with the Texture in code.
The difference between the source asset file and the artifact is bigger for some asset types than others. Some types of asset files Unity creates, such as **.**prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab)**, **.**scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)**, **.asset** , and **.mat** , already contain serialized data in their source file, so the artifact file Unity produces is similar to the source file. These file types are human-readable if [Asset Serialization Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html) is set to the default setting of **Force Text** , whereas binary files such as textures or audio are usually not.
Each artifact file name is a GUID with no file extension. Unity separates these files into subfolders, and each subfolder has a name that matches the first two characters of the artifact filename. These artifact files contain binary data, and are not designed to be human-readable. While it’s useful to understand that these files contain the data used by the Asset Database, you don’t need to view, edit, or use these files directly.
The [metadata file](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetMetadata.html) which Unity creates during the import process, stored next to the original asset file, contains the asset’s import settings, and contains a GUID which allows Unity to connect the original asset file with the artifact in the asset database.
You can view the artifacts produced for the assets in your project in the [Import Activity window](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportActivityWindow.html).
## Asset Database structure
The Asset Database consists of the following database files in the `Library` folder:
  * The source Asset Database (`Library\SourceAssetDB`): Contains meta-information about your source asset files which Unity uses to determine whether the file has been modified, and therefore whether it should reimport the files. This includes information such as last modified date, a hash of the file’s contents, GUIDs, and other meta-information.
  * The Artifact database (`Library\ArtifactDB`): Contains information about the import results of each source asset. Each artifact contains the import dependency information, artifact meta-information and a list of artifact files.


**Note:** Make sure to exclude these database files from **version control** A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and PlasticSCM. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VersionControl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VersionControl) systems.
## Asset caching and dependencies
The Asset Database keeps track of all the dependencies for each asset and caches artifacts. Artifacts are treated as cached data because Unity can always regenerate them from the source assets, using the import settings and **project settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings) saved in your project.
An asset’s import dependencies include all the data that might influence the imported data. If an imported asset’s source file or any of its dependencies change, then Unity reimports the file and updates the imported version of the data.
For more information on what constitutes an asset’s dependencies and the refresh process, refer to [Refreshing the Asset Database](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabaseRefreshing.html).
If you’re working in a team, every team member’s copy of Unity performs the import process if an asset or dependency changes, which can be time consuming. Unity provides a solution to this called Unity **Accelerator** The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Accelerator). For more information, refer to [Caching assets](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-caching-assets.html).
## Asset reimport on platform change
Changing the active [target platform](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html) can cause Unity to reimport your assets. This usually happens when the way the asset is imported differs between platforms, which is often the case. For example, different platforms have different **texture formats** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat), so textures are imported differently for each platform.
The results for importing your assets on different platforms are stored as separate pieces of cached data. The platform is part of the hash the Asset Database uses to store the import results for Unity’s [built-in importers](https://docs.unity3d.com/6000.0/Documentation/Manual/BuiltInImporters).
When you change to a different platform, any assets in your project that haven’t already been imported for the new platform are reimported. However, the new reimported data does not overwrite the old cached import data for the previous platform. When you switch back to a platform you’ve already imported assets for, those asset import results are already cached and ready to use, making the switch back faster.
## Additional resources
  * [Refreshing the Asset Database](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabaseRefreshing.html)
  * [Programming with the Asset Database](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabaseCustomizingWorkflow.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabase.html)
Managing assets with the Asset Database
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabaseRefreshing.html)
Refreshing the Asset Database
