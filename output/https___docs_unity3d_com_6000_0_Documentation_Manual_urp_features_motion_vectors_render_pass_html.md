* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-render-pass.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Motion vectors in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-landing.html)
  * Motion vectors render pass in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-shader-support.html)
Built-in shader support for motion vectors in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-custom-shader.html)
Output a motion vector texture in a custom shader in URP
# Motion vectors render pass in URP
Understand how the **MotionVectors** render pass renders the motion vector texture.
## Location in the frame loop
URP renders motion vectors at the `BeforeRenderingPostProcessing` event. Before that event the motion vector texture might not be set or might contain previous frame’s motion vector data.
## MotionVectors pass structure
URP renders the motion vector texture in 2 steps:
  1. URP renders the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) motion vectors in the **MotionVectors** full-screen pass. This pass uses the depth texture and the camera matrices for the current and the previous frames to calculate the camera motion vectors. This pass has a fixed per-camera computation load and does not require special motion vector support from renderers or materials.
  2. URP draws a per-object motion vector **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) pass for [each renderer and material combination that supports motion vectors](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors.html#cases-when-motion-vectors).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-shader-support.html)
Built-in shader support for motion vectors in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-custom-shader.html)
Output a motion vector texture in a custom shader in URP
