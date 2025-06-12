* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-stripUnusedMeshComponents.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).stripUnusedMeshComponents
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
stripUnusedMeshComponents; 
### Description
Should unused [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) components be excluded from game build?
When this setting is on, Mesh components (e.g. tangent vectors, vertex colors etc.) that are not in use will be removed. This is good for game data size and runtime performance.  
  
However, be aware of this flag if you're switching shaders on some objects at runtime. For example, if a mesh uses a simple Diffuse shader when building the game, Unity will remove tangent vectors since they are not needed. If you'd want to switch to a bumpmapped shader on this mesh at runtime, you will not get proper tangent data since it was removed!
* * *
