* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/URP-Config-Package.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Graphics quality settings in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-quality-settings-landing.html)
  * Configure settings with the URP Config package


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/quality/change-urp-asset-settings.html)
Change URP Asset settings at runtime
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html)
Add anti-aliasing in the Universal Render Pipeline
# Configure settings with the URP Config package
You can use the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) Config package to control some of the settings of URP. Unity automatically adds the package files in the package cache as they are a dependency of URP, but you must make a copy of them in your project before you can use the package.
The URP Config Package currently only changes one setting which is the maximum number of visible lights URP renders when you use the Forward+ **Rendering Path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath). For more information, refer to [Change the maximum number of visible lights](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/forward-plus-rendering-path-limitations.html).
## Embed the URP Config package source code in your project
To prepare the URP Config package source code for modifications:
  1. In the root folder of your project, go to `Library/PackageCache`.
  2. Copy the following folder into the `Packages` folder at the root of your project:
```
com.unity.render-pipelines.universal-config

```



The URP Config package is now ready for modification in your project.
**Note:** After you copy the package source code into the `Packages` folder, this package code becomes embedded in your project and is no longer part of a Unity install. If you upgrade the Unity version later, Unity doesn’t update the **embedded package** An _embedded_ package is a mutable package that you store under the `Packages` directory at the root of a Unity project. This differs from most packages which you download from a package server and are immutable. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-concepts.html#Embedded)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Embeddedpackage) source automatically. You need to apply the changes to the source code manually. For more information about embedded packages, refer to [Embedded dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-embed.html).
## Configure URP with the URP Config package
You can edit the `ShaderConfig.cs` file to configure the properties of your URP project. If you edit this file, you must also update the equivalent `ShaderConfig.cs.hlsl` header file so that it mirrors the definitions you set in `ShaderConfig.cs`.
You can update the `ShaderConfig.cs.hlsl` file in two ways:
  * Manually edit the `ShaderConfig.cs.hlsl` file to mirror the `ShaderConfig.cs` file. This method is faster but more likely to result in an error due to a mistake.
  * Use the Editor to generate the `ShaderConfig.cs.hlsl` file from the `ShaderConfig.cs` file, which might take longer than a manual edit but ensures that the two files are synchronized.


To use the Editor to generate the `ShaderConfig.cs.hlsl` file, follow these steps:
  1. In the **Project** window, go to **Packages** > **Universal RP Config** > **Runtime** and open **ShaderConfig.cs**.
  2. Edit the values of the properties you want to change and then save and close the file.
  3. In the Editor, select **Edit** > **Rendering** > **Generate Shader Includes**.
  4. Unity automatically configures your project and **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) to use the new configuration.


### Update the URP Config package
When you use the Package Manager to update your URP package, the Package Manager downloads the latest version of the URP Config package to the `/Library/PackageCache/` folder, but doesn’t automatically update the files of the URP Config package in your `Packages` folder. Instead, you need to manually update your copy of the URP Config package in your `Packages` folder and reapply your changes. To do this, use the following steps:
  1. Make a copy of the `com.unity.render-pipelines.universal-config` from your `Packages` folder. You can reference this later when you reapply your changes.
  2. Delete the `com.unity.render-pipelines.universal-config` folder in your `Packages` folder.
  3. Copy the `com.unity.render-pipelines.universal-config` folder again from the `/Library/PackageCache/` folder to your `Packages` folder, as shown above in the [Set up the URP Config package](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/URP-Config-Package.html#set-up-the-urp-config-package) section.
  4. Manually reapply your modifications to the updated copy of the URP Config package.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/quality/change-urp-asset-settings.html)
Change URP Asset settings at runtime
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html)
Add anti-aliasing in the Universal Render Pipeline
