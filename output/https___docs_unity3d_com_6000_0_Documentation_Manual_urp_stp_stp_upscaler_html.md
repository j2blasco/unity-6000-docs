* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-upscaler.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Upscaling resolution in URP with Spatial-Temporal Post-Processing](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/change-resolution-scale-urp.html)
  * Introduction to Spatial-Temporal Post-processing in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/change-resolution-scale-urp.html)
Upscaling resolution in URP with Spatial-Temporal Post-Processing
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-enable.html)
Enable Spatial-Temporal Post-processing in URP
# Introduction to Spatial-Temporal Post-processing in URP
Spatial-Temporal **Post-Processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) (STP) uses spatial and temporal upsampling techniques to produce a high quality, anti-aliased image.
STP is a software-based upscaler.
## Requirements
STP uses compute **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), so target platforms must support [Shader Model 5.0](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/d3d11-graphics-reference-sm5).
STP doesn’t support OpenGL ES, even if the platform supports compute shaders.
STP requires [temporal anti-aliasing (TAA)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html) pre-processing, it will implicitly enable it if not selected already.
## STP performance
STP configures itself automatically to provide the best balance of performance and quality based on the platform your application runs on. You don’t need to configure it for each different platform.
On high-performance platforms, like PCs and consoles, STP uses higher quality image filtering logic and additional deringing logic to improve image quality when it upscales images. These techniques require additional processing power and Unity uses them on high-performance devices where the performance impact is not significant.
On mobile devices, STP uses more performant image filtering logic to provide a balance between performance and image quality. This minimizes the performance impact of STP on less powerful devices, while still delivering a high quality image.
## Additional resources
  * [Enable Spatial Temporal Post-processing](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-enable.html)
  * [Spatial Temporal Post-processing debug views](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-debug-views.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/change-resolution-scale-urp.html)
Upscaling resolution in URP with Spatial-Temporal Post-Processing
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-enable.html)
Enable Spatial-Temporal Post-processing in URP
