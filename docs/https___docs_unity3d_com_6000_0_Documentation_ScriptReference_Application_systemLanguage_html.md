* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-systemLanguage.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).systemLanguage
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
[SystemLanguage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.html) systemLanguage; 
### Description
The language in which the user's operating system is running in.
You can use this to automatically pick a localization for your content based on the user's system language. Use `Application.systemLanguage` to find the value of this setting.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        //This checks if your computer's operating system is in the French language
        if (Application.systemLanguage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-systemLanguage.html) == SystemLanguage.French[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.French.html))
        {
            //Outputs into console that the system is French
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This system is in French. ");
        }
        //Otherwise, if the system is English, output the message in the console
        else if (Application.systemLanguage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-systemLanguage.html) == SystemLanguage.English[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.English.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This system is in English. ");
        }
    }
}

```

```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        //This outputs what language your system is in
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This system is in " + Application.systemLanguage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-systemLanguage.html));
    }
}

```

* * *
