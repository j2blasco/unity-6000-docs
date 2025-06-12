* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-y.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).y
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
y; 
### Description
Y component of the vector.
```
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
// Create two Input[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) Fields in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) (Create>UI>Input[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) Field)
// Click on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and attach both Input[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) Fields in the Inspector window  
  
using UnityEngine;
using UnityEngine.UI;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_NewPosition;  
  
    // Attach these in the Inspector window
    public InputField m_InputFieldX, m_InputFieldY;  
  
    // These are the strings that are returned from the InputFields
    string xString, yString;  
  
    // These are used when converting the strings to floats
    float m_XValue, m_YValue;  
  
    void Start()
    {
        // Initialise the vector
        m_NewPosition = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 0.0f, 0.0f);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Store the inputs from the InputFields as strings
        xString = m_InputFieldX.text;
        yString = m_InputFieldY.text;  
  
        // Convert the strings from the InputFields to floats
        ConvertStringsToFloats(xString, yString);  
  
        // Change the NewPosition Vector's x and y components
        m_NewPosition.x = m_XValue;
        m_NewPosition.y = m_YValue;  
  
        // Change the position depending on the vector
        transform.position = m_NewPosition;
    }  
  
    void ConvertStringsToFloats(string XVal, string YVal)
    {
        try
        {
            // Convert the strings to floats
            m_XValue = float.Parse(XVal);
            m_YValue = float.Parse(YVal);
        }
        catch{}
    }
}

```

* * *
