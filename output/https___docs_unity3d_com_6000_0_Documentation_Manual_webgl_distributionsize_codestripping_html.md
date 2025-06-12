* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-distributionsize-codestripping.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Build and distribute a Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)
  * Distribution size and code stripping


[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-assetbundles.html)
AssetBundles in Web
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-optimization.html)
Optimize your Web build
# Distribution size and code stripping
When publishing for Web, it is important to keep your build size low so users get reasonable download times before the content starts. For generic tips on reducing asset sizes, see documentation on [Reducing the file size of the build](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html). 
## Hints and tips specific to Web
  * Specify the **Crunch** texture **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) format for all your compressed textures in the [Texture Importer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).
  * Don’t deploy **development builds** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild); they’re not compressed or [minified](https://en.wikipedia.org/wiki/Minification_%28programming%29), and so have much larger file sizes.
  * In the **Player** settings window, (click **Edit** > **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings) > **Web**) expand **Publishing Settings** , and set **Enable Exceptions** to **None** if you don’t need exceptions in your build.
  * Enable **Strip Engine Code** in the **Player** settings > **Other Settings** panel, to ensure an efficient build.
  * When using third-party managed dlls, be aware that it might come with dependencies that increase the generated code size.


If you make a release build, Unity compresses the build output files according to the **Compression Format** selected in the **Publishing Settings** panel of the Web **Player** settings. 
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/WebGLBuilding-CompressionFormat.png)
For more information on how to publish compressed builds, see [Deploying compressed builds](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-deploying.html).
## Code stripping
Unity removes all unused code from your build by default. You can change this via the **Player** settings (menu: **Edit** > **Project Settings** , then select the **Player** category): Select the **Other Settings** panel to access the **Strip Engine Code** option. It is better to build with stripping enabled.
With code stripping, Unity scans your project for any `UnityObject`-derived classes used (either by being referenced in your script code, or in the serialized data in your Scenes). It then removes from the build any Unity subsystems which have none of their classes used. This makes your build have less code, resulting in both smaller downloads and less code to parse (so code runs faster and uses less memory).
### Issues with code stripping
Code stripping might cause issues with your project if it strips code which is actually necessary. This can be the case when you load AssetBundles at run time which contain classes that are not included in the main build, and have therefore been stripped from the project. Error messages appear in your browser’s JavaScript console when this happens (possibly followed by more errors). For example:
`Could not produce class with ID XXX`
To troubleshoot these errors, look up the ID (such as `XXX` in the example above) in the [Class ID Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/ClassIDReference.html) to see which class it is trying to create an instance of. In such cases, you can force Unity to include the code for that class in the build, either by adding a reference to that class to your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) or to your **Scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), or by adding a `link.xml` file to your project. 
Below is an example which makes sure that the **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) class and the Physics module gets preserved in a project. Add this XML code to a file called `link.xml`, and put that file into your _Assets_ folder.
```
<linker>
    <assembly fullname="UnityEngine">
        <type fullname="UnityEngine.Collider" preserve="all"/>
    </assembly>
</linker>


```

If you suspect that stripping is causing problems with your build, you can also try disabling the **Strip Engine Code** option during testing. 
Unity does not provide a convenient way to see which modules and classes are included in a build, which would allow you to optimize your project to strip well. However, to get an overview of included classes and modules, you can look at the generated file `Temp/StagingArea/Data/il2cppOutput/UnityClassRegistration.cpp` after making a build.
Note that the **Strip Engine Code** option only affects Unity engine code. **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) always strips byte code from your managed dlls and scripts. This can cause problems when you need to reference managed types dynamically through reflection rather than through static references in your code. If you need to access types through reflection, you may also need to set up a `link.xml` file to preserve those types. See the documentation page on [iOS Build size optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-playerSizeOptimization.html) for more information on `link.xml` files.
## Moving build output files
To change the location of your `Build` folder, modify the buildUrl variable in the Web Template index.html file.
To change the location of the files inside the `Build` folder, change their URLs (that is, `dataUrl`, `wasmCodeUrl`, `wasmMemoryUrl`, and `wasmFrameworkUrl`) in the parameters to the config variable in the index.html file.
You can specify URLs on external servers for these if you want to host your files on a content distribution network (CDN), but you need to make sure that the hosting server has enabled Cross Origin Resource Sharing (CORS) for this to work. See the manual page on [Web networking](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-networking.html) for more information about CORS.
## Incremental builds
The C++ code generated for your project by IL2CPP is compiled incrementally; that is, only generated C++ code that has changed since the last build is compiled again. Unchanged source code re-uses the same object files generated for the previous build. The object files used for incremental C++ builds are stored in the `Library/il2cpp_cache` directory in your Unity project. 
To perform a clean, from-scratch build of the generated C++ code which doesn’t use incremental compiling, delete the `Library/il2cpp_cache` directory in your Unity project. Note that if the Unity Editor version differs from the one used for the previous Web build, Unity does a clean, from-scratch build automatically.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-assetbundles.html)
AssetBundles in Web
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-optimization.html)
Optimize your Web build
