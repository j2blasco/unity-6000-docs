* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html

# Editor
class in UnityEditor
/
Inherits from:[ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
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
Derive from this base class to create a custom inspector or editor for your custom object.
```
using UnityEngine;
using System.Collections;  
  
// This is not an editor script.
public class MyPlayer : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int armor = 75;
    public int damage = 25;
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gun;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) logic here...
    }
}

```

For example, use a custom editor to change the appearance of the script in the Inspector.  
  
You can attach the Editor to a custom component by using the [CustomEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html) attribute.  
  
There are multiple ways to design custom Editors. If you want the Editor to support multi-object editing, you can use the [CanEditMultipleObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html) attribute. Instead of modifying script variables directly, it's advantageous to use the [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) and [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) system to edit them, since this automatically handles multi-object editing, undo, and Prefab overrides. If this approach is used a user can select multiple assets in the hierarchy window and change the values for all of them at once.  
  
You can either use UIElements to build your custom UI or you can use IMGUI. To create a custom inspector using UIElements, you have to override the [Editor.CreateInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateInspectorGUI.html) on the [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) class. To create a custom inspector using IMGUI, you have to override the [Editor.OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInspectorGUI.html) on the [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) class. If you use UIElements and have [Editor.CreateInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateInspectorGUI.html) overwritten, any existing IMGUI implementation using [Editor.OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInspectorGUI.html) on the same Editor will be ignored.  
  
Here's an example of a custom inspector:  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/CustomEditorUIElements.png)  
_Custom editor in the Inspector._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.UIElements;
using UnityEngine;
using UnityEngine.UIElements;
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(MyPlayer))]
public class MyPlayerEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    const string resourceFilename = "custom-editor-uie";
    public override VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) CreateInspectorGUI()
    {
        VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) customInspector = new VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)();
        var visualTree = Resources.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html)(resourceFilename) as VisualTreeAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualTreeAsset.html);
        visualTree.CloneTree(customInspector);
        customInspector.styleSheets.Add(Resources.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html)($"{resourceFilename}-style") as StyleSheet[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleSheet.html));
        return customInspector;
    }
}
```

The following example defines the layout of a custom inspector in uxml. The definition loads as a resource and the [VisualTreeAsset.CloneTree](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualTreeAsset.CloneTree.html) method puts the hierarchy in a [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) object.  
  
The InspectorWindow will instantiate an [InspectorElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.html) containing the custom inspector. The [InspectorElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.html) will call Bind on the custom inspector binding it to the MyPlayer object.
```
<UXML xmlns="UnityEngine.UIElements" xmlns:e="UnityEditor.UIElements">
    <VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class="player-property">
        <VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class="slider-row">
            <Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) class="player-property-label" text="Damage"/>
            <VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class="input-container">
                <SliderInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SliderInt.html) class="player-slider" name="damage-slider" high-value="100" direction="Horizontal" binding-path="damage"/>
                <e:IntegerField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IntegerField.html) class="player-int-field" binding-path="damage"/>
            </VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)>
        </VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)>
        <e:ProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ProgressBar.html) class="player-property-progress-bar" name="damage-progress" binding-path="damage" title="Damage"/>
    </VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)>  
  
    <VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class="player-property">
        <VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class="slider-row">
            <Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) class="player-property-label" text="Armor"/>
            <VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class="input-container">
                <SliderInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SliderInt.html) class="player-slider" name="armor-slider" high-value="100" direction="Horizontal" binding-path="armor"/>
                <e:IntegerField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IntegerField.html) class="player-int-field" binding-path="armor"/>
            </VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)>
        </VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)>
        <e:ProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ProgressBar.html) class="player-property-progress-bar" name="armor-progress" binding-path="armor" title="Armor"/>
    </VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)>  
  
    <e:PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropertyField.html) class="gun-field" binding-path="gun" label="Gun Object"/>
