* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClothSphereColliderPair.html

# ClothSphereColliderPair
struct in UnityEngine
/
Implemented in:[UnityEngine.ClothModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.ClothModule.html)
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
A pair of SphereColliders used to define shapes for Cloth objects to collide against.
A ClothSphereColliderPair can contain either a single valid SphereCollider instance (with the second one being null), or a pair of two SphereColliders. In the former cases the ClothSphereColliderPair just represents a single SphereCollider for the cloth to collide against. In the latter case, it represents a conic capsule shape defined by the two spheres, and the cone connecting the two. Conic capsule shapes are useful for modelling limbs of a character.  
  
Select the cloth object to see a visualization of Cloth colliders shapes in the Scene view.
### Properties
Property | Description  
---|---  
[first](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClothSphereColliderPair-first.html) | The first SphereCollider of a ClothSphereColliderPair.  
[second](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClothSphereColliderPair-second.html) | The second SphereCollider of a ClothSphereColliderPair.  
### Constructors
Constructor | Description  
---|---  
[ClothSphereColliderPair](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClothSphereColliderPair-ctor.html) | Creates a ClothSphereColliderPair. If only one SphereCollider is given, the ClothSphereColliderPair will define a simple sphere. If two SphereColliders are given, the ClothSphereColliderPair defines a conic capsule shape, composed of the two spheres and the cone connecting the two.  
* * *
