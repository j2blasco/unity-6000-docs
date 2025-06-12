* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.html

# CullingGroup
class in UnityEngine
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
Describes a set of bounding spheres that should have their visibility and distances maintained.
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup-enabled.html) | Pauses culling group execution.  
[onStateChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup-onStateChanged.html) | Sets the callback that will be called when a sphere's visibility and/or distance state has changed.  
[targetCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup-targetCamera.html) | Locks the CullingGroup to a specific camera.  
### Constructors
Constructor | Description  
---|---  
[CullingGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup-ctor.html) | Create a CullingGroup.  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.Dispose.html) | Clean up all memory used by the CullingGroup immediately.  
[EraseSwapBack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.EraseSwapBack.html) | Erase a given bounding sphere by moving the final sphere on top of it.  
[GetDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.GetDistance.html) | Get the current distance band index of a given sphere.  
[IsVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.IsVisible.html) | Returns true if the bounding sphere at index is currently visible from any of the contributing cameras.  
[QueryIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.QueryIndices.html) | Retrieve the indices of spheres that have particular visibility and/or distance states.  
[SetBoundingDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.SetBoundingDistances.html) | Set bounding distances for 'distance bands' the group should compute, as well as options for how spheres falling into each distance band should be treated.  
[SetBoundingSphereCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.SetBoundingSphereCount.html) | Sets the number of bounding spheres in the bounding spheres array that are actually being used.  
[SetBoundingSpheres](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.SetBoundingSpheres.html) | Sets the array of bounding sphere definitions that the CullingGroup should compute culling for.  
[SetDistanceReferencePoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.SetDistanceReferencePoint.html) | Set the reference point from which distance bands are measured.  
### Delegates
Delegate | Description  
---|---  
[StateChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.StateChanged.html) | This delegate is used for recieving a callback when a sphere's distance or visibility state has changed.  
* * *
