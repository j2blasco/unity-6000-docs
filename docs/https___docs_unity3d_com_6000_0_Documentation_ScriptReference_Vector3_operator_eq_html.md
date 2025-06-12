* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-operator_eq.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).operator ==
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
operator ==([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) lhs, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) rhs); 
### Description
Returns true if two vectors are approximately equal.
To allow for floating point inaccuracies, the two vectors are considered equal if the magnitude of their difference is less than 1e-5.  
  
Additional resources: [Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Equals.html)
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) other;  
  
    void Example()
    {
        if (other && transform.position == other.position)
        {
            print("I'm at the same place as the other transform!");
        }
    }
}

```

* * *
