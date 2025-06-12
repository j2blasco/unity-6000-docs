* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-sortingOrder.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).sortingOrder
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
sortingOrder; 
### Description
Renderer's order within a sorting layer.
You can group GameObjects into layers in their [SpriteRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) component. This is called the [SortingLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.html). The sorting order decides what priority each GameObject has to the Renderer within each Sorting Layer. The lower the number you give it, the further back the GameObject appears. The higher the number, the closer the GameObject looks to the Camera. This is very effective when creating 2D scroller games, as you may want certain GameObjects on the same layer but certain parts to appear in front of others, for example, layering clouds and making them appear in front of the sky.  
  
**Note** : The value must be between -32768 and 32767.
```
//Attach a script like this to a Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (**Create**>**2D Object**>**Sprite**). Assign a Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) to it in the Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) field.
//Repeat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Repeat.html) the first step for another two Sprites and make them overlap each other slightly. This shows how the order number changes the view of the Sprites.  
  
using UnityEngine;
public class MyScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int MyOrder;
    public string MyName;
}

```

```
//Create a folder named “Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)” (Right click in your Assets folder, **Create**>**Folder**)
//Put this script in the folder.
//This script adds fields to the Inspector of your GameObjects with the MyScript script attached. Edit the fields to change the layer and order number each Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) belongs to.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Custom Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) using SerializedProperties.  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(MyScript))]
public class MeshSortingOrderExample : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) m_Name;
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) m_Order;  
  
    private SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) rend;  
  
    void OnEnable()
    {
        // Fetch the properties from the MyScript script and set up the SerializedProperties.
        m_Name = serializedObject.FindProperty("MyName");
        m_Order = serializedObject.FindProperty("MyOrder");
    }  
  
    void CheckRenderer()
    {
        //Check that the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you select in the hierarchy has a SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) component
        if (Selection.activeGameObject.GetComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>())
        {
            //Fetch the SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) from the selected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
            rend = Selection.activeGameObject.GetComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>();
            //Change the sorting layer to the name you specify in the TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField.html)
            //Changes to Default if the name you enter doesn't exist
            rend.sortingLayerName = m_Name.stringValue;
            //Change the order (or priority) of the layer
            rend.sortingOrder = m_Order.intValue;
        }
    }  
  
    public override void OnInspectorGUI()
    {
        // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) the serializedProperty - always do this in the beginning of OnInspectorGUI.
        serializedObject.Update();
        //Create fields for each SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html)
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(m_Name, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Name"));
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(m_Order, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Order"));
        //Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) the name and order of the Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) properties
        CheckRenderer();  
  
        // Apply changes to the serializedProperty - always do this in the end of OnInspectorGUI.
        serializedObject.ApplyModifiedProperties();
    }
}

```

* * *
