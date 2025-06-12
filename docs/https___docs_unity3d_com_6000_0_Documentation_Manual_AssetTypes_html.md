* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Importing assets](https://docs.unity3d.com/6000.0/Documentation/Manual/import-assets.html)
  * Supported asset type reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextAsset.html)
Text assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SpecialFolders.html)
Reserved folder name reference
# Supported asset type reference
Unity supports many different types of assets and most common image file types. It uses [asset importers](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html#asset-importers) to process and convert external files into assets you can use in your project.
Unity supports the following kinds of files:
  * **3D model files** : Unity supports standard and proprietary **model file** A file containing a 3D data, which may include definitions for meshes, bones, animation, materials and textures. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Modelfile) formats. Internally, Unity uses the FBX file format as its importing chain. For a list of supported files, refer to [3D model importers](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html#3d-model-importers).
  * **Image files** : Unity imports image files as textures and supports most common image file types. For a list of supported files, refer to [Image importers](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html#image-importers).
  * **Audio and video files** : Unity supports many audio and video file formats. For a list of supported files, refer to [Audio and video importers](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html#audio-and-video-importers).
  * ****Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) files**: Unity supports different shader file types depending on the graphics pipeline you’re using. For a list of supported files, refer to [Shader importers](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html#shader-importers).
  * **Text and arbitrary data** : Unity can import arbitrary data from files such as .html, .xml, .json files, which you can use to store and use data from external sources. For a list of supported files, refer to [Text and arbitrary data importers](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html#text-and-arbitrary-data-importers).
  * **Plug-ins and code related assets** : You can add managed and native [plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) files into your project to expand the functionality of your application, and [assembly definitions](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html) to create and organize your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) into assemblies. For a list of supported files, refer to [Plug-ins and code importers](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html#plug-ins-and-code-importers)
  * **Native assets** : There are a range of asset types that are native to the Unity Editor. For a list of supported files, refer to [Native asset importers](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html#native-asset-importers).


## Asset importers
Unity uses importers to process and convert external files into assets that can be used in your project. Each file type has a corresponding importer that handles its specific requirements. 
Unity supports many asset file types via its collection of built-in importers. Most of these importers are implemented in the Unity Editor’s native code. They provide the import functionality for most of Unity’s basic asset types, such as 3D models, textures, and audio files.
Most importers have a corresponding class in the `UnityEditor` namespace that exposes the same configurable import settings as the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window for the asset type. They also have corresponding pre-process and post-process callbacks on the [`AssetPostprocessor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html) class so you can define custom behavior to run before or after asset import. For example, the import settings for the `AudioImporter` are configurable in the [Audio Clip Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html) or from code with the [`AudioImporter` class](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html). You can also create custom pre-import or post-import behavior for audio assets with [`AssetPostprocessor.OnPreprocessorAudio`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPreprocessAudio.html) and [`AssetPostprocessor.OnPostprocessAudio`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessAudio.html) respectively. This pattern applies for most major asset types.
### 3D model importers
Unity uses the FBX file format as its importing chain. For a list of 3D modeling software that Unity supports, refer to [Model file formats](https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html).
**Importer** | **Description** | **Supported file formats**  
---|---|---  
**FBXImporter** | Imports 3D model files. For more information, refer to [Importing a model](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html). | 
  * `.blend`
  * `.c4d`
  * `.dae`
  * `.dxf`
  * `.fbx`
  * `.jas`
  * `.lxo`
  * `.ma`
  * `.mb`
  * `.max`
  * `.obj`

  
**Mesh3DSImporter** | Imports 3D Studio Max files. For more information, refer to [Importing a model](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html). | `.3ds`  
**SketchUpImporter** | Imports SketchUp files. For more information, refer to [SketchUp Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SketchUpImporter.html) and [`SketchUpImporter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.html). | `.skp`  
**SpeedTreeImporter** | Imports SpeedTree files. For more information, refer to [SpeedTree Import Settings window](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SpeedTreeImporter.html) and [`SpeedTreeImporter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter.html). | 
  * `.spm`
  * `.st`

  
**SubstanceImporter** | Imports Substance files. | `.sbsar`  
### Audio and video importers
**Importer** | **Description** | **Supported file formats**  
---|---|---  
**AudioImporter** | Imports audio files. For more information, refer to [Audio files](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioFiles.html) and [`AudioImporter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html). | 
  * `.aif`
  * `.aiff`
  * `.flac`
  * `.it`
  * `.mod`
  * `.mp3`
  * `.ogg`
  * `.s3m`
  * `.wav`
  * `.xm`

  
**VideoClipImporter** | Imports video files. For more information, refer to [Video sources](https://docs.unity3d.com/6000.0/Documentation/Manual/video-sources.html) and [`VideoClipImporter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.html). | 
  * `.asf`
  * `.avi`
  * `.dv`
  * `.m4v`
  * `.mov`
  * `.mp4`
  * `.mpg`
  * `.mpeg`
  * `.ogv`
  * `.vp8`
  * `.webm`
  * `.wmv`

  
### Image importers
Unity imports image files as textures. Unity supports most common image file types, such as `.bmp`, `.tif`, `.tga`, `.jpg`, and `.psd`. For more information, refer to [Import a texture](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingTextures.html).
**Importer** | **Description** | **Supported file formats**  
---|---|---  
**IHVImageFormatImporter** | Imports specialized image formats. For more information, refer to [`IHVImageFormatImporter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IHVImageFormatImporter.html). | 
  * `.astc`
  * `.dds`
  * `.ktx`
  * `.pvr`

  
**TextureImporter** | Imports texture files. For more information, refer to [Import a texture](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingTextures.html) and [`TextureImporter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html). | 
  * `.bmp`
  * `.exr`
  * `.gif`
  * `.hdr`
  * `.iff`
  * `.jpeg`
  * `.jpg`
  * `.pct`
  * `.pic`
  * `.pict`
  * `.png`
  * `.psd`
  * `.tga`
  * `.tif`
  * `.tiff`

  
### Native asset importers
There are a range of asset types that are native to the Unity Editor. You can create assets of these types using Editor features. When you create these, Unity saves the files which represent them as asset files in the `Assets` folder of your project. These include [animations](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-CreatingANewAnimationClip.html), [curves](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingCurves.html), [gradients](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysUsage.html), [masks](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AvatarMask.html)Can refer to a Sprite Mask, a UI Mask, or a Layer Mask [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-Mask.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mask), [materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html)An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material), and [presets](https://docs.unity3d.com/6000.0/Documentation/Manual/Presets.html).
**Importer** | **Description** | **Supported file formats**  
---|---|---  
**NativeFormatImporter** | Imports Unity’s native asset formats. | 
  * `.anim`
  * `.animset`
  * `.asset`
  * `.blendtree`
  * `.brush`
  * `.buildreport`
  * `.colors`
  * `.controller`
  * `.cubemap`
  * `.curves`
  * `.curvesNormalized`
  * `.flare`
  * `.fontsettings`
  * `.giparams`
  * `.gradients`
  * `.guiskin`
  * `.ht`
  * `.mask`
  * `.mat`
  * `.mesh`
  * `.mixer`
  * `.overrideController`
  * `.particleCurves`
  * `.particleCurvesSigned`
  * `.particleDoubleCurves`
  * `.particleDoubleCurvesSigned`
  * `.physicMaterial`
  * `.physicsMaterial2D`
  * `.playable`
  * `.preset`
  * `.renderTexture`
  * `.shadervariants`
  * `.signal`
  * `.spriteatlas`
  * `.state`
  * `.statemachine`
  * `.terrainlayer`
  * `.texture2D`
  * `.transition`
  * `.webCamTexture`

  
**PrefabImporter** | Imports **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) files. For more information, refer to [Creating prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingPrefabs.html). | `.prefab`  
**VisualEffectImporter** | Imports visual effect files. | 
  * `.vfx`
  * `.vfxblock`
  * `.vfxoperator`

  
### Plug-ins and code importers
You can add managed and native [plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html) such as `.dll` files into your project to expand the functionality of your application. Unity also supports [assembly definitions](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html) to help you create and organize your scripts into assemblies.
**Importer** | **Description** | **Supported file formats**  
---|---|---  
**AssemblyDefinitionImporter** | Imports assembly definition files. For more information, refer to [Introduction to assemblies in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-intro.html). | `.asmdef`  
**AssemblyDefinitionReferenceImporter** | Imports assembly definition reference files. For more information, refer to [Introduction to assemblies in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definitions-intro.html). | `.asmref`  
**DefaultImporter** | Imports system files. | 
  * `.rsp`
  * `.unity`

  
**PackageManifestImporter** | Imports package manifest files. For more information, refer to [Package manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html)Each package has a _manifest_ , which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Packagemanifest). | `.json`  
**PluginImporter** | Imports plug-in files. For more information, refer to [Import and configure plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-in-inspector.html) and [`PluginImporter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html). | 
  * `.a`
  * `.aar`
  * `.bc`
  * `.bundle`
  * `.c`
  * `.cc`
  * `.config`
  * `.cpp`
  * `.dylib`
  * `.h`
  * `.jar`
  * `.java`
  * `.jslib`
  * `.jspre`
  * `.kt`
  * `.m`
  * `.mm`
  * `.prx`
  * `.rpl`
  * `.so`
  * `.suprx`
  * `.swift`
  * `.winmd`
  * `.xib`

  
### Shader importers
**Importer** | **Description** | **Supported file formats**  
---|---|---  
**ComputeShaderImporter** | Imports compute shader files. For more information, refer to [Writing compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html) and [`ComputeShader`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShaderImporter.html). | `.compute`  
**RayTracingShaderImporter** | Imports **ray tracing** The process of generating an image by tracing out rays from the Camera through each pixel and recording the color contribution at the hit point. This is an alternative to rasterization. raytracing  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Raytracing) shader files. For more information, refer to [Introduction to shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-introduction.html). | `.raytrace`  
**ShaderImporter** | Imports shader files. For more information, refer to [Introduction to shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-introduction.html) and [`ShaderImporter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderImporter.html). | 
  * `.cg`
  * `.cginc`
  * `.glslinc`
  * `.hlsl`
  * `.shader`

  
### Text and arbitrary data importers
**Importer** | **Description** | **Supported file formats**  
---|---|---  
**LocalizationImporter** | Imports localization files. | `.po`  
**TextScriptImporter** | Imports text and script files. For more information, refer to [Text assets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextAsset.html). | 
  * `.boo`
  * `.bytes`
  * `.csv`
  * `.fnt`
  * `.htm`
  * `.html`
  * `.js`
  * `.json`
  * `.manifest`
  * `.md`
  * `.rsp`
  * `.txt`
  * `.xml`
  * `.yaml`

  
**TrueTypeFontImporter** | Imports font files. For more information, refer to [Font assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset-landing.html) and [`TrueTypeFontImporter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter.html). | 
  * `.dfont`
  * `.otf`
  * `.ttc`
  * `.ttf`

  
### Built-in scripted importers
[Scripted importers](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptedImporters.html) allow you to write your own custom importers for formats that Unity doesn’t natively support. Some of Unity’s own built-in importers are implemented as scripted importers because they are written in C# in core packages, rather than within the Unity Editor’s native code itself. Unity imports scripted importer assets after native importer assets.
**Importer** | **Description** | **File formats**  
---|---|---  
**SpeedTree9Importer** | Imports SpeedTree 9 files. For more information, refer to [`SpeedTree9Importer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTree.Importer.SpeedTree9Importer.html). | `.st9`  
**StyleSheetImporter** | Imports Unity style sheet files. For more information, refer to [Introduction to USS](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-about-uss.html). | `.uss`  
**UIElementsViewImporter** | Imports Unity XML files. For more information, refer to [Structure UI with UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html). | `.uxml`  
## Additional resources
  * [Scripted importers](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptedImporters.html)
  * [Introduction to importing assets](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingAssets.html)
  * [Asset metadata](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetMetadata.html)
  * [`AssetPostprocessor` API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextAsset.html)
Text assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SpecialFolders.html)
Reserved folder name reference
