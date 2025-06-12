* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.GetShadowCasterBounds.html

#  [CullingResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html).GetShadowCasterBounds
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
public bool GetShadowCasterBounds(int lightIndex, out [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) outBounds); 
### Parameters
Parameter | Description  
---|---  
lightIndex | The index of the shadow-casting light.  
outBounds | The bounds to be computed.  
### Returns
**bool** True if the light affects at least one shadow casting object in the Scene. 
### Description
Returns the bounding box that encapsulates the visible shadow casters. Can be used to, for instance, dynamically adjust cascade ranges.
* * *
