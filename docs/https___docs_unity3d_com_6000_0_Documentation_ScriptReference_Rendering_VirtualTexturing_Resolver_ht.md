* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.Resolver.html

Virtual Texturing is experimental and not ready for production use. The feature and documentation might be changed or removed in the future.
# Resolver
class in UnityEngine.Rendering.VirtualTexturing
/
Implemented in:[UnityEngine.VirtualTexturingModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.VirtualTexturingModule.html)
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
Class responsable for virtual texturing feedback analysis.
This class is responsible for performing a GPU->CPU readback (asyncronous) and starting the feedback analysis.
### Properties
Property | Description  
---|---  
[CurrentHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.Resolver.CurrentHeight.html) | >Height of the texture that the internal buffers can hold.  
[CurrentWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.Resolver.CurrentWidth.html) | Width of the texture that the internal buffers can hold.  
### Constructors
Constructor | Description  
---|---  
[Resolver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.Resolver-ctor.html) | Create a new VirtualTextureResolver object.  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.Resolver.Dispose.html) | Disposes this object.  
[Process](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.Resolver.Process.html) | Process the passed in feedback texture.  
[UpdateSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.Resolver.UpdateSize.html) | Update the internal buffers.  
* * *
