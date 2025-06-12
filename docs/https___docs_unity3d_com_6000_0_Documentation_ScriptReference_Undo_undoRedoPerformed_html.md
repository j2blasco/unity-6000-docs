* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo-undoRedoPerformed.html

#  [Undo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html).undoRedoPerformed
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
[Undo.UndoRedoCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.UndoRedoCallback.html) undoRedoPerformed; 
### Description
Callback that is triggered after an undo or a redo was executed.
For more information on whether the callback was called from an undo or a redo, use [undoRedoEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo-undoRedoEvent.html) instead.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Undo.undoRedoPerformed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo-undoRedoPerformed.html) += MyUndoRedoCallback;
    }  
  
    void MyUndoRedoCallback()
    {
        // code for the action to take on Undo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html)/Redo
    }
}

```

* * *
