* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ChangeCheckScope.html

# ChangeCheckScope
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
Check if any control was changed inside a block of code.
When needing to check if [GUI.changed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html) is set to true inside a block of code, wrap the code inside a ChangeCheckScope like this:
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class ExampleClass
{
    void ExampleMethod()
    {
        using (var check = new EditorGUI.ChangeCheckScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ChangeCheckScope.html)())
        {
            // Block[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Block.html) of code with controls
            // that may set GUI.changed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html) to true  
  
            if (check.changed)
            {
                // Code to execute if GUI.changed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html)
                // was set to true inside the block of code above.
            }
        }
    }
}

```

Additional resources: [EditorGUI.BeginChangeCheck](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html).
### Properties
Property | Description  
---|---  
[changed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ChangeCheckScope-changed.html) | True if GUI.changed was set to true, otherwise false.  
### Constructors
Constructor | Description  
---|---  
[EditorGUI.ChangeCheckScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ChangeCheckScope-ctor.html) | Begins a ChangeCheckScope.  
* * *
