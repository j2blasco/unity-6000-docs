* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView-useScrollView.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).useScrollView
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
useScrollView; 
### Description
When drawing the TreeView contents, will it be enclosed within a ScrollView?
When enabled, the contents of the TreeView is culled so that anything outside of the ScrollView is not drawn. If the TreeView is contained within an external ScrollView, such as the Inspector window, then disabling this allows the TreeView to use the external ScrollView to perform its culling.
```
using UnityEngine;  
  
public class ExampleBehaviourScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // This is our example list.
    public string[] exampleList;
}

```

To use the following script, add it to the Editor directory.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.IMGUI.Controls;
using UnityEngine;  
  
// Simple TreeView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html) that draws a single list property.
class NewBehaviourScriptEditorTreeView : TreeView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html)
{
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) m_Property;  
  
    public NewBehaviourScriptEditorTreeView(SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property) :
        base(new TreeViewState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewState.html)())
    {
        m_Property = property;
        showBorder = true;
        showAlternatingRowBackgrounds = true;
        useScrollView = false; // We are using the Inspector ScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView.html)  
  
        MultiColumnHeaderState.Column[] columns = new MultiColumnHeaderState.Column[2];
        for (int i = 0; i < columns.Length; ++i)
        {
            columns[i] = new MultiColumnHeaderState.Column();
            columns[i].minWidth = 50;
            columns[i].width = 100;
            columns[i].headerTextAlignment = TextAlignment.Center[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAlignment.Center.html);
            columns[i].canSort = false;
        }
        columns[0].headerContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Index");
        columns[1].headerContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Value");
        var multiColState = new MultiColumnHeaderState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeaderState.html)(columns);
        multiColumnHeader = new MultiColumnHeader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html)(multiColState);
        multiColumnHeader.ResizeToFit();
        Reload();
    }  
  
    protected override TreeViewItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) BuildRoot()
    {
        int arraySize = m_Property.arraySize;  
  
        var root = new TreeViewItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) { id = -1, depth = -1, displayName = "Root" };
        var allItems = new List<TreeViewItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html)>(arraySize);
        for (int i = 0; i < arraySize; ++i)
        {
            var item = new TreeViewItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html)(i, 0, i.ToString());
            allItems.Add(item);
        }  
  
        SetupParentsAndChildrenFromDepths(root, allItems);
        return root;
    }  
  
    protected override void RowGUI(RowGUIArgs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs.html) args)
    {
        var prop = m_Property.GetArrayElementAtIndex(args.item.id);
        for (int i = 0; i < args.GetNumVisibleColumns(); ++i)
        {
            int col = args.GetColumn(i);
            var rect = args.GetCellRect(i);  
  
            if (col == 0)
            {
                GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(rect, args.row.ToString());
            }
            else
            {
                EditorGUI.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyField.html)(rect, prop, GUIContent.none[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-none.html));
            }
        }
    }
}  
  
// Shows how we can use a TreeView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html) to draw a large list of items.
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ExampleBehaviourScript))]
[CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
public class NewBehaviourScriptEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    NewBehaviourScriptEditorTreeView m_TreeView;
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) m_Size;  
  
    void OnEnable()
    {
        var listProperty = serializedObject.FindProperty("exampleList");
        m_Size = serializedObject.FindProperty("exampleList.Array.size");
        m_TreeView = new NewBehaviourScriptEditorTreeView(listProperty);
        Undo.undoRedoPerformed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo-undoRedoPerformed.html) += m_TreeView.Reload;
    }  
  
    void OnDisable()
    {
        if (m_TreeView != null)
            Undo.undoRedoPerformed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo-undoRedoPerformed.html) -= m_TreeView.Reload;
    }  
  
    public override void OnInspectorGUI()
    {
        serializedObject.Update();
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        int newSize = EditorGUILayout.IntField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntField.html)("Size", m_Size.intValue);
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            m_Size.intValue = newSize;
            m_TreeView.Reload();
        }  
  
        var rect = EditorGUILayout.GetControlRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.GetControlRect.html)(false, m_TreeView.totalHeight);
        m_TreeView.OnGUI(rect);
        serializedObject.ApplyModifiedProperties();
    }
}

```

* * *
