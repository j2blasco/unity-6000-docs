* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InitializeOnEnterPlayModeAttribute.html

# InitializeOnEnterPlayModeAttribute
class in UnityEditor
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
Allow an editor class method to be initialized when Unity enters Play Mode.
Use to reset static fields in Editor classes on Enter Play Mode without Domain Reload.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class MyAnotherClass
{
    static int s_MySimpleValue = 0;  
  
    [InitializeOnEnterPlayMode]
    static void OnEnterPlaymodeInEditor(EnterPlayModeOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EnterPlayModeOptions.html) options)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Entering PlayMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayMode.html)");  
  
        if (options.HasFlag(EnterPlayModeOptions.DisableDomainReload[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EnterPlayModeOptions.DisableDomainReload.html)))
            s_MySimpleValue = 0;
    }
}

```

Or perform any other logic on Enter Play Mode.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class MyClass
{
    static int s_MyValue = 0;  
  
    static void MyClassPlaymodeSetup()
    {
        s_MyValue = 1000;
        //...
    }  
  
    [InitializeOnEnterPlayMode]
    static void OnEnterPlaymodeInEditor(EnterPlayModeOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EnterPlayModeOptions.html) options)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Entering PlayMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayMode.html)");
        MyClassPlaymodeSetup();
    }
}

```

* * *
