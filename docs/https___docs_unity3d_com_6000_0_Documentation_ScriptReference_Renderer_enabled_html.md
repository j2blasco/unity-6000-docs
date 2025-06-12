* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-enabled.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).enabled
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
enabled; 
### Description
Makes the rendered 3D object visible if enabled.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend;  
  
    void Start()
    {
        rend = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
        rend.enabled = true;
    }  
  
    // Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) the Object's visibility each second.
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Find out whether current second is odd or even
        bool oddeven = Mathf.FloorToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.FloorToInt.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html)) % 2 == 0;  
  
        // Enable renderer accordingly
        rend.enabled = oddeven;
    }
}

```

* * *