</UXML>
```

UIElements automatically updates the UI when data changes and vice-versa. To bind data and automatically update data and UI, set values for the "binding-path" attributes.  
  
Styling of the inspector is done in uss.
```
.slider-row {
    flex-direction: row;
    justify-content: space-between;
    margin-top: 4px;
}
.input-container {
    flex-direction: row;
    flex-grow: .6;
    margin-right: 4px;
}
.player-property {
    margin-bottom: 4px;
}
.player-property-label {
    flex:1;
    margin-left: 16;
}
.player-slider {
    flex:3;
    margin-right: 4px;
}
.player-property-progress-bar {
    margin-left: 16px;
    margin-right: 4px;
}
.player-int-field {
    min-width: 48px;
}
.gun-field {
    justify-content: space-between;
    margin-left: 16px;
    margin-right: 4px;
    margin-top: 6px;
    flex-grow: .6;
}
```

Here's an example of a custom inspector using IMGUI and multi-selection:
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
// Custom Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) using SerializedProperties.
// Automatic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGame.Automatic.html) handling of multi-object editing, undo, and Prefab overrides.
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(MyPlayer))]
[CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
public class MyPlayerEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) damageProp;
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) armorProp;
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) gunProp;  
  
    void OnEnable()
    {
        // Setup the SerializedProperties.
        damageProp = serializedObject.FindProperty ("damage");
        armorProp = serializedObject.FindProperty ("armor");
        gunProp = serializedObject.FindProperty ("gun");
    }  
  
    public override void OnInspectorGUI()
    {
        // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) the serializedProperty - always do this in the beginning of OnInspectorGUI.
        serializedObject.Update ();  
  
        // Show the custom GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) controls.
        EditorGUILayout.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntSlider.html) (damageProp, 0, 100, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) ("Damage"));  
  
        // Only show the damage progress bar if all the objects have the same damage value:
        if (!damageProp.hasMultipleDifferentValues)
            ProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ProgressBar.html) (damageProp.intValue / 100.0f, "Damage");  
  
        EditorGUILayout.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntSlider.html) (armorProp, 0, 100, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) ("Armor"));  
  
        // Only show the armor progress bar if all the objects have the same armor value:
        if (!armorProp.hasMultipleDifferentValues)
            ProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ProgressBar.html) (armorProp.intValue / 100.0f, "Armor");  
  
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html) (gunProp, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) ("Gun Object"));  
  
        // Apply changes to the serializedProperty - always do this in the end of OnInspectorGUI.
        serializedObject.ApplyModifiedProperties ();
    }  
  
    // Custom GUILayout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html) progress bar.
    void ProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ProgressBar.html) (float value, string label)
    {
        // Get a rect for the progress bar using the same margins as a textfield:
        Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect = GUILayoutUtility.GetRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutUtility.GetRect.html) (18, 18, "TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField.html)");
        EditorGUI.ProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ProgressBar.html) (rect, value, label);
        EditorGUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Space.html) ();
    }
}

```

If automatic handling of multi-object editing, undo, and Prefab overrides is not needed, the script variables can be modified directly by the editor without using the [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) and [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) system, as in the IMGUI example below.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
// Example script with properties.
public class MyPlayerAlternative : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int damage;
    public int armor;
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gun;  
  
    // ...other code...
}  
  
// Custom Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) the "old" way by modifying the script variables directly.
// No handling of multi-object editing, undo, and Prefab overrides!
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html) (typeof(MyPlayerAlternative))]
public class MyPlayerEditorAlternative : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{  
  
    public override void OnInspectorGUI()
    {
        MyPlayerAlternative mp = (MyPlayerAlternative)target;  
  
        mp.damage = EditorGUILayout.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntSlider.html) ("Damage", mp.damage, 0, 100);
        ProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ProgressBar.html) (mp.damage / 100.0f, "Damage");  
  
        mp.armor = EditorGUILayout.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntSlider.html) ("Armor", mp.armor, 0, 100);
        ProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ProgressBar.html) (mp.armor / 100.0f, "Armor");  
  
        bool allowSceneObjects = !EditorUtility.IsPersistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsPersistent.html) (target);
        mp.gun = (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))EditorGUILayout.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html) ("Gun Object", mp.gun, typeof(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)), allowSceneObjects);
    }  
  
    // Custom GUILayout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html) progress bar.
    void ProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ProgressBar.html) (float value, string label)
    {
        // Get a rect for the progress bar using the same margins as a textfield:
        Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect = GUILayoutUtility.GetRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutUtility.GetRect.html) (18, 18, "TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField.html)");
        EditorGUI.ProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ProgressBar.html) (rect, value, label);
        EditorGUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Space.html) ();
    }
}

