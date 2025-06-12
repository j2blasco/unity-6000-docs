* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).ObjectField
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
public static Object ObjectField([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, Type objType, bool allowSceneObjects, params GUILayoutOption[] options); 
## Declaration
public static Object ObjectField(string label, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, Type objType, bool allowSceneObjects, params GUILayoutOption[] options); 
## Declaration
public static Object ObjectField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, Type objType, bool allowSceneObjects, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label in front of the field.  
obj | The object the field shows.  
objType | The type of the objects that can be assigned.  
allowSceneObjects | Allow assigning Scene objects. See Description for more info.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`. Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**Object** The object that has been set by the user. 
### Description
Make a field to receive any object type.
You can assign objects either by drag and drop or by selecting an object using the Object Picker.  
  
Ensure that the **allowSceneObjects** parameter is false if the object reference is stored as part of an asset, since assets can't store references to objects in a Scene.  
  
If the ObjectField is part of a custom Editor for a script component, use EditorUtility.IsPersistent() to check if the component is on an asset or a Scene object.  
  
See the example in the [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) class for further information.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/QuickHelperObjectField.png)  
_Search for a help page by selecting the GameObject in the Object Field._
```
// EditorScript that quickly searches for a help page
// about the selected Object.
//
// If no such page is found in the Manual it opens the Unity forum.  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    public Object source;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectField.html) Example _h")]
    static void Init()
    {
        var window = GetWindowWithRect<ExampleClass>(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 165, 100));
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        source = EditorGUILayout.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html)(source, typeof(Object), true);
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Search!"))
        {
            if (source == null)
                ShowNotification(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("No object selected for searching"));
            else if (Help.HasHelpForObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Help.HasHelpForObject.html)(source))
                Help.ShowHelpForObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Help.ShowHelpForObject.html)(source);
            else
                Help.BrowseURL[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Help.BrowseURL.html)("https://forum.unity3d.com/search.php");
        }
    }
}

```

  
  
You can also use the **options** parameter to change the look of the control. The following example changes the look of a Sprite ObjectField that is displayed with a large field format.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/SpriteObjectField.png)  
_Two different layout options for a sprite field._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class SpriteExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    public Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) sprite;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectField.html) Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) Example")]
    static void Init()
    {
        var window = GetWindowWithRect<SpriteExample>(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 165, 100));
        window.Show();
    }  
  
    void OnGUI()
    {
        sprite = EditorGUILayout.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html)(sprite, typeof(Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)), false, GUILayout.Height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html)(EditorGUIUtility.singleLineHeight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-singleLineHeight.html))) as Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html);
    }
}

```

* * *
## Declaration
public static void ObjectField([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, params GUILayoutOption[] options); 
## Declaration
public static void ObjectField([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, params GUILayoutOption[] options); 
## Declaration
public static void ObjectField([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, Type objType, params GUILayoutOption[] options); 
## Declaration
public static void ObjectField([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, Type objType, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
property | The object reference property the field shows.  
objType | The type of the objects that can be assigned.  
label | Optional label in front of the field. Pass [GUIContent.none](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-none.html) to hide the label.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Description
Make a field to receive any object type.
Obsoleted. Use the overloads at the top of the page, with the **allowSceneObjects** parameter.
* * *
