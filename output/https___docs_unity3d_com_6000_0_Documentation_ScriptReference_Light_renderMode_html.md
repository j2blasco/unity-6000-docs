* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-renderMode.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).renderMode
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html "Go to Light Component in the Manual")
[LightRenderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightRenderMode.html) renderMode; 
### Description
Controls how often the light's contribution is calculated during rendering.
The render mode of a light determines how Unity calculates and applies lighting to objects in the Scene. Depending on the selected mode, lighting is evaluated either per pixel or per vertex. Unity provides three render modes: [LightRenderMode.Auto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightRenderMode.Auto.html), [LightRenderMode.ForceVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightRenderMode.ForceVertex.html), and [LightRenderMode.ForcePixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightRenderMode.ForcePixel.html). 
  * [LightRenderMode.Auto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightRenderMode.Auto.html): Unity automatically selects the best lighting evaluation mode based on performance and quality considerations.
  * [LightRenderMode.ForceVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightRenderMode.ForceVertex.html): Forces lighting to be calculated per vertex. This mode is faster and uses fewer resources but might result in less smooth lighting unless the geometry is highly tessellated.
  * [LightRenderMode.ForcePixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightRenderMode.ForcePixel.html): Forces lighting to be calculated per pixel, offering the highest visual fidelity. Pixel lighting is required for certain effects, such as bumpmapping and specular highlights. However, it requires more rendering time and is slower compared to vertex lighting.


Lighting render modes allow developers to balance visual quality and performance based on the requirements of their project. Pixel lighting provides high-quality results for advanced effects and is compatible with pipelines like HDRP, which exclusively support pixel lighting. Conversely, vertex lighting is useful in performance-critical scenarios, such as mobile or VR applications.  
  
Choose [LightRenderMode.Auto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightRenderMode.Auto.html) in most cases, as Unity automatically determines the optimal mode for the platform and current rendering pipeline. Use [LightRenderMode.ForcePixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightRenderMode.ForcePixel.html) in high-fidelity applications where effects such as bumpmapping or specular highlights are necessary. Choose [LightRenderMode.ForceVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightRenderMode.ForceVertex.html) for scenes targeting low-power devices or where performance is the priority.
* * *
