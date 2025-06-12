* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchPackedCullingViewID.html

# BatchPackedCullingViewID
struct in UnityEngine.Rendering
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
The ID of the view from which Unity invoked the culling.
### Public Methods
Method | Description  
---|---  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchPackedCullingViewID.Equals.html) | Returns true if the ID in the argument equals this view ID.  
[GetHashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchPackedCullingViewID.GetHashCode.html) | Returns the hash code for the ID.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchPackedCullingViewID.GetInstanceID.html) | Returns the instance ID of the GameObject from which Unity performs the culling (for example, Camera, Light, etc.).  
[GetSliceIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchPackedCullingViewID.GetSliceIndex.html) | Returns the slice index of the culled view. The slice index depends on the view type. For cameras, the slice index is always zero. For cascaded shadow maps, it is equal to the index of the cascade.  
* * *
