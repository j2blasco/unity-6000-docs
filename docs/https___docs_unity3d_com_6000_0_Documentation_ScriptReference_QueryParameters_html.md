* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters.html

# QueryParameters
struct in UnityEngine
/
Implemented in:[UnityEngine.PhysicsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PhysicsModule.html)
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
Creates a struct to set up parameters for batch queries: [RaycastCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand.html), [BoxcastCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand.html), [CapsulecastCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CapsulecastCommand.html), [SpherecastCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand.html).
Use this struct to configure hit flags and layer mask. This supports hit triggers, hit backfaces and hit multiple Mesh faces.  
  
Note: Only RaycastCommand supports hitting multiple Mesh faces.
### Static Properties
Property | Description  
---|---  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters.Default.html) | Create a default QueryParameters struct.  
### Properties
Property | Description  
---|---  
[hitBackfaces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters-hitBackfaces.html) | Whether physics queries should hit back-face triangles.  
[hitMultipleFaces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters-hitMultipleFaces.html) | Whether raycast batch query should hit multiple faces.  
[hitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters-hitTriggers.html) | Whether queries hit Triggers by default.  
[layerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters-layerMask.html) | A LayerMask that is used to selectively ignore Colliders when casting a ray.  
### Constructors
Constructor | Description  
---|---  
[QueryParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters-ctor.html) | Struct used to set up parameters for queries: RaycastCommand, BoxcastCommand, CapsulecastCommand, SpherecastCommand.  
* * *
