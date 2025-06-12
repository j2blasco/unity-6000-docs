* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-x.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).x
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
x; 
### Description
X component of the vector.
Use this to modify or return the X component of a vector.
```
// This script moves a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to a new x position using Vector3.x[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-x.html).
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
// Set your x position in the Inspector  
  
using UnityEngine;  
  
public class Examples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_NewPosition;
    // This is the new X position. Set it in the Inspector.
    public float m_XPosition;  
  
    // Use this for initialization
    void Start()
    {
        // Initialise the vector
        m_NewPosition = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 0.0f, 0.0f);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Press the space key to change the x component of the vector
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            m_NewPosition.x = m_XPosition;
        }
        // Change the position depending on the vector
        transform.position = m_NewPosition;
    }
}

```

Below is another example that allows you to manipulate the GameObject’s x and y positions. Just type an x and y position in the Input Fields in Play Mode.
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
  
    // Use this for initialization
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
