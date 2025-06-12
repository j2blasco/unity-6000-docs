* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-streaming.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes.html)
  * Optimize loading Adaptive Probe Volume data


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-skyocclusion.html)
Update light from the sky at runtime with sky occlusion
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-fixissues.html)
Troubleshooting Adaptive Probe Volumes
# Optimize loading Adaptive Probe Volume data
To optimize loading Adaptive Probe Volume (APV) data at runtime, do either of the following:
  * Stream APV data.
  * Load APV data from AssetBundles or Addressables.


You can’t use both methods at the same time.
## Stream APV data
You can enable Adaptive Probe Volume streaming to enable Adaptive Probe Volume lighting in very large worlds. Using streaming means you can bake Adaptive Probe Volume data larger than available CPU or GPU memory, and load it at runtime when it’s needed. At runtime, as your **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) moves, the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) loads only Adaptive Probe Volume data from cells within the camera’s view frustum.
Unity uses Streaming Assets to store the lighting data. For more information about where Unity stores the files, refer to [Streaming Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/StreamingAssets.html).
To enable streaming, follow these steps:
  1. From the main menu, select **Edit** > **Project Settings** > **Quality**.
  2. Select a Quality Level.
  3. Double-click the **Render Pipeline Asset** to open it in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
  4. Expand **Lighting**.


You can now enable two types of streaming:
  * Enable **Enable GPU Streaming** to stream from CPU memory to GPU memory.
  * Enable **Enable Disk Streaming** to stream from disk to CPU memory. You must enable **Enable GPU Streaming** first.


You can configure streaming settings in the same window. Refer to [URP Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html) for more information.
### Debug streaming
The smallest section URP loads and uses is a cell, which is the same size as the largest [brick](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-concept.html) in an Adaptive Probe Volume. You can influence the size of cells in an Adaptive Probe Volume by [adjusting the density of Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-changedensity.html)
To view the cells in an Adaptive Probe Volume, or debug streaming, use the [Rendering Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger.html).
![The Rendering Debugger with Display Cells enabled.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/probe-volumes/probevolumes-debug-displayprobecells.PNG)  

## Load APV data from AssetBundles or Addressables
To load only the APV data you need at runtime, add the baked APV data to an [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundlesIntro.html) or [Addressable](https://docs.unity3d.com/Packages/com.unity.addressables@1.22/manual/index.html).
Follow these steps:
  1. To store APV data in normal assets instead of Streaming Assets, go to **Project Settings** > **Graphics** > **Pipeline Specific Settings** > **URP** , then under **Adaptive Probe Volumes** enable **Probe Volume Disable Streaming Assets**. This automatically disables **Enable Disk Streaming**.
  2. Bake your lighting.
  3. Add the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) to an AssetBundle. For more information about how to add assets to AssetBundles and load them at runtime, refer to [AssetBundle workflow](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Building.html).


Enabling **Probe Volume Disable Streaming Assets** may increase the amount of memory APV uses at runtime. Unity has to keep all the lighting data associated with the current Baking Set in memory, regardless of whether all scenes are loaded.
# Additional resources
  * [Understanding Adaptive Probe Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-concept.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-skyocclusion.html)
Update light from the sky at runtime with sky occlusion
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-fixissues.html)
Troubleshooting Adaptive Probe Volumes
