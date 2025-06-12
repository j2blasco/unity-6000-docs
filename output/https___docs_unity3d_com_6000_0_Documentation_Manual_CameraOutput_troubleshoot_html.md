* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/CameraOutput-troubleshoot.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Camera output](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraOutput.html)
  * Troubleshooting camera output


[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraOutput-shader.html)
Sample output textures in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
Cameras in URP
# Troubleshooting camera output
The **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) component **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window indicates when a camera is rendering a depth or a depth+normals texture.
The way that depth textures are requested from the Camera ([Camera.depthTextureMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-depthTextureMode.html)) might mean that after you disable an effect that needed them, the Camera might still continue rendering them. If there are multiple effects present on a Camera, where each of them needs the depth texture, there’s no good way to automatically disable depth texture rendering if you disable the individual effects.
When implementing complex **Shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) or Image Effects, keep [Rendering Differences Between Platforms](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html) in mind. In particular, using depth texture in an Image Effect often needs special handling on Direct3D + Anti-Aliasing.
In some cases, the depth texture might come directly from the native Z buffer. If you see artifacts in your depth texture, make sure that the shaders that use it **do not** write into the Z buffer (use [ZWrite Off](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ZWrite.html)).
When the DepthNormals texture is rendered in a separate pass, this is done through [Shader Replacement](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderReplacement.html). Hence it is important to have correct “**RenderType** ” tag in your shaders.
## Additional resources
  * [Camera Inspector windows reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-components-reference-landing.html)
  * [Camera Inspector window reference for the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraOutput-shader.html)
Sample output textures in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
Cameras in URP
