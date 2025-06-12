* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader.html

# ContactPairHeader
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
A header struct which contains colliding bodies.
This struct contains an array of [ContactPair](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair.html)s that can be retrieved with the [GetContactPair](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader.GetContactPair.html) method.
### Properties
Property | Description  
---|---  
[body](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader-body.html) | The first Rigidbody or ArticulationBody in the pair.  
[bodyInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader-bodyInstanceID.html) | Instance ID of the first Rigidbody or the ArticualtionBody in the pair.  
[otherBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader-otherBody.html) | The second Rigidbody or ArticulationBody in the pair.  
[otherBodyInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader-otherBodyInstanceID.html) | Instance ID of the second Rigidbody or the ArticualtionBody in the pair.  
[pairCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader-pairCount.html) | Number of ContactPairs that this header contains.  
### Public Methods
Method | Description  
---|---  
[GetContactPair](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader.GetContactPair.html) | Gets the ContactPair at index of this pair header.  
* * *
