* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingAssets.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Importing assets](https://docs.unity3d.com/6000.0/Documentation/Manual/import-assets.html)
  * Introduction to importing assets


[](https://docs.unity3d.com/6000.0/Documentation/Manual/import-assets.html)
Importing assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetMetadata.html)
Asset metadata
# Introduction to importing assets
When you create a Unity project, Unity creates a folder for your project which contains an `Assets` subfolder. You can use this folder to store assets created outside of Unity to then use in your project.
## Using the Assets folder
You can either export the asset file directly into the `Assets` folder, or copy it into the folder. For many common formats, you can save the source file directly into your project’s `Assets` folder and Unity can read it. Unity also detects when you save new changes to the file and re-imports files as necessary.
For a list of supported asset types, refer to [Supported asset type reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html).
### Managing assets in the Project window
Use the [Project window](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow) to view the contents of your `Assets` folder. Whenever you save or copy a file to your `Assets` folder, Unity imports it and it then appears in your Project window. If you drag a file from your computer’s file browser into Unity’s Project window, Unity makes a copy and places it into your `Assets` folder. You can then access this copy from the Project window.
**Warning:** Usually, the items that appear in your Project window represent actual files on your computer. If you delete them in the Project window, you also delete them from your computer.
![The Project window with the Assets folder opened, containing food related models.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/importing-project-window.png) The Project window with the Assets folder opened, containing food related models.
### Modifying asset files
When you modify a file in Unity, Unity doesn’t modify your original source file. Instead, the import process reads your source file, and creates a representation of your asset internally, which matches your chosen [import settings](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingAssets.html#asset-import-settings). If you modify the import settings for an asset, or make a change to the source file in the `Assets` folder, Unity re-imports the asset again to reflect your changes. 
If you want to move or rename assets in your project, it’s best practice to do it in the Project window. Unity then automatically moves or renames the asset’s corresponding `.meta` file. For more information on .meta files, refer to [Asset metadata](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetMetadata.html).
If you drag a file from your computer’s file browser into Unity’s Project window, Unity makes a copy and places it into your `Assets` folder. You can then access this copy from the Project window. 
### Complex assets
If you import a single asset file that contains complex information, Unity might create multiple assets from it. For example:
  * If a 3D file (such as an FBX file) defines materials or contains embedded textures, Unity extracts the [materials and embedded textures](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Materials.html) as separate assets.
  * If you want to import an image file as multiple 2D **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite). Use the 2D [Sprite Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html) to define multiple sprites from a single graphic image and Unity displays each sprite as a separate sprite asset in the Project window.
  * If a 3D file contains multiple animation timelines or multiple clips, Unity automatically defines separate animation timelines or clips based on its [animation import settings](https://docs.unity3d.com/6000.0/Documentation/Manual/Splittinganimations.html). The resulting multiple animation clips appear as separate **Animation Clip** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) assets in the Project window.


## Asset processing
Unity reads and processes any files that you add to the `Assets` folder and converts the contents of the file to internal data that’s correctly formatted for your application’s target platform. The source asset files remain unchanged, and Unity stores the internal data in the project’s `Library` folder. This data is part of Unity’s [Asset Database](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabase.html).
Unity uses internal formats for assets so it can use versions of your assets at runtime in the Unity Editor, and can keep your unmodified source files in the `Assets` folder. This system means that you can edit an asset file and the Editor picks up the changes automatically. For example, hardware such as mobile devices can’t convert `.psd` files directly to render them as textures. When you place a `.psd` file in the `Assets` folder, Unity converts the file to an internal version that mobile devices can process.
Unity stores the internal representation of your assets in the `Library` folder, which behaves like a cache folder. You don’t need to ever alter the `Library` folder manually, and if you do, you might negatively affect your project. This also means that you don’t need to include the `Library` folder under **version control** A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and PlasticSCM. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VersionControl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VersionControl).
**Tip:** If your project isn’t open, you can safely delete the `Library` folder, because Unity can regenerate all its data from the `Assets` and `ProjectSettings` folders the next time you launch your project.
## Asset import settings
Each type of asset that Unity supports has a set of import settings, which affect how the asset appears or behaves. To view an asset’s import settings, select the asset in the Project window. The import settings for the selected asset appear in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector). The options that appear vary depending on the type of asset selected.
![A selected models Inspector window with its Import Settings displayed.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/importing-model-import-settings.png) A selected model’s Inspector window with its Import Settings displayed.
For more information, refer to the documentation on the following Import Settings:
  * [Model Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html)
  * [SketchUp Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SketchUpImporter.html)
  * [SpeedTree Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SpeedTreeImporter.html)
  * [Texture Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)
  * [Cubemap texture Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cubemap.html)
  * [Animation Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)
  * [Assembly Definition Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AssemblyDefinitionImporter.html)
  * [Audio Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)


If you’re developing a cross-platform project, you can override the default settings and assign different import settings on a per-platform basis.
## Reusing assets between projects
As you build your application, [Unity stores metadata](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetMetadata.html) about your assets, such as import settings and links to other assets, among other information. If you want to transfer your assets into a different project and preserve all this information, you can export your assets into one of the following containers:
  * An [asset package](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Assetpackage), which you can create directly in the Editor.
  * A [custom package](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomPackages.html), which you can access and manage inside the [Package Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages.html).


## Additional resources
  * [Asset packages](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)
  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html)
  * [Textures and videos](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html)
  * [Sprite Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html)
  * [Audio files](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioFiles.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/import-assets.html)
Importing assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetMetadata.html)
Asset metadata
