* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-randomAcceleration.html

#  [Cloth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html).randomAcceleration
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) randomAcceleration; 
### Description
A random, external acceleration applied to the cloth.
Use this to simulate randomly changing forces on the cloth, such as wind turbulences waving a flag. Additional resources: [Cloth.externalAcceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-externalAcceleration.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Simulate wind going trough the X axis.
    void Start()
    {
        GetComponent<Cloth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html)>().randomAcceleration = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(10, 0, 0);
    }
}

```

* * *
