* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-objects.html

#  [Selection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html).objects
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
objects; 
### Description
The actual unfiltered selection from the Scene.
All objects will be returned, including assets in projects. You can also assign objects to the selection.  
  
Additional resources: [Selection.instanceIDs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-instanceIDs.html).  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/SelectAllOfTag.png)  
_Scriptable Wizard that lets you select GameObjects by their tag._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class SelectAllOfTag : ScriptableWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html)
{
    public string tagName = "ExampleTag";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Select All of Tag...")]
    static void SelectAllOfTagWizard()
    {
        ScriptableWizard.DisplayWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.DisplayWizard.html)(
            "Select All of Tag...",
            typeof(SelectAllOfTag),
            "Make Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html)");
    }  
  
    void OnWizardCreate()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] gos = GameObject.FindGameObjectsWithTag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.FindGameObjectsWithTag.html)(tagName);
        Selection.objects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-objects.html) = gos;
    }
}

```

* * *
