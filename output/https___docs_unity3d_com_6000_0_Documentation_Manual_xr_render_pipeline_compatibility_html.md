* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/xr-render-pipeline-compatibility.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [XR](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)
  * [XR graphics](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-graphics.html)
  * Universal Render Pipeline compatibility in XR


[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-graphics.html)
XR graphics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SinglePassStereoRendering.html)
Stereo rendering
# Universal Render Pipeline compatibility in XR
Support for **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) features in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) varies by URP package version. This page details compatibility between XR features in Unity 6 and the latest compatible URP version.
To determine which version of URP is compatible with your current Unity version, refer to the [Requirements and compatibility](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/?subfolder=/manual/requirements.html) page in the Universal Render Pipeline documentation.
Unity 6 supports the following **AR** Augmented Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AR) and **VR** Virtual Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VR) features in the Universal Render Pipeline:
**Feature** | **Supported in XR**  
---|---  
**Post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects: Bloom | Yes  
Post-processing effects: MotionBlur | Yes  
Post-processing effects: Lens Distortion | No  
Post-processing effects: **Depth of Field** A post-processing effect that simulates the focus properties of a camera lens. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DepthofField) | Yes  
Post-processing effects: **ToneMapping** The process of remapping HDR values of an image into a range suitable to be displayed on screen. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tonemapping) | Yes  
Other post-processing effects (color adjustment, etc.) | Yes  
GI (Global Illumination) | Yes  
**HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) | Yes  
MSAA | Yes  
Physical **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) | No  
CopyColor / ColorDepth | Yes  
Multi Display | No  
Camera Stacking | Yes  
Cascaded Shadow | Yes  
sRGB | Yes  
**Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) | Yes  
Fog | Yes  
**Billboard** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) | Yes  
**Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) Graph | Yes (1)  
Particles | Yes  
**Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) | Yes  
2D UI (Canvas Renderer, Text Mesh Pro) | Yes  
URP Debug (Scene View Mode, Frame Debug) | Yes (2)  
  * (1) Although Shader Graph shaders can run in XR, Shader Graph doesn’t currently support the XR utility feature to create SPI-compatible shader input textures. Unity will expand support for Shader Graph functionality in future releases.
  * (2) Unity supports frame debugging for mock HMDs. Currently, there is no support for Meta/Oculus.


To learn more about post-processing effects, refer to the [Effect list](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/?subfolder=/manual/EffectList.html) page in the Universal Render Pipeline documentation.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-graphics.html)
XR graphics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SinglePassStereoRendering.html)
Stereo rendering
