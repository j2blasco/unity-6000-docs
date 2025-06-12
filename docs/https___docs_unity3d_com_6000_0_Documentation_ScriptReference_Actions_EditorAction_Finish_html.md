* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.Finish.html

#  [EditorAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.html).Finish
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
## Declaration
public void Finish([Actions.EditorActionResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorActionResult.html) result); 
### Parameters
Parameter | Description  
---|---  
result | The state that the [EditorAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.html) was finished in.  
### Description
Finishes an [EditorAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.html) with a specific result.
Call this method to forcibly end an active [EditorAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.html) with a [EditorActionResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorActionResult.html). A common use is when implementing atomic actions that do not require interactivity.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Actions;

public class SingleFrameActionSample : EditorAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Test/Start Single Frame Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)")]
    static void StartEditorActionSample()
    {
        Start(new SingleFrameActionSample(4));
    }

    int m_Value;

    public SingleFrameActionSample(int value)
    {
        m_Value = value;
        Finish(EditorActionResult.Success[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorActionResult.Success.html));
    }

    protected override void OnFinish(EditorActionResult[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorActionResult.html) result)
    {
        m_Value += 2;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) Finished [{result}] with value: {m_Value}");
    }
}


```

* * *
