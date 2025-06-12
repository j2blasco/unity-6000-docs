* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureState.html

# GraphicsTextureState
enumeration
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
The state of a [GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html).
Describes the state of a GraphicsTexture as it is constructed, initialized, or destroyed on the render thread.
### Properties
Property | Description  
---|---  
[Constructed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureState.Constructed.html) | The GraphicsTexture constructor has started execution.  
[Initializing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureState.Initializing.html) | The descriptor is initialized and the work to create the GraphicsTexture has been queued on the render thread.  
[InitializedOnRenderThread](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureState.InitializedOnRenderThread.html) | The GraphicsTexture has completed creation on the render thread.  
[DestroyQueued](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureState.DestroyQueued.html) | The GraphicsTexture is queued for destruction on the render thread, but has not completed yet.  
[Destroyed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureState.Destroyed.html) | The GraphicsTexture has been completely destroyed on the render thread.  
* * *
