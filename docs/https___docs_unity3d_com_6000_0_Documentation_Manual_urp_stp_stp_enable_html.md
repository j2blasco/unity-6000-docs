* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-enable.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Upscaling resolution in URP with Spatial-Temporal Post-Processing](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/change-resolution-scale-urp.html)
  * Enable Spatial-Temporal Post-processing in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-upscaler.html)
Introduction to Spatial-Temporal Post-processing in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-debug-views.html)
Spatial-Temporal Post-processing Rendering Debugger reference for URP
# Enable Spatial-Temporal Post-processing in URP
To enable STP in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP):
  1. Select the active URP Asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow).
  2. In the Inspector, go to **Quality** > **Upscaling Filter** , and select **Spatial-Temporal Post-Processing**.


STP remains active when **Render Scale** is set to **1.0** as it applies temporal anti-aliasing (TAA) to the final rendered output.
**Note** : STP is not compatible with ****Dynamic Resolution** A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#dynamicresolution)** in URP, only with **Render Scale**.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-upscaler.html)
Introduction to Spatial-Temporal Post-processing in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-debug-views.html)
Spatial-Temporal Post-processing Rendering Debugger reference for URP
