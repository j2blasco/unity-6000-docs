* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * [Project Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)
  * Editor


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioManager.html)
Audio
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html)
Graphics
# Editor
Use the **Editor** settings to apply global settings for working in the Unity Editor. To access the Editor settings, go to **Edit** > **Project Settings** then select the **Editor** category. 
## Unity Remote
Unity Remote is deprecated. For most use cases, [Device Simulator package](https://docs.unity3d.com/Packages/com.unity.device-simulator@latest) replaces Unity Remote.
**Property** | **Description**  
---|---  
**Device** | Choose the device type you want to use for Unity Remote testing.   
[Unity Remote](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityRemote5.html)A downloadable app designed to help with Android, iOS and tvOS development. The app connects with Unity while you are running your project in Play Mode from the Unity Editor. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityRemote5.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UnityRemote) is a downloadable app designed to help with Android, iOS and tvOS development.  
**Compression** | Choose the type of image compression to use when transmitting the game screen to the device via Unity Remote. Choose from the following options: 
  * **JPEG** : Usually gives higher compression and performance, but the graphics quality is a little lower. This is the default option.
  * **PNG** : Gives a more accurate representation of the game display, but can result in lower performance.

  
**Resolution** | Choose the resolution the game runs at on Unity Remote: 
  * **Downsize** : Display the game at a lower resolution. This results in better performance, but lower graphical accuracy. This is the default option.
  * **Normal** : Display the game at normal resolution. This results in better graphical accuracy, but lower performance.

  
**Joystick Source** | Choose the connection source for the joysticks you’re using:
  * **Remote** : Use joysticks that connect to a device running Unity Remote. This is the default option.
  * **Local** : Use joysticks that connect to the computer running the Editor.

  
