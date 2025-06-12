* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html

# ContactFilter2D
struct in UnityEngine
/
Implemented in:[UnityEngine.Physics2DModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.Physics2DModule.html)
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
A set of parameters for filtering contact results. Define the angle by referring to their position in world space, where 0 degrees is parallel to the positive x-axis, 90 degrees is parallel to the positive y-axis, 180 degrees is parallel to the negative x-axis, and 270 degrees is parallel to the negative y-axis.
Use a contact filter to precisely control which contact results get returned. This removes the need to filter the results later, is faster, and more convenient.  
  
If you are using a function that requires a [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html), but you don't want to perform any filtering, then use [ContactFilter2D.NoFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.NoFilter.html).  
  
For more information on using [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) with casting, see: [Physics2D.CircleCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.CircleCast.html), [Physics2D.BoxCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.BoxCast.html), [Physics2D.CapsuleCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.CapsuleCast.html), [Physics2D.Linecast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Linecast.html), [Physics2D.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Raycast.html), [Collider2D.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.Raycast.html), [Collider2D.Cast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.Cast.html) and [Rigidbody2D.Cast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Cast.html).  
  
For more information on using [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) with overlapping areas, see: [Physics2D.OverlapPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapPoint.html), [Physics2D.OverlapCircle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapCircle.html), [Physics2D.OverlapBox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapBox.html), [Physics2D.OverlapArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapArea.html), [Physics2D.OverlapCapsule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapCapsule.html), [Physics2D.OverlapCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapCollider.html), Rigidbody2D.OverlapCollider and Collider2D.OverlapCollider.  
  
For more information on using [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) with contacts, see: [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html), [Collider2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetContacts.html), [Rigidbody2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetContacts.html), [Physics2D.IsTouching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.IsTouching.html), [Rigidbody2D.IsTouching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.IsTouching.html) and [Collider2D.IsTouching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.IsTouching.html).
### Properties
Property | Description  
---|---  
[isFiltering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-isFiltering.html) | Given the current state of the contact filter, determine whether it would filter anything.  
[layerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-layerMask.html) | Sets the contact filter to filter the results that only include Collider2D on the layers defined by the layer mask.  
[maxDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-maxDepth.html) | Sets the contact filter to filter the results to only include Collider2D with a Z coordinate (depth) less than this value.  
[maxNormalAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-maxNormalAngle.html) | Sets the contact filter to filter the results to only include contacts with collision normal angles that are less than this angle.  
[minDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-minDepth.html) | Sets the contact filter to filter the results to only include Collider2D with a Z coordinate (depth) greater than this value.  
[minNormalAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-minNormalAngle.html) | Sets the contact filter to filter the results to only include contacts with collision normal angles that are greater than this angle.  
[useDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-useDepth.html) | Sets the contact filter to filter the results by depth using minDepth and maxDepth.  
[useLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-useLayerMask.html) | Sets the contact filter to filter results by layer mask.  
[useNormalAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-useNormalAngle.html) | Sets the contact filter to filter the results by the collision's normal angle using minNormalAngle and maxNormalAngle.  
[useOutsideDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-useOutsideDepth.html) | Sets the contact filter to filter within the minDepth and maxDepth range, or outside that range.  
[useOutsideNormalAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-useOutsideNormalAngle.html) | Sets the contact filter to filter within the minNormalAngle and maxNormalAngle range, or outside that range.  
[useTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-useTriggers.html) | Sets to filter contact results based on trigger collider involvement.  
### Public Methods
Method | Description  
---|---  
[ClearDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.ClearDepth.html) | Turns off depth filtering by setting useDepth to false. The associated values of minDepth and maxDepth are not changed.  
[ClearLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.ClearLayerMask.html) | Turns off layer mask filtering by setting useLayerMask to false. The associated value of layerMask is not changed.  
[ClearNormalAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.ClearNormalAngle.html) | Turns off normal angle filtering by setting useNormalAngle to false. The associated values of minNormalAngle and maxNormalAngle are not changed.  
[IsFilteringDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.IsFilteringDepth.html) | Checks if the Transform for obj is within the depth range to be filtered.  
[IsFilteringLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.IsFilteringLayerMask.html) | Checks if the GameObject.layer for obj is included in the layerMask to be filtered.  
[IsFilteringNormalAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.IsFilteringNormalAngle.html) | Checks if the angle of normal is within the normal angle range to be filtered.  
[IsFilteringTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.IsFilteringTrigger.html) | Checks if the collider is a trigger and should be filtered by the useTriggers to be filtered.  
[NoFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.NoFilter.html) | Sets the contact filter to not filter any ContactPoint2D.  
[SetDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.SetDepth.html) | Sets the minDepth and maxDepth filter properties and turns on depth filtering by setting useDepth to true.  
[SetLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.SetLayerMask.html) | Sets the layerMask filter property using the layerMask parameter provided and also enables layer mask filtering by setting useLayerMask to true.  
[SetNormalAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.SetNormalAngle.html) | Sets the minNormalAngle and maxNormalAngle filter properties and turns on normal angle filtering by setting useNormalAngle to true.  
* * *
