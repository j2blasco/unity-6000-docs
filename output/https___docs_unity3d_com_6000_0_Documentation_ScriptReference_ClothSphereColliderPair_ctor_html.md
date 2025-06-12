* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClothSphereColliderPair-ctor.html

# ClothSphereColliderPair Constructor
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
public ClothSphereColliderPair([SphereCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html) a); 
## Declaration
public ClothSphereColliderPair([SphereCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html) a, [SphereCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html) b); 
### Parameters
Parameter | Description  
---|---  
a | The first SphereCollider of a ClothSphereColliderPair.  
b | The second SphereCollider of a ClothSphereColliderPair.  
### Description
Creates a ClothSphereColliderPair. If only one SphereCollider is given, the ClothSphereColliderPair will define a simple sphere. If two SphereColliders are given, the ClothSphereColliderPair defines a conic capsule shape, composed of the two spheres and the cone connecting the two.
* * *
