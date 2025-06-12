* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVectors.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).InverseTransformVectors
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
### Parameters
Parameter | Description  
---|---  
vectors | The vectors to be transformed, each is replaced by the transformed version.  
### Description
Transforms multiple vectors from world space to local space overwriting each original position with the transformed version. The opposite of [Transform.TransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVectors.html).
This operation is not affected by position of the transform but it is affected by scale. The transformed vectors may have different lengths than the originals.  
  
Additional resources:[Transform.TransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVectors.html), [Transform.InverseTransformVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVector.html), [Transform.InverseTransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoint.html), [Transform.InverseTransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirection.html).
* * *
## Declaration
public void InverseTransformVectors(ReadOnlySpan<Vector3> vectors, Span<Vector3> transformedVectors); 
### Parameters
Parameter | Description  
---|---  
vectors | The vectors to be transformed, these vectors are not modified by the function unless the `transformedVectors` span overlaps.  
transformedVectors | Receives the transformed vectors, must be the same length as `vectors` otherwise an exception will be thrown. If this span overlaps `vectors` other than representing the exact same elements the behaviour is undefined.  
### Description
Transforms the vector `x`, `y`, `z` from world space to local space writing the transformed positions to a possibly different location. The opposite of [Transform.TransformVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVector.html).
This operation is not affected by position of the transform but it is affected by scale.The transformed vectors may have different lengths than the originals.  
  
Additional resources:[Transform.TransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVectors.html), [Transform.InverseTransformVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVector.html), [Transform.InverseTransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoint.html), [Transform.InverseTransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirection.html).
* * *