## Asset Serialization
**Property** | **Description**  
---|---  
**Mode** | Choose which format to use for storing serialized Assets. This is set to **Force Text** by default.   
Unity uses [serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization.html) to load and save assets and AssetBundles to and from your computer’s hard drive. To help with version control merges, Unity can store scene files in a [text-based format](https://docs.unity3d.com/6000.0/Documentation/Manual/TextSceneFormat.html). If you aren’t merging scenes, Unity can store scenes in a more space-efficient binary format, or allow both text and binary scene files to exist at the same time. Choose from the following formats:
  * **Mixed** : Assets in Binary mode remain in Binary mode, and Assets in Text mode remain in Text mode. Unity uses Binary mode by default for new assets.
  * **Force Binary** : Convert all assets to Binary mode, including new assets.
  * **Force Text** : Convert all assets to Text mode, including new assets. This is the default option.

  
**Reduce**version control** A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and PlasticSCM. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VersionControl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VersionControl) noise** | Forces the Editor to write references and similar YAML structures on one line, which reduces version control noise. When Unity reaches a line length of 80 characters it attempts to split the YAML data over multiple lines.  
## Build Pipeline
**Property** | **Description**  
---|---  
**Multi-process AssetBundle Building** | Enable improvements to the AssetBundle Build Pipeline to reduce build times with multi process importing. **Multi-process AssetBundle Building** provides more efficient incremental content building. To learn more, refer to [Multi-Process AssetBundle Building](https://docs.unity3d.com/6000.0/Documentation/Manual/Build-MultiProcess.html)  
## Default Behavior Mode
**Property** | **Description**  
---|---  
**Mode** | Choose the default [2D or 3D development](https://docs.unity3d.com/6000.0/Documentation/Manual/2DAnd3DModeSettings.html) mode. Unity sets up the certain default behaviors according to the mode you choose to make development easier: 
  * **3D** : Set Unity up for 3D development. This is the default option.
  * **2D** : Set Unity up for 2D development. 

  
## Asset Pipeline
**Property** | **Description**  
---|---  
**Remove unused Artifacts on Restart** | Enable to remove unused artifact files in the Library folder and remove their entries in the Asset Database. This setting is a form of garbage collection. Use this setting to disable the Asset Database garbage collection, so that previous artifact revisions which are no longer used are still preserved after you restart the Editor. This is useful if you need to debug unexpected import results. To learn more, refer to [Import Activity window](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportActivityWindow.html).  
**Parallel Import** | Use multiple processes to import assets simultaneously. By default, Unity imports assets one after another sequentially on the main Editor process. Parallel importing can be faster than the default sequential method of importing. To learn more, refer to [Importing assets simultaneously](https://docs.unity3d.com/6000.0/Documentation/Manual/ParallelImport.html)  
**Desired worker count** | Set the number of import worker processes that the import pipeline considers the optimal number to run in parallel.  
**Standby Import Worker Count** | Set the minimum number of worker processes to keep, even if they’re idle. If there are more worker processes than this, Unity shuts down import workers that have been idle for some time, to free up system resources. This property allows you to manage how Unity balances system resources when some processes are idle, compared with the time it takes to start up new import worker processes. You might see an improvement in import performance by increasing this value if you are frequently iterating on model, animation or texture work, and are therefore frequently importing batches of models or image files.  
**Idle Import Worker Shutdown Delay** | Set the amount of time in seconds to wait before shutting down an idle worker.  
**Exactly Match Referenced Clip Names** | Controls how referenced clips are matched with models animated in Legacy mode. When enabled, model names and referenced clip names must exactly match. When disabled, only the start of the model name must match the referenced clip name.  
## Cache Server (project specific)
Contains settings for [Unity Accelerator](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html).
**Setting** | **Description**  
---|---  
**Mode** | Choose whether to use the cache server. Choose from the following options: 
  * **Use global settings:** Uses the settings in the **Preferences** window (**Settings > Asset Pipeline > Unity Accelerator**).
  * **Enabled** : Enable the cache server.
  * **Disabled:** Disable the cache server.

  
**IP Address** | Input the **accelerator** The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Accelerator)’s IP address and port.  
**Check Connection** | Select **Check Connection** to test the connectivity of the accelerator.  
**Namespace prefix** | Set a custom namespace for the server.  
**Download** | Enable downloads from the cache server.  
**Upload** | Enable uploads from the cache server.  
**TLS/SSL** | Enable encryption on the cache server.  
**Authentication (Using Unity ID)** | Enable authentication for the cache server using Unity ID.  
**Content Validation** | Select the level of content validation: Disabled, Upload Only, Enabled, Required.  
**Download Batch Size** | Set the size of download.  
## Prefab Mode
**Property** | **Description**  
---|---  
**Allow Auto Save** | Enable an Auto Save toggle in **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) Mode which you can disable or enable. This is the default. When **Allow Auto Save** is disabled, there is no auto save in Prefab Mode in this project and the toggle doesn’t display. Refer to [Auto Save in Prefab Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingInPrefabMode.html#AutoSave) to learn more.  
**Regular Environment** | Assign a Scene as an editing environment in Prefab Mode for _regular_ Prefabs (that is, Prefabs with a regular [Transform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html) component). This allows you to edit your Prefab against a backdrop of your choosing rather than an empty Scene.  
Refer to [Editing a Prefab in Prefab Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingInPrefabMode.html) for more information.  
**UI Environment** | Assign a Scene as an editing environment in Prefab Mode for _UI_ Prefabs (that is, Prefabs with a [Rect Transform](https://docs.unity3d.com/Packages/com.unity.ugui@3.0/manual/class-RectTransform.html) component). This allows you to edit your Prefab against a backdrop of your choosing rather than an empty Scene.  
Refer to [Editing a Prefab in Prefab Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingInPrefabMode.html) for more information.  
## Graphics
**Property** | **Description**  
---|---  
**Use legacy**Light Probe** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) sample counts** | Use fixed Light Probe sample counts for baking with the Progressive **Lightmapper** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmapper). The sample counts are: 64 direct samples, 2048 indirect samples, and 2048 environment samples.  
## Sprite Atlas
**Property** | **Description**  
---|---  
**Mode** | Choose a mode to configure the [Sprite Atlas](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/atlas-landing.html)A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/v2-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteAtlas) tool: 
  * **Disabled** : Do not pack Sprite Atlases. This is the default setting.
  * **Sprite Atlas V1 - Enabled For Builds** : Pack Sprite Atlases for builds only. 
  * **Sprite Atlas V1 - Always Enabled** : Pack Sprite Atlases for builds and before entering Play mode. 
  * **Sprite Atlas V2 - Enabled** : Pack Sprite Atlases for both builds and before entering Play mode.
  * **Sprite Atlas V2 - Enabled For Builds** : Pack Sprite Atlases for builds only. 

  
## C# Project Generation
**Property** | **Description**  
---|---  
**Additional extensions to include** | Include a list of additional file types to add to the C# project. Separate each file type with a semicolon. By default, this field contains `txt;xml;fnt;cd;asmdef;rsp;asmref`.  
**Root namespace** | Fill in the namespace to use for the C# project `RootNamespace` property. Refer to [Common MSBuild Project Properties](https://docs.microsoft.com/en-us/visualstudio/msbuild/common-msbuild-project-properties?view=vs-2022) for more information. This field is blank by default.  
## Texture Compressors
**Property** | **Description**  
---|---  
**BC7 Compressor** | Select the compressor to use for BC7 format texture **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression).  
**ETC Compressor** | Select the compressors to use for different compression qualities of ETC Textures.  
The compression tools available are [etcpak](https://bitbucket.org/wolfpld/etcpak/wiki/Home), [ETCPACK](https://github.com/Ericsson/ETCPACK) and [Etc2Comp](https://github.com/google/etc2comp). These are all third-party compressor libraries. Choose from the following:
  * **Legacy** : Use the configuration that was available before ETC Texture compression became configurable. This sets the following properties: **Fast** : ETCPACK Fast, **Normal** : ETCPACK Fast, **Best** : ETCPACK Best
  * **Default** : Use the default configuration for Unity. This sets the following properties: **Fast** : etcpack, **Normal** : ETCPACK Fast, **Best** : Etc2Comp Best.
  * **Custom** : Customize the ETC Texture compression configuration. When you choose this option, the **Fast** , **Normal** , and **Best** properties are enabled. This maps to the **Compressor Quality** setting in the [Texture Importer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html) for the supported platforms.

  
**Fast** | Define the compression quality tool to use for Fast compression. This property is modifiable only when **ETC Compressor** is set to **Custom**.  
**Normal** | Define the compression quality tool to use for Normal compression. This property is modifiable only when **ETC Compressor** is set to **Custom**.  
**Best** | Define the compression quality tool to use for Best compression. This property is modifiable only when **ETC Compressor** is set to **Custom**.  
## Line Endings For New Scripts
**Property** | **Description**  
---|---  
**Mode** | Choose the file line endings to apply to new scripts created within the Editor. Note that configuring these settings does not convert existing scripts. Choose from the following: 
  * **OS Native** : Apply line endings based on the operating system the Editor is running on.
  * **Unix** : Apply line endings based on the Unix operating system.
  * **Windows** : Apply line endings based on the Windows operating system. 

  
## Texture Streaming Settings
If you enable Mipmap Streaming in the Editor for one mode but not the other, entering and exiting Play mode takes slightly longer. Enabling Mipmap Streaming for both modes prevents Unity from unloading and reloading mipmap data, and increases the speed of entering and exiting Play Mode.
**Property** | **Description**  
---|---  
**Enable Mipmap Streaming in Play Mode** | Enable [Mipmap Streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html) in Play mode.   
  
The **Texture Mipmap Streaming** setting in the [Quality](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html) project settings must also be enabled.  
  
Play mode might take longer to open and close if you enable this setting and disable **Enable Mipmap Streaming in Edit Mode**.  
**Enable Mipmap Streaming in Edit Mode** | Enable Mipmap Streaming in Edit Mode.   
  
The **Texture Mipmap Streaming** setting in the [Quality](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html) project settings must also be enabled.   
  
Play mode might take longer to open and close if you enable this setting but disable **Enable Mipmap Streaming in Play Mode**.  
**Load texture data on demand** | Load CPU-side texture data from disk asynchronously on demand to avoid some stalls and reduce CPU memory usage. If you enable mipmap streaming, this setting requires more processing time on the CPU, and might cause textures to temporarily appear at a lower resolution while Unity loads a higher resolution mipmap level from disk.  
## Shader Compilation
**Property** | **Description**  
---|---  
**Asynchronous**Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) Compilation** | Enable this checkbox to make Unity compile shaders in the background. While compiling, the Unity engine uses a placeholder Shader to render geometry in the Editor. When Shader compilation has finished, the engine swaps your Shader Variant back in. This means the Editor runs seamlessly, without having to wait for the Unity engine to compile every single Shader variant before rendering. For more information, refer to [Asynchronous Shader compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation.html).  
## Enter Play Mode Settings
**Property** | **Description**  
---|---  
**When entering play mode** | Select which reload options to start when you enter Play mode. [Domain reloading](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html) is when the Editor resets the scripting state before it starts Play mode. [Scene reloading](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-reloading.html) is when the Editor destroys all scene GameObjects and reloads the scene from disk before Play mode starts. To enter Play mode faster, you can disable [scene](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-reloading.html)A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) or [domain](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html) reloads. To learn more, refer to [Details of disabling Domain and Scene Reload](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode-details.html). Choose from the following options: 
  * **Reload Domain and Scene** : Reload both the [domain](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html) and [scene](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-reloading.html) when you enter Play mode. **Reload Domain and Scene** is enabled by default.
  * **Reload Scene Only** : Reload the [scene](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-reloading.html) and do not reload the [domain](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html) when you enter Play mode.
  * **Reload Domain Only** : Reload the [domain](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html) and do not reload the [scene](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-reloading.html) when you enter Play mode. 
  * **Do not reload Domain or Scene** : Do not reload either the [scene](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-reloading.html) or [domain](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html) when you enter Play mode.

  
