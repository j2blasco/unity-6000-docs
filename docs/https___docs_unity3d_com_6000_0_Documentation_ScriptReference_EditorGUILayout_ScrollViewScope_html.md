* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ScrollViewScope.html

# ScrollViewScope
class in UnityEditor
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
Disposable helper class for managing [BeginScrollView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginScrollView.html) / [EndScrollView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndScrollView.html).
These work just like [ScrollViewScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ScrollViewScope.html) but feel more application-like and should be used in the editor  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/BeginEndScrollView.png)  
_Label inside a scroll view._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Simple Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Window that creates a scroll view with a Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) inside
class BeginEndScrollView : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPos;
    string t = "This is a string inside a Scroll view!";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Write text on ScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView.html)")]
    static void Init()
    {
        var window = GetWindow<BeginEndScrollView>();
        window.Show();
    }  
  
    void OnGUI()
    {
        using (var h = new EditorGUILayout.HorizontalScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.HorizontalScope.html)())
        {
            using (var scrollView = new EditorGUILayout.ScrollViewScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ScrollViewScope.html)(scrollPos, GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(100), GUILayout.Height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html)(100)))
            {
                scrollPos = scrollView.scrollPosition;
                GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)(t);
            }
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Add More Text", GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(100), GUILayout.Height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html)(100)))
                t += " \nAnd this is more text!";
        }
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Clear"))
            t = "";
    }
}

```

### Properties
Property | Description  
---|---  
[handleScrollWheel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ScrollViewScope-handleScrollWheel.html) | Whether this ScrollView should handle scroll wheel events. (default: true).  
[scrollPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ScrollViewScope-scrollPosition.html) | The modified scrollPosition. Feed this back into the variable you pass in, as shown in the example.  
### Constructors
Constructor | Description  
---|---  
[EditorGUILayout.ScrollViewScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ScrollViewScope-ctor.html) | Create a new ScrollViewScope and begin the corresponding ScrollView.  
* * *
