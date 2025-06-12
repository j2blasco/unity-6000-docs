* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.AddDropHandler.html

#  [DragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.html).AddDropHandler
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
public static void AddDropHandler([DragAndDrop.ProjectBrowserDropHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.ProjectBrowserDropHandler.html) handler); 
## Declaration
public static void AddDropHandler([DragAndDrop.SceneDropHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.SceneDropHandler.html) handler); 
## Declaration
public static void AddDropHandler([DragAndDrop.HierarchyDropHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.HierarchyDropHandler.html) handler); 
## Declaration
public static void AddDropHandler([DragAndDrop.InspectorDropHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.InspectorDropHandler.html) handler); 
### Parameters
Parameter | Description  
---|---  
handler | Function to handle drop on the corresponding window.  
### Description
Allow override of the default behavior for the corresponding window. Multiple handlers can be registered on the same window. If a handler returns [DragAndDropVisualMode.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.None.html) the system will check the next handler. Any other results ([DragAndDropVisualMode.Rejected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.Rejected.html) or others [DragAndDropVisualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.html)) means this handler has processed the drop event and no other handler will be called. The last handler is the default Unity handler.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);  
  
static class DragDropSample
{
    static DragAndDropVisualMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.html) ProjectHandler(int id, string path, bool perform)
    {
        if (perform)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Dropped upon {path} {id}");
        else
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Dragging upon {path} {id}");
        return DragAndDropVisualMode.Move[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.Move.html);
    }  
  
    public static void AddDragProjectHandler()
    {
        // Add the handler
        DragAndDrop.AddDropHandler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.AddDropHandler.html)(ProjectHandler);
    }  
  
    public static void RemoveProjectHandler()
    {
        // Remove the handler
        DragAndDrop.RemoveDropHandler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.RemoveDropHandler.html)(ProjectHandler);
    }
}

```

* * *