## Numbering Scheme
**Property** | **Description**  
---|---  
**Game Object Naming** | Naming scheme for duplicated **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). Duplicated or instantiated GameObjects are named by appending successive numbers to the original object name.  
**Game Object Digits** | Sets the amount of digits to use for duplicated GameObject numbers.  
**Space Before Number in Asset Names** | Controls whether to insert a space before a number in duplicated Asset names.  
## Inspector
**Property** | **Description**  
---|---  
**Use IMGUI Default**Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** | Revert to using IMGUI to generate Default Inspectors where no custom Inspector or Editor is defined.  
## Additional resources
  * [Project Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings)
  * [Unity Remote](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityRemote5.html)
  * [Script serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization.html)
  * [2D and 3D mode settings](https://docs.unity3d.com/6000.0/Documentation/Manual/2DAnd3DModeSettings.html)
  * [Importing assets simultaneously](https://docs.unity3d.com/6000.0/Documentation/Manual/ParallelImport.html)
  * [Preferences](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html)
  * [Transforms](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html)
  * [Cookies](https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies.html)
  * [Progressive Lightmapper](https://docs.unity3d.com/6000.0/Documentation/Manual/progressive-lightmapper.html)
  * [Multi-Process AssetBundle Building](https://docs.unity3d.com/6000.0/Documentation/Manual/Build-MultiProcess.html)
  * [The Mipmap Streaming system](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html)
  * [Asynchronous Shader compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation.html)
  * [Sprite Atlas V2](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/v2-landing.html)


EditorManager
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioManager.html)
Audio
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html)
Graphics
