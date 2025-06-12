* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo-postprocessModifications.html

#  [Undo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html).postprocessModifications
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
[Undo.PostprocessModifications](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.PostprocessModifications.html) postprocessModifications; 
### Description
Callback that is triggered whenever a new set of property modifications is created.
Additional resources: [PostprocessModifications](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.PostprocessModifications.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class ExamplePostprocessModificationScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Undo.postprocessModifications[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo-postprocessModifications.html) += MyPostprocessModificationsCallback;
    }  
  
    void OnDestroy()
    {
        Undo.postprocessModifications[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo-postprocessModifications.html) -= MyPostprocessModificationsCallback;
    }  
  
    UndoPropertyModification[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UndoPropertyModification.html)[] MyPostprocessModificationsCallback(UndoPropertyModification[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UndoPropertyModification.html)[] modifications)
    {
        // here, you can perform processing of the recorded modifications before returning them
        return modifications;
    }
}

```

* * *
