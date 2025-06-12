* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-allPositionsWithin.html

#  [BoundsInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.html).allPositionsWithin
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
[BoundsInt.PositionEnumerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.PositionEnumerator.html) allPositionsWithin; 
### Description
A BoundsInt.PositionCollection that contains all positions within the [BoundsInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.html).
Positions within the BoundsInt are not inclusive of the positions on the upper limits of the BoundsInt. This iterator will only return positions of size greater than zero for each axis.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Create a BoundsInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.html) of a cube with a
    // bottom-left coordinate of (0, 0, 0),
    // and a height, width and depth of 4,
    // and log its contained points to the console.
    void Start()
    {
        // bounds is a cube where every edge has exactly four points.
        // It has 4 * 4 * 4 = 64 points.
        // min = (0,0,0), max = (3,3,3).
        var bounds = new BoundsInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.html)(new Vector3Int[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.html)(0, 0, 0), new Vector3Int[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.html)(4, 4, 4));  
  
        // Iterate through each point, and log it to the Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html) Console.
        foreach (var point in bounds.allPositionsWithin)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(point.ToString());
        }  
  
        // The 64 unique integer 3-dimensional points that fall within this Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) will be logged to the Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html) Console.
    }
}

```

* * *