```

### Properties
Property | Description  
---|---  
[hasUnsavedChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-hasUnsavedChanges.html) | This property specifies whether the Editor prompts the user to save or discard unsaved changes before the Inspector gets rebuilt.  
[saveChangesMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-saveChangesMessage.html) | The message that displays to the user if they are prompted to save.  
[serializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-serializedObject.html) | A SerializedObject representing the object or objects being inspected.  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-target.html) | The object being inspected.  
[targets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-targets.html) | An array of all the object being inspected.  
### Public Methods
Method | Description  
---|---  
[CreateInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateInspectorGUI.html) | Implement this method to make a custom UIElements inspector.  
[CreatePreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreatePreview.html) | Implement this method to make a custom UIElements inspector preview.  
[DiscardChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DiscardChanges.html) | Discards unsaved changes to the contents of the editor.  
[DrawDefaultInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawDefaultInspector.html) | Draws the built-in Inspector.  
[DrawHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawHeader.html) | Call this function to draw the header of the editor.  
[DrawPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawPreview.html) | The first entry point for Preview Drawing.  
[GetInfoString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.GetInfoString.html) | Implement this method to show asset information on top of the asset preview.  
[GetPreviewTitle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.GetPreviewTitle.html) | Override this method if you want to change the label of the Preview area.  
[HasPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.HasPreviewGUI.html) | Override this method in subclasses if you implement OnPreviewGUI.  
[OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInspectorGUI.html) | Implement this function to make a custom inspector.  
[OnInteractivePreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInteractivePreviewGUI.html) | Implement to create your own interactive custom preview. Interactive custom previews are used in the preview area of the inspector and the object selector.  
[OnPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnPreviewGUI.html) | Creates a custom preview for the preview area of the Inspector, the headers of the primary Editor, and the object selector.You must implement Editor.HasPreviewGUI for this method to be called.  
[OnPreviewSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnPreviewSettings.html) | Override this method if you want to show custom controls in the preview header.  
[RenderStaticPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.RenderStaticPreview.html) | Override this method if you want to render a static preview.  
[Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.Repaint.html) | Redraw any inspectors that shows this editor.  
[RequiresConstantRepaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.RequiresConstantRepaint.html) | Checks if this editor requires constant repaints in its current state.  
[SaveChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.SaveChanges.html) | Performs a save action on the contents of the editor.  
[UseDefaultMargins](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.UseDefaultMargins.html) | Override this method in subclasses to return false if you don't want default margins.  
### Protected Methods
Method | Description  
---|---  
[ShouldHideOpenButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.ShouldHideOpenButton.html) | Returns the visibility setting of the "open" button in the Inspector.  
### Static Methods
Method | Description  
---|---  
[CreateCachedEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateCachedEditor.html) | On return previousEditor is an editor for targetObject or targetObjects. The function either returns if the editor is already tracking the objects, or destroys the previous editor and creates a new one.  
[CreateCachedEditorWithContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateCachedEditorWithContext.html) | Creates a cached editor using a context object.  
[CreateEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateEditor.html) | Make a custom editor for targetObject or targetObjects.  
[CreateEditorWithContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateEditorWithContext.html) | Make a custom editor for targetObject or targetObjects with a context object.  
[DrawFoldoutInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawFoldoutInspector.html) | Draws the inspector GUI with a foldout header for target.  
### Messages
Message | Description  
---|---  
[HasFrameBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.HasFrameBounds.html) | Validates whether custom bounds can be calculated for this Editor.  
[OnGetFrameBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnGetFrameBounds.html) | Gets custom bounds for the target of this editor.  
[OnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnSceneGUI.html) | Enables the Editor to handle an event in the Scene view.  
### Events
Event | Description  
---|---  
[finishedDefaultHeaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-finishedDefaultHeaderGUI.html) | An event raised while drawing the header of the Inspector window, after the default header items have been drawn.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
[CreateInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html) | Creates an instance of a scriptable object.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
### Messages
Message | Description  
---|---  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Awake.html) | Called when an instance of ScriptableObject is created.  
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDestroy.html) | This function is called when the scriptable object will be destroyed.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html) | This function is called when the scriptable object goes out of scope.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html) | This function is called when the object is loaded.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html) | Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Reset.html) | Reset to default values.  
* * *
