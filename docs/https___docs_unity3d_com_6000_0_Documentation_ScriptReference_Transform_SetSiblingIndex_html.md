* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.SetSiblingIndex.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).SetSiblingIndex
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html "Go to Transform Component in the Manual")
## Declaration
public void SetSiblingIndex(int index); 
### Parameters
Parameter | Description  
---|---  
index | Index to set.  
### Description
Sets the sibling index.
Use this to change the sibling index of the GameObject. If a GameObject shares a parent with other GameObjects and are on the same level (i.e. they share the same direct parent), these GameObjects are known as siblings. The sibling index shows where each GameObject sits in this sibling hierarchy.  
  
Use SetSiblingIndex to change the GameObject’s place in this hierarchy. When the sibling index of a GameObject is changed, its order in the Hierarchy window will also change. This is useful if you are intentionally ordering the children of a GameObject such as when using Layout Group components.  
  
Layout Groups will also visually reorder the group by their index. To read more about Layout Groups see [AutoLayout](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-UIAutoLayout.html). To return the sibling index of a GameObject, see [Transform.GetSiblingIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.GetSiblingIndex.html).
```
//This script demonstrates how to return (GetSiblingIndex) and change (SetSiblingIndex) the sibling index of a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
//Attach this script to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you would like to change the sibling index of.
//To see this in action, make this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) the child of another GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), and create siblings for it.  
  
using UnityEngine;  
  
public class TransformGetSiblingIndex : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Use this to change the hierarchy of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) siblings
    int m_IndexNumber;  
  
    void Start()
    {
        //Initialise the Sibling Index to 0
        m_IndexNumber = 0;
        //Set the Sibling Index
        transform.SetSiblingIndex(m_IndexNumber);
        //Output the Sibling Index to the console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Sibling Index : " + transform.GetSiblingIndex());
    }  
  
    void OnGUI()
    {
        //Press this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) to increase the sibling index number of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 200, 40), "Add Index Number"))
        {
            //Make sure the index number doesn't exceed the Sibling Index by more than 1
            if (m_IndexNumber <= transform.GetSiblingIndex())
            {
                //Increase the Index Number
                m_IndexNumber++;
            }
        }  
  
        //Press this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) to decrease the sibling index number of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 40, 200, 40), "Minus Index Number"))
        {
            //Make sure the index number doesn't go below 0
            if (m_IndexNumber >= 1)
            {
                //Decrease the index number
                m_IndexNumber--;
            }
        }
        //Detect if any of the Buttons are being pressed
        if (GUI.changed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html))
        {
            //Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) the Sibling Index of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
            transform.SetSiblingIndex(m_IndexNumber);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Sibling Index : " + transform.GetSiblingIndex());
        }
    }
}

```

* * *
