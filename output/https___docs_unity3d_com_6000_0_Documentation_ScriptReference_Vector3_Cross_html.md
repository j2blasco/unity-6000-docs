* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Cross.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).Cross
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Cross([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) lhs, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) rhs); 
### Description
Cross Product of two vectors.
The cross product of two vectors results in a third vector which is perpendicular to the two input vectors. The result's magnitude is equal to the magnitudes of the two inputs multiplied together and then multiplied by the sine of the angle between the inputs. You can determine the direction of the result vector using the "left hand rule".  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/LeftHandRuleDiagram.png)  
_The left hand rule applied to Cross(a, b)._
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Get the normal to a triangle from the three corner points a, b, and o, where o is the origin point of vectors a and b.
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) GetNormal(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) a, Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) b, Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) o)
    {
        // Find vectors corresponding to two of the sides of the triangle.
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) side1 = a - o;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) side2 = b - o;  
  
        // Cross the vectors to get a perpendicular vector, then normalize it. This is the Result[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.html) vector in the drawing above.
        return Vector3.Cross[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Cross.html)(side1, side2).normalized;
    }
}

```

* * *
