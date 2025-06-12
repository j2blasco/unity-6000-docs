* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/xr-graphics.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [XR](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)
  * XR graphics


[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-run.html)
Run an XR application
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-render-pipeline-compatibility.html)
Universal Render Pipeline compatibility in XR
# XR graphics
Graphics and rendering in an **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) app follow the same principles as they do in any Unity application, with some differences arising from the need for stereo rendering and increased efficiency.
XR apps generally require very high and consistent frame rates for user comfort. At the same time, rendering in stereo means that every visible object must be drawn twice from different perspectives. Techniques like single-pass rendering can improve rendering efficiency by reducing the duplication of effort, but also require changes to **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) code.
Topic | Description  
---|---  
[Universal Render Pipeline compatibility in XR](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-render-pipeline-compatibility.html) | Understand which Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) features are compatible with XR platforms.  
[Stereo rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/SinglePassStereoRendering.html) | Understand stereo rendering for XR platforms.  
[Foveated rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-foveated-rendering.html) | Learn about foveated rendering for XR.  
[VR frame timing](https://docs.unity3d.com/6000.0/Documentation/Manual/VRFrameTiming.html) | Learn about **VR** Virtual Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VR) frame timing.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-run.html)
Run an XR application
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-render-pipeline-compatibility.html)
Universal Render Pipeline compatibility in XR
