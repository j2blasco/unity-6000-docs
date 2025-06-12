* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.GetLocalCorners.html

#  [RectTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html).GetLocalCorners
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
public void GetLocalCorners(Vector3[] fourCornersArray); 
### Parameters
Parameter | Description  
---|---  
fourCornersArray | The array that corners are filled into.  
### Description
Get the corners of the calculated rectangle in the local space of its Transform.
Each corner provides its local space value. The returned array of 4 vertices is clockwise. It starts bottom left and rotates to top left, then top right, and finally bottom right. Note that bottom left, for example, is an (x, y, z) vector with x being left and y being bottom.  
  
**Note** : If the [RectTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html) is rotated in Z then the dimensions of the [GetLocalCorners](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.GetLocalCorners.html) will not be changed.  
  
Additional resources: [GetWorldCorners](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.GetWorldCorners.html). 
```
using UnityEngine;  
  
// GetLocalCorners():
//   Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the local corners and display
//   the corner values.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    RectTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html) rt;  
  
    void Start()
    {
        rt = GetComponent<RectTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html)>();
        DisplayLocalCorners();
    }  
  
    void DisplayLocalCorners()
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] v = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[4];  
  
        rt.rotation = Quaternion.AngleAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.AngleAxis.html)(45, Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html));
        rt.GetLocalCorners(v);  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Local Corners");
        for (var i = 0; i < 4; i++)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Local Corner " + i + " : " + v[i]);
        }
    }
}

```

Additional resources: [GetWorldCorners](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.GetWorldCorners.html). 
* * *
