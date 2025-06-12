* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-inputString.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).inputString
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
inputString; 
### Description
Returns the keyboard input entered this frame. (Read Only)
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
Only ASCII characters are contained in the `inputString`.  
  
The string can contain two special characters which should be handled: Character `"\b"` represents backspace.  
Character `"\n"` represents return or enter.  

```
using UnityEngine;
using System.Collections;
using UnityEngine.UI;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Text  gt;  
  
    void Start()
    {
        gt = GetComponent<Text>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        foreach (char c in Input.inputString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-inputString.html))
        {
            if (c == '\b') // has backspace/delete been pressed?
            {
                if (gt.text.Length != 0)
                {
                    gt.text = gt.text.Substring(0, gt.text.Length - 1);
                }
            }
            else if ((c == '\n') || (c == '\r')) // enter/return
            {
                print("User entered their name: " + gt.text);
            }
            else
            {
                gt.text += c;
            }
        }
    }
}

```

* * *
