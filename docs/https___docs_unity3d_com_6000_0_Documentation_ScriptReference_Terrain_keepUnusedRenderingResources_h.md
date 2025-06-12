* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-keepUnusedRenderingResources.html

#  [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html).keepUnusedRenderingResources
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
keepUnusedRenderingResources; 
### Description
Defines whether Unity frees per-Camera rendering resources for the Terrain when those resources aren't in use after a certain number of frames.
By default, this property is `false`, which implies that Unity deletes these rendering resources from memory if the Camera they're associated with hasn't rendered for 100 frames. You might sometimes not want this behavior because the next time these resources are required (for example, when that Camera starts to render again), you must reallocate them, which can negatively impact performance. In such cases, set this property to `true` to keep those resources in memory unless the Camera they're associated with is destroyed. You can also use [Terrain.SetKeepUnusedCameraRenderingResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.SetKeepUnusedCameraRenderingResources.html) and [Terrain.GetKeepUnusedCameraRenderingResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.GetKeepUnusedCameraRenderingResources.html) to configure the setting for a specific Camera.  
  
The value is not serialized with Terrain component.
* * *
