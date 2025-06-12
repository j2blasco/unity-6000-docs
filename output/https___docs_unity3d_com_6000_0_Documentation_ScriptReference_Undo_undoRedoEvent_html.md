* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo-undoRedoEvent.html

#  [Undo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html).undoRedoEvent
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
[Undo.UndoRedoEventCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.UndoRedoEventCallback.html) undoRedoEvent; 
### Description
Callback that is triggered after any undo or redo event.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class ExampleUndoRedoEventScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Undo.undoRedoEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo-undoRedoEvent.html) += OnUndoRedoEvent;
    }  
  
    void OnDestroy()
    {
        Undo.undoRedoEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo-undoRedoEvent.html) -= OnUndoRedoEvent;
    }  
  
    void OnUndoRedoEvent(in UndoRedoInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UndoRedoInfo.html) info)
    {
        // code for the action to take on Undo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html) or Redo event
    }
}

```

* * *
