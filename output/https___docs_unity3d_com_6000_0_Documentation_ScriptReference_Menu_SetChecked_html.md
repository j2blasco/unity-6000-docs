* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.SetChecked.html

#  [Menu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html).SetChecked
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
public static void SetChecked(string menuPath, bool isChecked); 
### Description
Sets the check status of a menu item.
The check status of a menu item is cleared when the Editor restarts.
```
    using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
    using UnityEngine;  
  
    public class CheckMenuTest: MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
    {
        // Add a menu item named "MenuTest" to MyMenu in the main menu.    
        [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("MyMenu/MenuTest")]
        static void DoSomething()
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("A placeholder menu item.");         
        }
        
        // Add a menu item that you can click to add a check to the "MenuTest" menu item in MyMenu in the main menu. 
        [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("MyMenu/Check menu item")]
        static void CheckMenu()
        {
            Menu.SetChecked[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.SetChecked.html)("MyMenu/MenuTest", true);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Checked 'MenuTest'");            
        }
        
        // Add a menu item that you can click to clear the check from the "MenuTest" menu item in MyMenu in the main menu. 
        [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("MyMenu/Clear check from menu")]
        static void ClearCheck()
        {
            Menu.SetChecked[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.SetChecked.html)("MyMenu/MenuTest", false);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Cleared check from menu");
        }
    }

```

* * *
