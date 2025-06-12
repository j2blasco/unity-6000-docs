* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVector.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).InverseTransformVector
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html "Go to Transform Component in the Manual")
## Declaration
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) InverseTransformVector([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) vector); 
### Description
Transforms a `vector` from world space to local space. The opposite of [Transform.TransformVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVector.html).
This operation is not affected by position of the transform but it is affected by scale. The returned vector may have a different length than `vector`.  
  
If you need to transform many vectors at once consider using [Transform.InverseTransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVectors.html) instead as it is much faster than repeatedly calling this function.  
  
Additional resources:[Transform.TransformVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVector.html), [Transform.InverseTransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVectors.html), [Transform.InverseTransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoint.html), [Transform.InverseTransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirection.html).
* * *
## Declaration
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) InverseTransformVector(float x, float y, float z); 
### Description
Transforms the vector `x`, `y`, `z` from world space to local space. The opposite of [Transform.TransformVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVector.html).
This operation is not affected by position of the transform but it is affected by scale. The returned vector may have a different length than `vector`.  
  
If you need to transform many vectors at once consider using [Transform.InverseTransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVectors.html) instead as it is much faster than repeatedly calling this function.  
  
Additional resources:[Transform.TransformVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVector.html), [Transform.InverseTransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVectors.html), [Transform.InverseTransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoint.html), [Transform.InverseTransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirection.html).
* * *
