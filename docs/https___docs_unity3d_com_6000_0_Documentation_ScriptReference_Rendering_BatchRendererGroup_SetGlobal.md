* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.SetGlobalBounds.html

#  [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html).SetGlobalBounds
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
public void SetGlobalBounds([Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds); 
### Parameters
Parameter | Description  
---|---  
bounds | The center and the size of the global batch bounding box.  
### Description
Set the bounds of the `BatchRendererGroup`. The bounds should encapsulate the render bounds of every object rendered with this `BatchRendererGroup`. Unity uses these bounds internally for culling.
* * *
