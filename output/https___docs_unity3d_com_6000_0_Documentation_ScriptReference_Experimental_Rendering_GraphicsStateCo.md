* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState.html

**Experimental** : this API is experimental and might be changed or removed in the future.
# GraphicsState
struct in UnityEngine.Experimental.Rendering
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
A graphics state identifies a specific rendering configuration.
Modern graphics APIs (i.e. Metal, D3D12, Vulkan) use both the active shader variant and rendering configuration to create the accurate GPU representation of a shader.
### Properties
Property | Description  
---|---  
[attachments](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-attachments.html) | Array of color attachments used in this rendering configuration.  
[depthAttachmentIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-depthAttachmentIndex.html) | The index of the attachment to be used as the depth/stencil buffer for this rendering configuration.  
[depthBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-depthBias.html) | The global depth bias value for this rendering configuration.  
[forceCullMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-forceCullMode.html) | The forced cull mode in this rendering configuration.  
[invertCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-invertCulling.html) | Flag indicating if backface culling is inverted in this rendering configuration.  
[invertProjection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-invertProjection.html) | Flag indicating if the projection matrix is inverted in this rendering configuration.  
[multiviewCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-multiviewCount.html) | The number of VR views used in this rendering configuration.  
[negativeScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-negativeScale.html) | Flag indicating if the mesh has inverted scale in this rendering configuration.  
[renderState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-renderState.html) | The render state used in this rendering configuration.  
[sampleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-sampleCount.html) | The number of samples per pixel in this rendering configuration.  
[shadingRateIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-shadingRateIndex.html) | Index of attachment used as shading rate image.  
[slopeDepthBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-slopeDepthBias.html) | The global slope depth bias value for this rendering configuration.  
[subPasses](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-subPasses.html) | Array containing information of each subpass.  
[subPassIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-subPassIndex.html) | Index of the active subpass in this rendering configuration.  
[topology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-topology.html) | The topology of the Mesh, e.g: Triangles, Lines, Quads, Points, etc. used in this rendering configuration.  
[vertexAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-vertexAttributes.html) | Array containing information of vertex attributes.  
[wireframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.GraphicsState-wireframe.html) | Is wireframe mode enabled for this rendering configuration.  
* * *
