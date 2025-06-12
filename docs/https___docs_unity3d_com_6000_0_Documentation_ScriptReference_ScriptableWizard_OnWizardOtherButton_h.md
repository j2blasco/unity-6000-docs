* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.OnWizardOtherButton.html

#  [ScriptableWizard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html).OnWizardOtherButton()
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
Allows you to provide an action when the user clicks on the other button.
This is the place where you can implement all the stuff that will be done if the user clicks the secondary option when calling DisplayWizard.  
  
Additional resources: [ScriptableWizard.DisplayWizard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.DisplayWizard.html)  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ScriptableWizardOnWizardOtherButton.png)  
_ScriptableWizard with an "Other" button, in this case named "Info"._
```
// Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) a window showing the distance between two objects when clicking the Info button.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ScriptableWizardOnWizardOtherButton : ScriptableWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) firstObject = null;
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) secondObject = null;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Show OnWizardOtherButton Usage")]
    static void CreateWindow()
    {
        ScriptableWizard.DisplayWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.DisplayWizard.html)("Click info to know the distance between the objects",
            typeof(ScriptableWizardOnWizardOtherButton), "Finish!", "Info");
    }  
  
    void OnWizardUpdate()
    {
        if (firstObject == null || secondObject == null)
        {
            isValid = false;
            errorString = "Select the objects you want to measure";
        }
        else
        {
            isValid = true;
            errorString = "";
        }
    }  
  
    // Called when you press the "Info" button.
    void OnWizardOtherButton()
    {
        float distanceObjs = Vector3.Distance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Distance.html)(firstObject.position, secondObject.position);
        EditorUtility.DisplayDialog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayDialog.html)(
            "The distance between the objects is: " + distanceObjs + " Units",
            "",
            "OK");
    }  
  
    // Called when you press the "Finish!" button.
    void OnWizardCreate()
    {
    }
}

```

* * *
