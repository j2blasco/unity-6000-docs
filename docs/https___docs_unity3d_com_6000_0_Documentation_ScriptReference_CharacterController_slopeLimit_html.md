* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController-slopeLimit.html

#  [CharacterController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html).slopeLimit
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterController.html "Go to CharacterController Component in the Manual")
slopeLimit; 
### Description
The character controllers slope limit in degrees.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Set the controller slope limit to 45 degrees
    CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html) controller;  
  
    void Start()
    {
        controller = GetComponent<CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html)>();
        controller.slopeLimit = 45.0f;
    }
}

```

* * *
