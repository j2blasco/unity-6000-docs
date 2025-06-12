* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).InverseTransformDirections
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
public void InverseTransformDirections(Span<Vector3> directions); 
### Parameters
Parameter | Description  
---|---  
directions | The directions to be transformed, each is replaced by the transformed version.  
### Description
Transforms multiple directions from world space to local space overwriting each original position with the transformed version. The opposite of [Transform.TransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirections.html).
This operation is not affected by scale or position of the transform. The transformed vectors have the same lengths as the originals.  
  
If you need the inverse operation to transform from local space to world space you can use [Transform.TransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirections.html)  
  
You should use [Transform.InverseTransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html) if the vectors represent positions in space rather than directions.  
  
Additional resources:[Transform.InverseTransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirection.html), [Transform.TransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirections.html), [Transform.InverseTransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html), [Transform.InverseTransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVectors.html).
* * *
## Declaration
public void InverseTransformDirections(ReadOnlySpan<Vector3> directions, Span<Vector3> transformedDirections); 
### Parameters
Parameter | Description  
---|---  
directions | The directions to be transformed, these vectors are not modified by the function unless the `transformedDirections` span overlaps.  
transformedDirections | Receives the transformed directions, must be the same length as the `directions` span otherwise an exception will be thrown. If this span overlaps `directions` other than representing the exact same elements the behaviour is undefined.  
### Description
Transforms multiple directions from world space to local space writing the transformed positions to a possibly different location. The opposite of [Transform.TransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirections.html).
This operation is not affected by scale or position of the transform. The transformed vectors have the same lengths as the originals.  
  
If you need the inverse operation to transform from local space to world space you can use [Transform.TransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirections.html)  
  
You should use [Transform.InverseTransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html) if the vectors represent positions in space rather than directions.  
  
Additional resources:[Transform.InverseTransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirection.html), [Transform.TransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirections.html), [Transform.InverseTransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html), [Transform.InverseTransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVectors.html).
* * *
