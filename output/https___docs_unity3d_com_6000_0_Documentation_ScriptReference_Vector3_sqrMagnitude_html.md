* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-sqrMagnitude.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).sqrMagnitude
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
sqrMagnitude; 
### Description
Returns the squared length of this vector (Read Only).
The magnitude of a vector `v` is calculated as Mathf.Sqrt(Vector3.Dot(v, v)). However, the Sqrt calculation is quite complicated and takes longer to execute than the normal arithmetic operations. Calculating the squared magnitude instead of using the [magnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-magnitude.html) property is much faster - the calculation is basically the same only without the slow Sqrt call. If you are using magnitudes simply to compare distances, then you can just as well compare squared magnitudes against the squares of distances since the comparison will give the same result.  
  
Additional resources: [magnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-magnitude.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // detects when the other transform is closer than closeDistance
    // this is faster than using Vector3.magnitude[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-magnitude.html)
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) other;
    public float closeDistance = 5.0f;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (other)
        {
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) offset = other.position - transform.position;
            float sqrLen = offset.sqrMagnitude;  
  
            // square the distance we compare with
            if (sqrLen < closeDistance * closeDistance)
            {
                print("The other transform is close to me!");
            }
        }
    }
}

```

* * *
