* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DisabledScope.html

# DisabledScope
struct in UnityEditor
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
Create a group of controls that can be disabled.
If disabled is true, the controls inside the group will be disabled. If false, the enabled/disabled state will not be changed.  
  
The group cannot be used to enable controls that would otherwise be disabled to begin with. The groups can be nested and the controls within a child group will be disabled either if that child group is itself disabled or if a parent group is.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class ExampleClass
{
    bool canJump = false;
    float jumpHeight = 0f;  
  
    void Example()
    {
        canJump = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("Can Jump", canJump);  
  
        // Disable the jumping height control if canJump is false:
        using (new EditorGUI.DisabledScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DisabledScope.html)(canJump == false))
        {
            jumpHeight = EditorGUILayout.FloatField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.FloatField.html)("Jump Height", jumpHeight);
        }
    }
}

```

### Constructors
Constructor | Description  
---|---  
[EditorGUI.DisabledScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DisabledScope-ctor.html) | Create a new DisabledScope and begin the corresponding group.  
* * *
