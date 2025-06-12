* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Thai.html

#  [SystemLanguage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.html).Thai
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
Thai.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        //This checks if your computer's operating system is in the Thai language
        if (Application.systemLanguage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-systemLanguage.html) == SystemLanguage.Thai[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Thai.html))
        {
            //Outputs into console that the system is Thai
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This system is in Thai. ");
        }
    }
}

```

* * *
