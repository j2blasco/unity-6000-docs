* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SpecialFolders.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Importing assets](https://docs.unity3d.com/6000.0/Documentation/Manual/import-assets.html)
  * Reserved folder name reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html)
Supported asset type reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-caching-assets.html)
Caching assets
# Reserved folder name reference
Every Unity project has an `Assets` folder in the project root which contains the project’s [assets](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset). The [Project window](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow) displays the contents of the `Assets` folder.
Some limitations apply when choosing names for new folders. There are some names for subfolders of the `Assets` folder that Unity reserves for certain subtypes of assets, and which have special compilation significance or are used to categorize assets for the Editor or Player. These folder names and their meaning are detailed in the following table.
Folder name | Description  
---|---  
`Editor` | Reserved for Editor scripts, which add functionality to the Unity Editor at authoring time but aren’t available in Player builds at runtime. An alternative to placing scripts in a folder called `Editor` is to [create an assembly definition asset](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-creating.html) for Editor code. The exact location of an `Editor` folder determines the script compilation order of its contents. For more information, refer to [Special folders and script compilation order](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compile-order-folders.html).  
**Maximum number of folders with this name per project:** Unlimited  
**Valid location for folder** : Root of the `Assets` folder or any of its subfolders.  
**Place relevant assets in** : `Editor` folder or any of its subfolders.  
  
**Note:** MonoBehaviour scripts in an `Editor` folder can’t be attached to GameObjects as components.  
`Editor Default Resources` | Reserved for asset files that Editor scripts can load on-demand using [EditorGUIUtility.Load](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.Load.html).  
**Maximum number of folders with this name per project:** 1  
**Valid location for folder** : Root of the `Assets` folder only.  
**Place relevant assets in** : `Editor Default Resources` folder or any of its subfolders.  
  
**Note** : Always include the subfolder path in the path passed to [EditorGUIUtility.Load](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.Load.html) if your asset files are in subfolders.  
`Gizmos` | Reserved for image files used by the [Gizmos.DrawIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawIcon.html) function to draw icons in a **Scene** view. For more information, refer to [Gizmos and Handles](https://docs.unity3d.com/6000.0/Documentation/Manual/gizmos-and-handles.html).  
**Maximum number of folders with this name per project:** 1  
**Valid location for folder** : Root of the `Assets` folder only.  
**Place relevant assets in** : `Gizmos` folder or any of its subfolders.  
  
**Note** : Always include the subfolder path in the path passed to the [Gizmos.DrawIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawIcon.html) function if your asset files are in subfolders.  
`Resources` | Reserved for assets to load on-demand from a script at application runtime rather than creating references to assets in a scene. For more information, refer to [Loading Resources at Runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingResourcesatRuntime.html).  
**Maximum number of folders with this name per project:** Unlimited  
**Valid location for folder** : Root of the `Assets` folder or any of its subfolders.  
**Place relevant assets in** : `Resources` folder or any of its subfolders.  
  
**Note** : Always include the subfolder path in the path passed to the [Resources.Load](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html) function if your asset files are in subfolders. Assets in a `Resources` folder increase the size of Player builds and assets not required at runtime must be manually cleaned up to prevent them degrading your application’s performance. For more information, refer to [The Resources folder](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingResourcesatRuntime.html).  
`Plugins` | Reserved for third-party plugins. For platform-specific information on valid folder path patterns, refer to [Import and configure plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-in-inspector.html).  
`StreamingAssets` | Reserved for asset files that should be available in their original format at runtime for streaming. For more information, refer to [Streaming Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/StreamingAssets.html).  
**Maximum number of folders with this name per project:** 1  
**Valid location for folder** : Root of the `Assets` folder only.  
**Place relevant assets in** : `StreamingAssets` folder or any of its subfolders.  
## Platform-specific folders
For information on folder name formats and extensions which denote **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) or asset types specific to particular platforms, refer to [Platform development](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html).
## Hidden assets
During the [import](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingAssets.html) process, Unity ignores the following files and folders in the `Assets` folder and its subfolders:
  * Hidden folders.
  * Files and folders which start with `.`, except for those under `StreamingAssets` where this pattern is not ignored.
  * Files and folders which end with `~`.
  * Files and folders named `cvs`.
  * Files with the extension `.tmp`.


This prevents importing special and temporary files created by the operating system or other applications.
**Note** : For folders created through the Editor’s create menu, the Editor automatically converts a dot (`.`) prefix into an underscore (`_`) prefix to prevent crashes. For example, a folder created in the Editor and named `.folder` is automatically renamed `_folder`. If you want to name a folder with a dot prefix, create it directly in your local file system instead. 
## Additional resources
  * [Script compilation order](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compile-order-folders.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html)
Supported asset type reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-caching-assets.html)
Caching assets
