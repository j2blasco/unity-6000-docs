* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.SetColumn.html

#  [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html).SetColumn
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
public void SetColumn(int index, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) column); 
### Description
Sets a column of the matrix.
You use this to build transformation matrices using right, up and forward vectors:
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // build a matrix from a transform.
    Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix = new Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html)();  
  
    /// Build a matrix from a transform.
    void Start()
    {
        matrix.SetColumn(0, transform.right);
        matrix.SetColumn(1, transform.up);
        matrix.SetColumn(2, transform.forward);
        var p = transform.position;
        matrix.SetColumn(3, new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(p.x, p.y, p.z, 1));
    }
}

```

The i-th column is set from `v`. `i` must be from 0 to 3 inclusive.  
  
Additional resources: [GetColumn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.GetColumn.html).
* * *
