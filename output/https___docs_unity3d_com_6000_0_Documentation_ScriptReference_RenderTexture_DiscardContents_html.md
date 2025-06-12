* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.DiscardContents.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).DiscardContents
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html "Go to RenderTexture Component in the Manual")
## Declaration
public void DiscardContents(); 
## Declaration
public void DiscardContents(bool discardColor, bool discardDepth); 
### Parameters
Parameter | Description  
---|---  
discardColor | Should the colour buffer be discarded?  
discardDepth | Should the depth buffer be discarded?  
### Description
Hint the GPU driver that the contents of the RenderTexture will not be used.
On some platforms, it can be good for performance if you indicate when the current contents of a RenderTexture aren't needed any more. This can save copying it from one kind of memory to another when the texture is reused. Many mobile GPUs can benefit from this.  
  
This call is typically only meaningful when the given RenderTexture is currently an active render target. After this call, the contents of the RenderTexture are undefined, so the user should not attempt to access its contents before either clearing the RenderTexture or drawing into each pixel of it.  
  
Both the colour buffer and depth buffer are discarded by default but either can be selected individually using the optional boolean parameters.
* * *
