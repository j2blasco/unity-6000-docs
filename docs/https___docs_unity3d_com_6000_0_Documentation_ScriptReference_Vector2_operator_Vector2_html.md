* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-operator_Vector2.html

#  [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html).Vector3
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
### Description
Converts a [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) to a [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).
A [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) can be implicitly converted into a [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html). (The z is set to zero in the result).
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) v2 = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 2);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) is: " + v2);  
  
        // convert v2 to v3
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) v3 = v2;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) is: " + v3);  
  
        // convert v3 to new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Set v3 to (3, 4, 5)");
        v3 = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(3, 4, 5);  
  
        // convert v3 to v2
        v2 = v3;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) is: " + v2);
    }
}

```

* * *
