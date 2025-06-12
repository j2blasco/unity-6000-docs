* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-frameCount.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).frameCount
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
frameCount; 
### Description
The total number of frames since the start of the game (Read Only).
This value starts at 0 and increases by 1 on each [Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) phase.  
  
Internally, Unity uses a 64 bit integer which it downcasts to 32 bits when this is called, and discards the most significant (i.e. top) 32 bits.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Makes sure that RecalculateValue only performs
    // some operations once per frame and no more.
    static private int lastRecalculation = -1;  
  
    static void RecalculateValue()
    {
        if (lastRecalculation == Time.frameCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-frameCount.html))
            return;
        //  ProcessData.AndDoSomeCalculations();
    }
}

```

**Note:** frameCount starts once all Awake functions have finished. The frameCount value is undefined during Awake functions.
* * *
