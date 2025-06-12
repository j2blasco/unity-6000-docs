* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-determinant.html

#  [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html).determinant
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
determinant; 
### Description
The determinant of the matrix. (Read Only)
You can not invert matrices with a determinant of zero.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // create a transformation matrix with scale, zero position and no rotation
        var scale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(5,3,2);
        var matrix = Matrix4x4.TRS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.TRS.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html), scale);  
  
        // determinant of a scaled matrix is volume of the parallelepiped
        // formed from its axes, in this case 5*3*2=30
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(matrix.determinant);
    }
}
```

See [Determinant on Wikipedia](https://en.wikipedia.org/wiki/Determinant) for more details.  
  
Additional resources: [inverse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-inverse.html) property, [Inverse3DAffine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Inverse3DAffine.html) method.
* * *
