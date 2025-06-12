* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirections.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).TransformDirections
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
public void TransformDirections(Span<Vector3> directions); 
### Parameters
Parameter | Description  
---|---  
directions | The directions to be transformed, each is replaced by the transformed version.  
### Description
Transforms multiple directions from local space to world space overwriting each original direction with the transformed version.
This operation is not affected by scale or position of the transform. The transformed vectors have the same length as the original versions.  
  
If you need the inverse operation to transform from world space to local space you can use [Transform.InverseTransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html)  
  
You should use [Transform.TransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoints.html) for the conversion if the vectors represent positions rather than directions.  
  
Additional resources: [Transform.TransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirection.html), [Transform.InverseTransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html), [Transform.TransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoints.html), [Transform.TransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVectors.html).
* * *
## Declaration
public void TransformDirections(ReadOnlySpan<Vector3> directions, Span<Vector3> transformedDirections); 
### Parameters
Parameter | Description  
---|---  
directions | The directions to be transformed, these vectors are not modified by the function unless the `transformedDirections` span overlaps.  
transformedDirections | Receives the transformed directions, must be the same length as `directions` otherwise an exception will be thrown. If this span overlaps `directions` other than representing the exact same elements the behaviour is undefined.  
### Description
Transforms multiple directions from local space to world space writing the transformed directions to a possibly different location.
This operation is not affected by scale or position of the transform. The transformed vectors have the same length as the original versions.  
  
If you need the inverse operation to transform from world space to local space you can use [Transform.InverseTransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html)  
  
You should use [Transform.TransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoints.html) for the conversion if the vectors represent positions rather than directions.  
  
Additional resources: [Transform.TransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirection.html), [Transform.InverseTransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html), [Transform.TransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoints.html), [Transform.TransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVectors.html).
* * *
