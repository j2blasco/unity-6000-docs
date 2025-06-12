* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-bendingStiffness.html

#  [Cloth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html).bendingStiffness
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cloth.html "Go to Cloth Component in the Manual")
bendingStiffness; 
### Description
Bending stiffness of the cloth.
Must be between zero and one. Setting the value to zero disables bending stiffness simulation.  
In many cases, when you want a cloth to be more stiff, actually reducing the number of vertices will get you better results - and performance.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        GetComponent<Cloth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html)>().bendingStiffness = 1;
    }
}

```

* * *
