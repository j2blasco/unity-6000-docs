* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterCreatedObjectUndo.html

#  [Undo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html).RegisterCreatedObjectUndo
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
public static void RegisterCreatedObjectUndo([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) objectToUndo, string name); 
### Parameters
Parameter | Description  
---|---  
objectToUndo | The newly created object. This object is destroyed when the undo operation is performed. When the value is a GameObject, Unity registers the GameObject and its child GameObjects, but not sibling or parent GameObjects.  
name | The name of the action to undo. Use this string to provide a short description of the action to be undone. For **Undo** or **Redo** items in the **Edit** menu, Unity adds "Undo" or "Redo" to the string that you provide. For example, if you provide the string "Create GameObject", the Unity Editor displays the menu item **Edit** > **Undo Create GameObject**.  
### Description
Registers an undo operation to undo the creation of an object.
This method registers the creation of an object to the undo stack so that users can undo a create object action. Use this method each time you define an action that creates an object, for example, inside a custom Editor or menu item. Unity updates the undo action in the **Edit** menu with the name of the undo operation. When the user performs the undo action, Unity destroys the object.  
  
**Note:** The undo process destroys objects in the same way as [Object.Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html), but with no delay.  
  
When you create and modify an object at the same time, use the following workflow to ensure that [Undo.RegisterCreatedObjectUndo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterCreatedObjectUndo.html) saves all updates to the object: 
  1. Create the object.
  2. Register the object as created with `Undo.RegisterCreatedObjectUndo`.
  3. Register the object with [Undo.RegisterCompleteObjectUndo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterCompleteObjectUndo.html) so that the Editor records changes to the object. If the object has any child GameObjects, register it with [Undo.RegisterFullObjectHierarchyUndo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterFullObjectHierarchyUndo.html) instead.
  4. Update the object.


If you do not follow this workflow, `Undo.RegisterCreatedObjectUndo` might not save any updates to the object other than object creation.  
  
When you register a new object with `Undo.RegisterCreatedObjectUndo`, Unity registers any changes to objects that are currently recorded by [Undo.RecordObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html) and then stops recording. This means that after you register a new object, Unity does not record any subsequent changes to any other objects that `Undo.RecordObject` was already recording.  
  
When Unity is already recording changes to existing objects with `Undo.RecordObject` and you want to register newly created objects, it is best practice to follow this workflow: 
  1. Complete any changes you want to make to objects that `Undo.RecordObject` is recording. Unity calls [Undo.FlushUndoRecordObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.FlushUndoRecordObjects.html) automatically.
  2. Register newly created objects with `Undo.RegisterCreatedObjectUndo`.


If you do not follow this workflow, Unity might not store the state of the recorded objects on the undo stack correctly.  
  
The following example shows how to create and modify a GameObject with a child as an operation that can be undone in a single undo step.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
class CreateGameObjectMenu
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Create GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)")]
    static void CreateGameObject()
    {
        // Create new undo group
        Undo.IncrementCurrentGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.IncrementCurrentGroup.html)();  
  
        // Create GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) hierarchy
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("my GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)");
        Undo.RegisterCreatedObjectUndo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterCreatedObjectUndo.html)(go, "Create my GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)");
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) child = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)();
        Undo.RegisterCreatedObjectUndo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterCreatedObjectUndo.html)(child, "Create child");
        Undo.SetTransformParent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.SetTransformParent.html)(child.transform, go.transform, "Modify parent");  
  
        // Move GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) hierarchy
        Undo.RegisterFullObjectHierarchyUndo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterFullObjectHierarchyUndo.html)(go, "Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) my GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) position");
        go.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(5, 5, 5);  
  
        // Name undo group
        Undo.SetCurrentGroupName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.SetCurrentGroupName.html)("Create and Reposition GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with Child");
    }
}

```

**Note:** This operation cannot be performed when [isProcessing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo-isProcessing.html) is `true`.
* * *
