* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.EditorCameraUtils.RenderToCubemap.html

#  [EditorCameraUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.EditorCameraUtils.html).RenderToCubemap
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
## Declaration
public static bool RenderToCubemap([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) target, int faceMask, [StaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.html) culledFlags); 
### Parameters
Parameter | Description  
---|---  
camera | The Camera to use during rendering.  
target | The cubemap to render to.  
faceMask | A bitmask which determines which of the six faces to render to.  
culledFlags | The flags of objects to cull during rendering.  
### Returns
**bool** If the render process succeeds, returns `true`. Otherwise, returns `false`. 
### Description
Renders this Camera into a static cubemap.
This function is mostly useful in the editor for "baking" static cubemaps of your Scene.  
  
This functions uses the Camera's Clear Flags, its Transform’s Position, and its Clipping Plane distances to render sections of the Scene into each cubemap face. `faceMask` is a bitfield indicating which cubemap faces to render into. Each set bit corresponds to a face. Bit numbers are integer values of [CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) enum type. By default, this process renders to all six cubemap faces (the default value of 63 means the lowest six bits are set. `false`). This function returns `false` if rendering to the cubemap fails. An example of how this could happen is that some graphics hardware does not support this functionality. Note: ReflectionProbes are a more advanced method of performing real-time reflections. Note: You can create cubemaps in the Editor by navigating to **Assets >Create>Legacy** and selecting **Cubemap** option.  
  
Additional resources: [Cubemap assets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap.html), [Reflective shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveFamily.html).
* * *
