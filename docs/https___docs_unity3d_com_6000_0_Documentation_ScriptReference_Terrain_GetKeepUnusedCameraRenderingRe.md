* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.GetKeepUnusedCameraRenderingResources.html

#  [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html).GetKeepUnusedCameraRenderingResources
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
public bool GetKeepUnusedCameraRenderingResources(int cameraInstanceID); 
### Parameters
Parameter | Description  
---|---  
cameraInstanceID | The InstanceID of the camera being queried. See [Object.GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html).  
### Returns
**bool** Returns `true` if all rendering resources for the given camera are saved regardless of usage. Returns `false` if garbage collection is allowed to free unused resources. 
### Description
Each Camera has its own `KeepUnusedRenderingResources` setting, which is `false` by default. Unity uses this per-Camera setting in combination with the Terrain's overall `KeepUnusedRenderingResources` setting. If either setting is `true`, Unity preserves all rendering resources regardless of how long they've remained unused.  
  
Additional resources: [Terrain.SetKeepUnusedCameraRenderingResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.SetKeepUnusedCameraRenderingResources.html), [Terrain.keepUnusedRenderingResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-keepUnusedRenderingResources.html).
* * *
