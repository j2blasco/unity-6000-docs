* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).InverseTransformPoints
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
public void InverseTransformPoints(Span<Vector3> positions); 
### Parameters
Parameter | Description  
---|---  
positions | The positions of the points to be transformed, each is replaced by the transformed version.  
### Description
Transforms multiple positions from world space to local space overwriting each original position with the transformed version.
This function is essentially the opposite of [Transform.TransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoints.html) which is used to convert from local to world space.  
  
Note that the returned positions are affected by scale. Use [Transform.InverseTransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html) if you are dealing with direction vectors rather than positions.  
  
Additional resources:[Transform.TransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoints.html), [Transform.InverseTransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoint.html), [Transform.InverseTransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html), [Transform.InverseTransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVectors.html).
* * *
## Declaration
public void InverseTransformPoints(ReadOnlySpan<Vector3> positions, Span<Vector3> transformedPositions); 
### Parameters
Parameter | Description  
---|---  
positions | The positions of the points to be transformed, these vectors are not modified by the function unless the `transformedPositions` span overlaps.  
transformedPositions | Receives the transformed positions of each point, must be the same length as the `positions` span otherwise an exception will be thrown. If this span overlaps the `positions` span other than representing the exact same elements the behaviour is undefined.  
### Description
Transforms multiple positions from world space to local space writing the transformed positions to a possibly different location.
This function is essentially the opposite of [Transform.TransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoints.html) which is used to convert from local to world space.  
  
Note that the returned positions are affected by scale. Use [Transform.InverseTransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html) if you are dealing with direction vectors rather than positions.  
  
Additional resources:[Transform.TransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoints.html), [Transform.InverseTransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoint.html), [Transform.InverseTransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html), [Transform.InverseTransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVectors.html).
* * *
