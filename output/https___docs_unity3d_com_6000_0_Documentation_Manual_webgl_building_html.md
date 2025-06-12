* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Build and distribute a Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)
  * Web Build folder


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-build-settings.html)
Web build settings
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-assetbundles.html)
AssetBundles in Web
# Web Build folder
When you build your Web application, Unity creates a `Build` folder with all files necessary to run your application in a web browser.
## Build folder structure
The `Build` folder has the name you specify in the ****Build Profiles** A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile)** window. The folder contains the following files, where `[ExampleBuild]` represents the name of the target build folder.
File name | Description  
---|---  
`[ExampleBuild].loader.js` | The JavaScript code that the web page needs to load the Unity content.  
`[ExampleBuild].framework.js` | JavaScript runtime and **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in).  
`[ExampleBuild].wasm` | WebAssembly binary.  
`[ExampleBuild].mem` | A binary image to initialize the heap memory for your Player. Unity generates this file for multithreaded WebAssembly builds only.  
`[ExampleBuild].data` | Asset data and **Scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).  
`[ExampleBuild].symbols.json` | Debug symbol names necessary to demangle an error stack trace. This file is only generated for Release builds when you enable the Debug Symbols option (**File** > **Build Profiles** > **Player Settings**.)  
`[ExampleBuild].jpg` | A background image, which displays while the build is loading. This file is only generated when a Background Image is available in the Player Settings (**File** > **Build Profiles** > **Player Settings** > **Splash Image**). For more information, refer to [Splash Screen](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsSplashScreen.html).  
### File extensions
If you enable a ****Compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) Method** for your build, Unity identifies the extension that corresponds with the compression method and adds this extension to the names of the files inside the Build sub folder. If you enable **Decompression Fallback** , Unity appends the extension `.unityweb` to the build file names. Otherwise, Unity appends the extension `.gz` for the Gzip compression method, or `.br` for the Brotli compression method.
For more information, refer to [Compressed builds and server configuration](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-deploying.html).
### Name files as hashes
If you enable **Name Files As Hashes** in the ****Player Settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings)**, Unity uses the hash of the file content instead of the default file name. This applies to each file in the build folder. This option allows you to upload updated versions of the game builds into the same folder on the server, and only upload the files which have changed between build iterations.
**Note** : Opening a Player directly from the file system might not work in some browsers. This is due to security restrictions applied to local file URLs.
## Additional resources
  * [Web Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsWebGL.html)
  * [Web build settings](https://docs.unity3d.com/6000.0/Documentation/Manual/web-build-settings.html)
  * [Build and distribute a Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)
  * [Deploy a Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-deploying.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-build-settings.html)
Web build settings
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-assetbundles.html)
AssetBundles in Web
