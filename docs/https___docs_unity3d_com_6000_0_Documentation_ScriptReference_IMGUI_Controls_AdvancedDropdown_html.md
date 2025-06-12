* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdown.html

# AdvancedDropdown
class in UnityEditor.IMGUI.Controls
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
Inherit from this class to implement your own drop-down control.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEditor.IMGUI.Controls;  
  
class WeekdaysDropdown : AdvancedDropdown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdown.html)
{
    public WeekdaysDropdown(AdvancedDropdownState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownState.html) state) : base(state)
    {
    }  
  
    protected override AdvancedDropdownItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownItem.html) BuildRoot()
    {
        var root = new AdvancedDropdownItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownItem.html)("Weekdays");  
  
        var firstHalf = new AdvancedDropdownItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownItem.html)("First half");
        var secondHalf = new AdvancedDropdownItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownItem.html)("Second half");
        var weekend = new AdvancedDropdownItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownItem.html)("Weekend");  
  
        firstHalf.AddChild(new AdvancedDropdownItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownItem.html)("Monday"));
        firstHalf.AddChild(new AdvancedDropdownItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownItem.html)("Tuesday"));
        secondHalf.AddChild(new AdvancedDropdownItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownItem.html)("Wednesday"));
        secondHalf.AddChild(new AdvancedDropdownItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownItem.html)("Thursday"));
        weekend.AddChild(new AdvancedDropdownItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownItem.html)("Friday"));
        weekend.AddChild(new AdvancedDropdownItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownItem.html)("Saturday"));
        weekend.AddChild(new AdvancedDropdownItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownItem.html)("Sunday"));  
  
        root.AddChild(firstHalf);
        root.AddChild(secondHalf);
        root.AddChild(weekend);  
  
        return root;
    }
}  
  
public class AdvancedDropdownTestWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    void OnGUI()
    {
        var rect = GUILayoutUtility.GetRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutUtility.GetRect.html)(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Show"), EditorStyles.toolbarButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-toolbarButton.html));
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(rect, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Show"), EditorStyles.toolbarButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-toolbarButton.html)))
        {
            var dropdown = new WeekdaysDropdown(new AdvancedDropdownState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownState.html)());
            dropdown.Show(rect);
        }
    }
}

```

### Properties
Property | Description  
---|---  
[minimumSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdown-minimumSize.html) | Minimum size of the drop-down window. By default, the drop-down will try to match the width of the given rect or the rendered content.  
### Public Methods
Method | Description  
---|---  
[Show](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdown.Show.html) | Call this method to show the drop-down at the given position.  
### Protected Methods
Method | Description  
---|---  
[BuildRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdown.BuildRoot.html) | Implement this method to generate the content of the drop-down. This method is called when the drop-down is being shown.  
[ItemSelected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdown.ItemSelected.html) | Override this method to get notified when an item is selected.  
* * *
