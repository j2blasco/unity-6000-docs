* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutManager.UnregisterContext.html

#  [ShortcutManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutManager.html).UnregisterContext
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
public static void UnregisterContext([ShortcutManagement.IShortcutContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutContext.html) context); 
### Parameters
Parameter | Description  
---|---  
context | The custom context to remove from the shortcut context list.  
### Description
Removes a [IShortcutContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutContext.html) from the shortcut context list.
Additional resources: [ShortcutManager.RegisterContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutManager.RegisterContext.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.ShortcutManagement;
using UnityEngine;

public class ShortcutContextSample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    public class CustomShortcutContext : IShortcutContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutContext.html)
    {
        public bool active
        {
            get
            {
                if (!(focusedWindow is ShortcutContextSample view))
                    return false;

                return view.toggleValue;
            }
        }
    }

    [Shortcut("Custom Shortcut Context/Sample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.UI.Sample.html) Shortcut", typeof(CustomShortcutContext), KeyCode.Mouse1[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse1.html))]
    static void SampleShortcut(ShortcutArguments[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutArguments.html) args)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The sample shortcut was called.");
    }

    bool m_ToggleValue = false;
    public bool toggleValue => m_ToggleValue;

    CustomShortcutContext m_ShortcutContext = new CustomShortcutContext();

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Custom Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Window")]
    public static void ShowWindow()
    {
        ShortcutContextSample wnd = GetWindow<ShortcutContextSample>();
        wnd.titleContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Custom Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Window");
    }

    void OnGUI()
    {
        var content = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html)", "Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) to activate the shortcut context.");
        m_ToggleValue = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)(content, m_ToggleValue);
    }

    private void OnEnable()
    {
        ShortcutManager.RegisterContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutManager.RegisterContext.html)(m_ShortcutContext);
    }

    private void OnDisable()
    {
        ShortcutManager.UnregisterContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutManager.UnregisterContext.html)(m_ShortcutContext);
    }
}

```

* * *
