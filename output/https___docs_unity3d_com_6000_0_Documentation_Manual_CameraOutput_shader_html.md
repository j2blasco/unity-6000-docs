* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/CameraOutput-shader.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Camera output](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraOutput.html)
  * Sample output textures in a shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-CameraDepthTexture-motionvectors.html)
Output a motion vector texture from a camera
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraOutput-troubleshoot.html)
Troubleshooting camera output
# Sample output textures in a shader
Depth textures are available for sampling in shaders as global **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) properties. By declaring a sampler called `_CameraDepthTexture` you will be able to sample the main depth texture for the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera).
`_CameraDepthTexture` always refers to the camera’s primary depth texture. By contrast, you can use `_LastCameraDepthTexture` to refer to the last depth texture rendered by any camera. This could be useful for example if you render a half-resolution depth texture in script using a secondary camera and want to make it available to a post-process shader.
In the Built-In **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), the motion vectors texture (when enabled) is available in Shaders as a global Shader property. By declaring a sampler called ‘_CameraMotionVectorsTexture’ you can sample the Texture for the currently rendering Camera. When sampling from this texture motion from the encoded **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) is returned in a range of –1..1. This will be the UV offset from the last frame to the current frame. 
## Additional resources
  * [Sample motion vectors in a shader in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-sample.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-CameraDepthTexture-motionvectors.html)
Output a motion vector texture from a camera
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraOutput-troubleshoot.html)
Troubleshooting camera output
