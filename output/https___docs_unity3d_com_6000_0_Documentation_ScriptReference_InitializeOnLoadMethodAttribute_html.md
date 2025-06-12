* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InitializeOnLoadMethodAttribute.html

# InitializeOnLoadMethodAttribute
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
Allow an editor class method to be initialized when Unity loads without action from the user.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class MyClass
{
    [InitializeOnLoadMethod]
    static void OnProjectLoadedInEditor()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Project loaded in Unity Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)");
    }
}

```

* * *
