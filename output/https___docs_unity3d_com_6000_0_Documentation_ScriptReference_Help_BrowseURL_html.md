* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Help.BrowseURL.html

#  [Help](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Help.html).BrowseURL
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
public static void BrowseURL(string url); 
### Description
Open `url` in the default web browser.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/QuickHelper.png)   
_Editor Window that lets you load docs for any Selected GameObject._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// EditorScript that quickly searchs for a help page
// of the selected Object.
//
// If there is no page found on the Manual it opens the Unity forum.  
  
class QuickHelper : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    Object source;  
  
    [@MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/QuickHelper _h")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = EditorWindow.GetWindowWithRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindowWithRect.html)(typeof(QuickHelper), new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 165, 100));
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        source = EditorGUILayout.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html)(source, typeof(Object));
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Search!"))
        {
            if (source == null)
            {
                this.ShowNotification(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("No object selected for searching"));
            }
            else
            {
                if (Help.HasHelpForObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Help.HasHelpForObject.html)(source))
                {
                    Help.ShowHelpForObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Help.ShowHelpForObject.html)(source);
                }
                else
                {
                    Help.BrowseURL[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Help.BrowseURL.html)("https://forum.unity3d.com/search.php");
                }
            }
        }
    }
}

```

* * *
