* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-enabled.html

#  [Cloth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html).enabled
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
enabled; 
### Description
Is this cloth enabled?
This is the same as the checkbox next to the component label in the inspector. A disabled cloth component will not update it's physics simulation, so you can use this to suspend the simulation of cloth objects when they are not needed, as cloth simulation is a very CPU-intensive task.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Example()
    {
        GetComponent<Cloth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html)>().enabled = false;
    }
}

```

* * *
