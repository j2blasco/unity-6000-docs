* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Norwegian.html

#  [SystemLanguage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.html).Norwegian
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
Norwegian.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        //This checks if your computer's operating system is in the Norwegian language
        if (Application.systemLanguage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-systemLanguage.html) == SystemLanguage.Norwegian[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Norwegian.html))
        {
            //Outputs into console that the system is Norwegian
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This system is Norwegian. ");
        }
    }
}

```

* * *
