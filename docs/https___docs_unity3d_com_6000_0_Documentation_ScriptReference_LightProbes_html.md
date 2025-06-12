* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html

# LightProbes
class in UnityEngine
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
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
Stores light probe data for all currently loaded Scenes.
The data includes: probe positions, Spherical Harmonics (SH) coefficients and the tetrahedral tessellation.  
  
You can modify the probe positions and coefficients, and update the tetrahedral tessellation at runtime. You can also swap the entire `LightProbes` object for a different pre-baked one using [LightmapSettings.lightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapSettings-lightProbes.html).  
  
To retrieve the `LightProbes` objects for a specific scene, use [LightProbes.GetInstantiatedLightProbesForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetInstantiatedLightProbesForScene.html) or [LightProbes.GetSharedLightProbesForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetSharedLightProbesForScene.html).  
  
Additional resources: [Light Probes in the Unity Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html), [LightmapSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapSettings.html), [ReceiveGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReceiveGI.html).
### Properties
Property | Description  
---|---  
[bakedProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes-bakedProbes.html) | Coefficients of baked light probes.  
[cellCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes-cellCount.html) | The number of cells space is divided into (Read Only).  
[cellCountSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes-cellCountSelf.html) | The number of cells space is divided into for this LightProbes object (Read Only).  
[count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes-count.html) | The number of light probes (Read Only).  
[countSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes-countSelf.html) | The number of light probes stored in this LightProbes object (Read Only).  
[positions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes-positions.html) | Positions of the baked light probes (Read Only).  
### Public Methods
Method | Description  
---|---  
[GetPositionsSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetPositionsSelf.html) | Gets the positions of the baked light probes stored in this LightProbes object.  
[SetPositionsSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.SetPositionsSelf.html) | Sets the positions of the baked light probes stored in this LightProbes object.  
### Static Methods
Method | Description  
---|---  
[CalculateInterpolatedLightAndOcclusionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html) | Calculate light probes and occlusion probes at the given world space positions.  
[GetInstantiatedLightProbesForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetInstantiatedLightProbesForScene.html) | Gets an instantiated clone of the LightProbes object for a specific scene.  
[GetInterpolatedProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetInterpolatedProbe.html) | Returns an interpolated probe for the given position for both real-time and baked light probes combined.  
[GetSharedLightProbesForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetSharedLightProbesForScene.html) | Gets the shared LightProbes object for a specific scene.  
[Tetrahedralize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.Tetrahedralize.html) | Synchronously tetrahedralize the currently loaded LightProbe positions.  
[TetrahedralizeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.TetrahedralizeAsync.html) | Asynchronously tetrahedralize all currently loaded LightProbe positions.  
### Events
Event | Description  
---|---  
[lightProbesUpdated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes-lightProbesUpdated.html) | Unity raises this event to indicate that the light probe structure (tetrahedralization) or values (spherical harmonics coefficients) have changed.  
[needsRetetrahedralization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes-needsRetetrahedralization.html) | An event which is called when the number of currently loaded light probes changes due to additive scene loading or unloading.  
[tetrahedralizationCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes-tetrahedralizationCompleted.html) | Event which is called after LightProbes.Tetrahedralize or LightProbes.TetrahedralizeAsync has finished computing a tetrahedralization.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
