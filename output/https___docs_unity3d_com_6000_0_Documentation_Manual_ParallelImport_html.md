* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ParallelImport.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Importing assets](https://docs.unity3d.com/6000.0/Documentation/Manual/import-assets.html)
  * Import assets simultaneously


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetMetadata.html)
Asset metadata
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptedImporters.html)
Managing importers with scripts
# Import assets simultaneously
By default, Unity imports assets one after another sequentially on the main Unity Editor process. However, you can use the **Parallel Import** setting to import certain texture and **model files** A file containing a 3D data, which may include definitions for meshes, bones, animation, materials and textures. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Modelfile) simultaneously. The **Parallel Import** setting uses multiple processes to import assets simultaneously, which is faster than the default sequential method of importing.
## Supported file types
The **Parallel Import** setting supports only certain types of asset. The specific types of asset which Unity can import in parallel are as follows:
  * Image file types imported by the [Texture Importer](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingTextures.html).
  * Model file types imported by the [Model Importer](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html).


Other types of asset are always imported sequentially during an Asset Database refresh.
Some Asset Database API methods also respect this setting if you use them to import, refresh, or create texture or model assets. These are:
  * [`AssetDatabase.ImportAsset`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportAsset.html)
  * [`AssetDatabase.Refresh`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Refresh.html)
  * [`AssetDatabase.CreateAsset`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)


## Enable parallel importing
To enable parallel importing:
  1. Go to **Edit** > **Project Settings** > **Editor**.
  2. Under the **Asset Pipeline** section, enable the **Parallel Import** setting.


Parallel importing only happens when the Editor performs a standard [Asset Database refresh](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabaseRefreshing.html), which happens when it detects new or modified assets in the Project folder and automatically imports them.
## Parallel importing effects on AssetPostprocessor instances
Parallel imports operate in a separate worker instance of the Editor, so any [`AssetPostprocessor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html) instances that handle texture or model imports take effect in that instance rather than the main Editor process.
If you enable the **Parallel Import** setting, be aware that Unity executes the code on multiple threads, so any code you write for post processors must be self-contained, deterministic, and must not change the context it’s running in. For example, don’t use an `AssetPostprocessor` to change the Editor settings or create new assets on disk. Following these rules helps your processor code avoid parallel threading issues and ensures that the results are always consistent.
## Controlling the import worker processes
You can use the [Asset Pipeline Project settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html#asset-pipeline) to control the behavior of the import worker processes. These settings are project-specific. 
You can also control the default values that Unity sets the **Desired Import Worker Count** for new projects in the [Settings window](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html#asset-pipeline). To do this, go to **Settings** > **Asset Pipeline** > **Import Worker Count %**.
When you create a new project, Unity uses the **Import Worker Count %** value to assign your project’s **Desired Import Worker Count** value to the percentage of the number of logical cores available on your system. 
For example, if your system has 16 logical cores and this preference is set to 25%, the **Desired Import Worker Count** for new projects is 4. If you set this value too high, the import worker processes need to compete over other processes and system resources such as reading and writing files. The default value is 25% which suits most situations.
## Additional resources
  * [Importing assets introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingAssets.html)
  * [Asset Database introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabase.html)
  * [Asset Pipeline Project Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html#asset-pipeline)
  * [Asset Pipeline Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html#asset-pipeline)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetMetadata.html)
Asset metadata
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptedImporters.html)
Managing importers with scripts
