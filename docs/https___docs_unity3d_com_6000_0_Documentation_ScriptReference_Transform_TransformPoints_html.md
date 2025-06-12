* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoints.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).TransformPoints
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
public void TransformPoints(Span<Vector3> positions); 
### Parameters
Parameter | Description  
---|---  
positions | The positions of the points to be transformed, each is replaced by the transformed version.  
### Description
Transforms multiple points from local space to world space overwriting each original point with the transformed version.
Note that the positions of the returned points are affected by scale. Use [Transform.TransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirections.html) if you are dealing with direction vectors.  
  
You can perform the opposite conversion, from world to local space using [Transform.InverseTransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) someObject;  
  
    const int kNumPoints = 100;  
  
    void Start()
    {
        // Instantiate 100 objects to the right of the current object
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] points = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[kNumPoints];
        for (int pointNum = 0; pointNum < kNumPoints; pointNum++)
        {
            points[pointNum] = Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html) * pointNum;
        }
        transform.TransformPoints(points);
        for (int pointNum = 0; pointNum < kNumPoints; pointNum++)
        {
            Instantiate(someObject, points[pointNum], someObject.transform.rotation);
        }
    }
}

```

Additional resources:[Transform.TransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoint.html), [Transform.InverseTransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html), [Transform.TransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirections.html), [Transform.TransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVectors.html).
* * *
## Declaration
public void TransformPoints(ReadOnlySpan<Vector3> positions, Span<Vector3> transformedPositions); 
### Parameters
Parameter | Description  
---|---  
positions | The positions of the points to be transformed, these vectors are not modified by the function unless the `transformedPositions` span overlaps.  
transformedPositions | Receives the transformed positions of each point, must be the same length as `positions` otherwise an exception will be thrown. If this span overlaps `positions` other than representing the exact same elements the behaviour is undefined.  
### Description
Transforms multiple points from local space to world space writing the transformed points to a possibly different location.
Note that the positions of the returned points are affected by scale. Use [Transform.TransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirections.html) if you are dealing with directions.  
  
You can perform the opposite conversion, from world to local space using [Transform.InverseTransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) someObject;  
  
    const int kNumPoints = 100;  
  
    void Start()
    {
        // Instantiate 100 objects to the right of the current object
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] points = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[kNumPoints];
        for (int pointNum = 0; pointNum < kNumPoints; pointNum++)
        {
            points[pointNum] = Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html) * pointNum;
        }
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] transformedPoints = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[kNumPoints];
        transform.TransformPoints(points, transformedPoints);
        for (int pointNum = 0; pointNum < kNumPoints; pointNum++)
        {
            Instantiate(someObject, transformedPoints[pointNum], someObject.transform.rotation);
        }
    }
}

```

Additional resources:[Transform.TransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoint.html), [Transform.InverseTransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html), [Transform.TransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirections.html), [Transform.TransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVectors.html).
* * *
