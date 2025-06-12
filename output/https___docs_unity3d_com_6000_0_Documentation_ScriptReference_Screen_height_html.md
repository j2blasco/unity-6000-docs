* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html

#  [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html).height
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
height; 
### Description
The current height of the screen window in pixels (Read Only).
This is the actual height of the player window (in full-screen it is also the current resolution).
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        //Output the current screen window height in the console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Screen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html) Height : " + Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html));
    }
}

```

* * *
