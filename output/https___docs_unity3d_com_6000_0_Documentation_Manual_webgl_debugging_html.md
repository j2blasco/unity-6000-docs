* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-debugging.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * Debug and troubleshoot Web builds


[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-performance.html)
Web performance considerations
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)
Build and distribute a Web application
# Debug and troubleshoot Web builds
Visual Studio doesn’t support debugging Unity Web content. Use the following tips to get your build information.
## Debug your build in a browser’s JavaScript console
The Unity Web platform doesn’t have access to your file system, so it doesn’t write a log file like other platforms. However, it does write all logging information such as `Debug.Log`, `Console.WriteLine` or Unity’s internal logging to the browser’s JavaScript console.
To open the JavaScript console:
**OS** | **Browser** | **Instructions**  
---|---|---  
**Windows** |  Firefox | Press Ctrl-Shift-K.   
|  Chrome  | Press Ctrl-Shift-J.   
|  Microsoft Edge  | Press F12.   
|  Internet Explorer  | Press F12.   
**Mac** |  Firefox  | Press Command-Option-K.   
|  Chrome  | Press Command-Option-J.   
|  Safari  | 
  1. Go to **Preferences** > **Advanced** > **Develop**. 
  2. Press Command-Option-C.

  
## Create a development build to debug
You might want to make a **development build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild) in Unity to debug your code. To make a development build: 
  1. Open the [Build Profiles window](https://docs.unity3d.com/6000.0/Documentation/Manual/PublishingBuilds.html).
  2. Enable **Development Build**. 


Development builds allow you to connect the **profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler). Unity doesn’t [minify](https://en.wikipedia.org/wiki/Minification_%28programming%29) the code, so the emitted JavaScript code still contains human-readable, [C++-mangled](https://en.wikipedia.org/wiki/Name_mangling#Name_mangling_in_C.2B.2B), function names.
The browser uses these to display stack traces if you run into a browser error, when using `Debug.LogError`, or when an exception occurs and exception support is disabled. Unlike the managed stack traces that occur when you have full exception support, these stack traces have mangled names, and contain managed code and the internal Unity Engine code.
## Exception support
Web has different levels of exception support, but by default, Unity Web only supports explicitly thrown exceptions. For more information, refer to [Web Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsWebGL.html#wasm-language-features). You can enable **Full** exception support, which emits additional checks in the IL2CPP-generated code, to catch access to null references and out-of-bounds array elements in your managed code. These additional checks significantly impact performance and increase code size and load times, so you must only use it for debugging.
Full exception support also emits function names to generate stack traces for your managed code. For this reason, stack traces appear in the console for uncaught exceptions and for `Debug.Log` statements. Use `System.Environment.StackTrace` to get a stack trace string.
## Troubleshooting
### Problem: The build runs out of memory
This is a common problem, especially on 32-bit browsers. For more information on Web memory issues and how to fix them, refer to the documentation on [Memory in Unity Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-memory.html).
### Error message: Incorrect header check
The browser console log usually prints this error due to incorrect server configuration. For more information on how to deploy a release build, refer to documentation on [Deploying compressed builds](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-deploying.html).
### Error message: Decompressing this format (1) isn’t supported on this platform
The browser console log prints this error when the content tries to load an AssetBundle compressed using LZMA, which Unity Web doesn’t support. Re-compress the AssetBundle using LZ4 **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) to solve this problem. For more information on compression for Web, refer to documentation on [Web building](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building.html), particularly the **AssetBundles** section.
## Additional resources:
  * [Web Development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * [Web performance considerations](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-performance.html)
  * [Build and distribute a Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-performance.html)
Web performance considerations
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)
Build and distribute a Web application
